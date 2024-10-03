# src/anomaly_detection.py
import numpy as np
from collections import deque

def moving_average_anomaly_detection(stream, window_size=50, threshold=3):
    """Detects anomalies in a data stream using a simple moving average."""
    window = deque(maxlen=window_size)
    anomalies = []

    for index, value in enumerate(stream):
        if len(window) == window_size:
            mean = np.mean(window)
            std = np.std(window)
            if abs(value - mean) > threshold * std:
                anomalies.append((index, value))  # Store anomaly index and value
        window.append(value)

    return anomalies
