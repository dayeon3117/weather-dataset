import unittest
from datetime import datetime
from src.fetch_forecast_data import simulate_weather

class TestFetchForecastData(unittest.TestCase):

    def test_simulate_weather(self):
        # Test simulating weather for a specific date
        test_date = datetime(2024, 1, 1)
        result = simulate_weather(test_date, "January")
        self.assertIsInstance(result, dict)
        self.assertIn("temperature_c", result)
        self.assertIn("humidity", result)
        self.assertIn("precipitation_mm", result)
        self.assertGreaterEqual(result["temperature_c"], -3)  # Low for January
        self.assertLessEqual(result["temperature_c"], 10)    # High for January

    def test_simulated_weather_for_year(self):
        # Test generating weather for 365 days
        start_date = datetime(2024, 1, 1)
        simulated_weather = []
        for i in range(365):
            current_date = start_date + timedelta(days=i)
            simulated_weather.append(simulate_weather(current_date, current_date.strftime("%B")))
        self.assertEqual(len(simulated_weather), 365)
        for record in simulated_weather:
            self.assertIn("temperature_c", record)
            self.assertIn("humidity", record)
            self.assertIn("precipitation_mm", record)

if __name__ == "__main__":
    unittest.main()
