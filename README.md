# 🏥 MedSecure AI : Cybersecurity Command Center

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Status](https://img.shields.io/badge/status-Live_Demo-success)

**MedSecure AI** is a state-of-the-art cybersecurity and privacy preservation framework designed specifically for the healthcare sector. It provides an impenetrable defense system for Electronic Health Records (EHR) by combining generative AI for data anonymization, cryptographic blockchains for audit logging, and active honeypot traps for threat neutralization.

---

## 🚀 Core Technologies & Features

### 1. GAN Synthetic Data Engine
To prevent the exposure of sensitive Protected Health Information (PHI), MedSecure AI uses Generative Adversarial Networks (GANs).
*   **The Process:** Upload raw patient datasets (CSV/HL7). The AI synthesizes entirely new, mathematically equivalent records.
*   **The Result:** Researchers and third-party analysts can work with high-fidelity data without ever touching real patient records, ensuring 100% HIPAA compliance.

### 2. Immutable Blockchain Audit Ledger
Traditional databases can be tampered with. MedSecure AI routes every single interaction through a custom cryptographic blockchain.
*   **Tamper-Proof:** Every data synthesis, vault access request, and system event is permanently hashed into the ledger.
*   **Forensics:** In the event of a breach, investigators have a perfect, unalterable timeline of the attack vector.

### 3. Interactive Honeypot Defense System
Instead of just building a wall, MedSecure AI actively hunts attackers.
*   **Decoys:** Deploys highly attractive, fake data assets (e.g., `VIP_Patient_Records.decoy`, `DECOY-DB-04`) around the perimeter of the real data vault.
*   **Instant Lockdown:** If a malicious actor probes a decoy, the system immediately locks down the real data vault, blocks exfiltration, and triggers a visual command center alarm.

### 4. Threat Resolution HUD
A professional, glassmorphic command center dashboard that allows administrators to actively monitor and resolve threats.
*   **Active Threat Analysis:** View the attacker's IP, Geo-Location, and SQL Injection vectors in real time.
*   **Firewall Integration:** A one-click "Ban IP & Seal Perimeter" protocol that neutralizes the threat, logs the action to the blockchain, and restores the system to a secure state.

---

## 🛠️ Tech Stack

*   **Frontend:** HTML5, Vanilla JavaScript, CSS3 (Custom Glassmorphism UI)
*   **Backend:** Python, Flask API
*   **Security Ledger:** Custom Python-based Cryptographic Blockchain (`hashlib`, `time`)
*   **AI Synthesis:** (Simulated/Integrated) Generative Adversarial Networks

---

## 📦 Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/medsecure-ai.git
    cd medsecure-ai/backend
    ```

2.  **Install Dependencies**
    Ensure you have Python installed, then run:
    ```bash
    pip install Flask werkzeug
    ```

3.  **Run the Command Center**
    ```bash
    python app.py
    ```

4.  **Access the Dashboard**
    Open your web browser and navigate to:
    `http://127.0.0.1:5000`

---

## 📋 Running the Live Presentation Demo

If you are presenting MedSecure AI to judges or stakeholders, follow this exact workflow:

1.  **The Synthesis Demo:** Navigate to the "Synthetic Data" tab. Click **Run GAN Synthesis** to watch the progress bar generate fake data, then click **Download Synthetic** to prove the file generates.
2.  **The Blockchain Demo:** Navigate to the "Blockchain Audit" tab. Click **Audit Entire Chain** to show the terminal decoding the cryptographic blocks live.
3.  **The Attack Demo:** Click the green **System Secure** pill in the top right corner. The system will simulate a critical privacy breach, locking down the UI with a full-screen red warning.
4.  **The Resolution Demo:**
    *   Click **Override Lockdown**.
    *   Navigate to the **Honeypot** page (Notice `DECOY-PT-001` is flashing red).
    *   Click **🚨 Investigate Alerts** to open the Threat Analysis HUD.
    *   Click **Ban IP & Seal Perimeter**. The system will visually execute the firewall protocol, log the permanent IP ban to the blockchain, and restore the dashboard to a secure green state!

---

## 🔒 Security Disclaimer

> **Important:** MedSecure AI is a demonstration prototype designed for hackathons and presentations. Do not deploy this in a live clinical environment handling real HIPAA patient data without integrating a production-ready Web3 ledger (e.g., Ethereum/Hyperledger) and passing a rigorous third-party penetration test.

---

## 📄 License
Distributed under the MIT License.
