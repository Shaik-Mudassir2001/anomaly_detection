# tests/test_anomaly_detection.py
import sys
import os
import unittest
from src.anomaly_detection import moving_average_anomaly_detection

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestAnomalyDetection(unittest.TestCase):
    def test_moving_average_detection(self):
        # Create a test data stream
        test_stream = [1, 1, 1, 1, 1, 20, 1, 1, 1, 1, 1]  # Introduce an anomaly at index 5
        anomalies = moving_average_anomaly_detection(test_stream, window_size=3, threshold=3)

        # Check if anomaly is detected at the correct index
        self.assertEqual(len(anomalies), 1)
        self.assertEqual(anomalies[0][0], 5)

if __name__ == '__main__':
    unittest.main()
