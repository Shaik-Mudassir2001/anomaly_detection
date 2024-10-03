# main.py
from src.data_stream import generate_data_stream
from src.anomaly_detection import moving_average_anomaly_detection
from src.visualization import visualize_stream

def main():
    # 1. Generate the Data Stream
    data_stream = generate_data_stream(n=1000)

    # 2. Run Anomaly Detection
    anomalies = moving_average_anomaly_detection(data_stream, window_size=50, threshold=3)

    # 3. Visualize the Results
    visualize_stream(data_stream, anomalies)

if __name__ == "__main__":
    main()
