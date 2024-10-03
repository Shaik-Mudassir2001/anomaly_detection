import unittest
from src.data_stream import generate_data_stream

class TestDataStream(unittest.TestCase):

    def test_generate_data_stream_length(self):
        """Test if the generated data stream has the correct length."""
        length = 100
        data = generate_data_stream(length)
        self.assertEqual(len(data), length)

    def test_generate_data_stream_value_range(self):
        """Test if the values in the data stream are within a specified range."""
        length = 100
        data = generate_data_stream(length)
        for value in data:
            self.assertTrue(0 <= value <= 100)  # Assuming data values are between 0 and 100

if __name__ == '__main__':
    unittest.main()
