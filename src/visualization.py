# src/visualization.py
import matplotlib.pyplot as plt

def visualize_stream(data, anomalies):
    """Visualizes the data stream and marks detected anomalies."""
    plt.figure(figsize=(12, 6))
    plt.plot(data, label="Data Stream")
    for idx, value in anomalies:
        plt.scatter(idx, value, color='red', label="Anomaly" if idx == anomalies[0][0] else "")
    plt.title("Real-Time Data Stream with Anomalies")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.legend()
    plt.show()
