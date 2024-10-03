# Efficient Data Stream Anomaly Detection

## Project Overview
This project implements a solution to detect anomalies in a continuous data stream, simulating real-time scenarios such as financial transactions or system metrics. The goal is to develop a Python script that identifies unusual patterns, such as sudden spikes or dips, using efficient algorithms that can adapt to changing data trends.

The project is structured to handle real-time data streams, optimize for performance, and provide visualization to highlight detected anomalies.

## Features
- **Real-Time Data Stream Simulation**: Generates synthetic data with seasonal patterns, noise, and anomalies.
- **Anomaly Detection Algorithms**: Includes a simple moving average-based method and can be extended with more sophisticated techniques.
- **Real-Time Visualization**: Displays the data stream and marks detected anomalies in an intuitive plot.
- **Modular Codebase**: Clean, modular structure for easy extension and testing.


## Getting Started

### Prerequisites
- Python 3.x
- Required libraries (if using `requirements.txt`):


### Installation
1. **Clone the Repository**:
  git clone https://github.com/Shaik-Mudassir2001/anomaly_detection_project.git

2. **Set Up the Environment**:
- Create a virtual environment (optional but recommended):
  ```
  python -m venv venv
  source venv/bin/activate  # For Linux/Mac
  venv\Scripts\activate     # For Windows
  ```

- Install dependencies using `requirements.txt`:
  ```
  pip install -r requirements.txt
  ```

3. **Run the Project**:
Execute the main script to generate the data stream, detect anomalies, and visualize the results:

## Project Modules
1. **`src/data_stream.py`**:
- Generates a continuous data stream with seasonality, random noise, and injected anomalies for testing purposes.

2. **`src/anomaly_detection.py`**:
- Implements a simple **Moving Average Anomaly Detection** algorithm.
- Anomalies are detected if a point significantly deviates from the rolling average by a specified threshold.

3. **`src/visualization.py`**:
- Visualizes the data stream and highlights the detected anomalies using `matplotlib`.

4. **`main.py`**:
- Combines all modules to simulate the data stream, run the detection algorithm, and visualize the results.

## How to Customize
- **Change the Data Stream Pattern**:
- Modify `generate_data_stream()` in `src/data_stream.py` to adjust the seasonality, noise, or anomaly patterns.

- **Implement a New Algorithm**:
- Create a new function in `src/anomaly_detection.py` and update `main.py` to use the new method.

- **Save or Log Results**:
- Update `main.py` to save plots or log anomaly information to the `results/` folder.

## Testing
Unit tests are included in the `tests/` directory to verify the behavior of the data stream and anomaly detection algorithms.

1. Run the tests using the following command:

2. Test files include:
- **`test_data_stream.py`**: Validates the data generation process.
- **`test_anomaly_detection.py`**: Verifies the accuracy and efficiency of the detection algorithm.

**Run the tests**: You can run each test file individually:
  python -m unittest tests/test_data_stream.py
  python -m unittest tests/test_anomaly_detection.py

Or run all **tests** in the tests directory:

  python -m unittest discover -s tests
