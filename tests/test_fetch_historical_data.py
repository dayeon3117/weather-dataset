import unittest
from datetime import datetime, timedelta
from src.fetch_historical_data import get_weather, get_weather_data

class TestFetchHistoricalData(unittest.TestCase):

    def test_get_weather_valid(self):
        # Test for a valid date
        result = get_weather("Durham, North Carolina", "2023-01-01")
        self.assertIsNotNone(result)
        self.assertIn("temperature_c", result)
        self.assertIn("humidity", result)
        self.assertIn("precipitation_mm", result)

    def test_get_weather_invalid_date(self):
        # Test for an invalid date
        result = get_weather("Durham, North Carolina", "invalid-date")
        self.assertIsNone(result)

    def test_get_weather_data(self):
        # Test fetching data for a range of dates
        start_date = datetime.today() - timedelta(days=7)
        end_date = datetime.today()
        data = get_weather_data("Durham, North Carolina", start_date, end_date)
        self.assertGreater(len(data), 0)
        for record in data:
            self.assertIn("temperature_c", record)
            self.assertIn("humidity", record)
            self.assertIn("precipitation_mm", record)

if __name__ == "__main__":
    unittest.main()

