import unittest
import pandas as pd
from src.EDA import historical_data, forecast_data, combined_data

class TestEDA(unittest.TestCase):

    def test_historical_data_loading(self):
        # Ensure historical data is loaded properly
        self.assertFalse(historical_data.empty)
        self.assertIn("temperature_c", historical_data.columns)
        self.assertIn("humidity", historical_data.columns)
        self.assertIn("precipitation_mm", historical_data.columns)

    def test_forecast_data_loading(self):
        # Ensure forecast data is loaded properly
        self.assertFalse(forecast_data.empty)
        self.assertIn("temperature_c", forecast_data.columns)
        self.assertIn("humidity", forecast_data.columns)
        self.assertIn("precipitation_mm", forecast_data.columns)

    def test_combined_data(self):
        # Check combined dataset structure
        self.assertFalse(combined_data.empty)
        self.assertEqual(len(combined_data), len(historical_data) + len(forecast_data))
        self.assertIn("source", combined_data.columns)

if __name__ == "__main__":
    unittest.main()

