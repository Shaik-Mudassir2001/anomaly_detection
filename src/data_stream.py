# src/data_stream.py
import numpy as np

def generate_data_stream(n=1000):
    """Generates a synthetic data stream with seasonality, noise, and anomalies."""
    seasonality = np.sin(np.linspace(0, 20, n))      # Create a sinusoidal seasonal pattern
    noise = np.random.normal(0, 0.5, n)              # Add random Gaussian noise
    anomalies = np.zeros(n)                          # Add anomalies as zero by default
    anomalies[100] = 10                              # Introduce a spike at index 100
    anomalies[600] = -5                              # Introduce a dip at index 600

    # Combine components to create the data stream
    data_stream = seasonality + noise + anomalies
    return data_stream
