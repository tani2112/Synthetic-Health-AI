import pandas as pd
from sdv.single_table import GaussianCopulaSynthesizer
from sdv.metadata import SingleTableMetadata

def generate_synthetic_data(input_csv):
    # Load raw data
    real_data = pd.read_csv(input_csv)
    
    # Auto-detect metadata (PII protection)
    metadata = SingleTableMetadata()
    metadata.detect_from_dataframe(data=real_data)
    
    # Train the GAN model
    synthesizer = GaussianCopulaSynthesizer(metadata)
    synthesizer.fit(real_data)
    
    # Generate 100 synthetic records
    synthetic_data = synthesizer.sample(num_rows=100)
    return synthetic_data