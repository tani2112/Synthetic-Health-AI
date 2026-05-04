from flask import Flask, jsonify, request, render_template, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
from blockchain import AuditChain
import os
import gan_engine

app = Flask(__name__)
CORS(app)
audit_trail = AuditChain()

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    # Serves your provided medsecure_ai_dashboard.html
    return render_template('medsecure_ai_dashboard.html')

@app.route('/api/blockchain', methods=['GET'])
def get_chain():
    return jsonify(audit_trail.chain)

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        last_block = audit_trail.get_last_block()
        audit_trail.create_block(proof=100, previous_hash=last_block['hash'], meta=f"Uploaded raw data: {filename}")
        
        return jsonify({"status": "success", "filename": filename})

@app.route('/api/synthesis/start', methods=['POST'])
def start_synthesis():
    filename = request.json.get('filename') if request.json else None
    if not filename:
        return jsonify({"error": "No filename provided"}), 400
        
    input_filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    output_filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'synthetic_data.csv')
    
    try:
        synthetic_data = gan_engine.generate_synthetic_data(input_filepath)
        synthetic_data.to_csv(output_filepath, index=False)
        
        last_block = audit_trail.get_last_block()
        audit_trail.create_block(proof=100, previous_hash=last_block['hash'], meta=f"GAN synthesis completed for {filename}")
        return jsonify({"status": "Training GAN complete", "blockchain_log": "Success"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/synthesis/download', methods=['GET'])
def download_synthetic():
    path = os.path.join(app.config['UPLOAD_FOLDER'], 'synthetic_data.csv')
    if os.path.exists(path):
        last_block = audit_trail.get_last_block()
        audit_trail.create_block(proof=100, previous_hash=last_block['hash'], meta="Synthetic data downloaded")
        return send_file(path, as_attachment=True)
    return jsonify({"error": "File not found"}), 404

@app.route('/api/honeypot/deploy', methods=['POST'])
def deploy_honeypot():
    trap_name = request.json.get('trap_name', 'UNKNOWN-TRAP')
    last_block = audit_trail.get_last_block()
    audit_trail.create_block(proof=100, previous_hash=last_block['hash'], meta=f"Honeypot trap deployed: {trap_name}")
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(port=5000, debug=True)