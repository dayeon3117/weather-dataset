import pandas as pd
import random
from datetime import datetime, timedelta

# API Key and Base URL (not used here but leaving it for reference)
API_KEY = "abd882d5f30e477d91d45604242511"
BASE_URL = "http://api.weatherapi.com/v1/history.json"

# Load last 365 days of weather data
last_365_days_file = "durham_weather_data_last_365_days.csv"
last_365_data = pd.read_csv(last_365_days_file)

# Monthly average weather info for Durham, NC
monthly_averages = {
    "January": {"high": 10, "low": -3, "rain_days": 8},
    "February": {"high": 12, "low": -2, "rain_days": 7},
    "March": {"high": 17, "low": 2, "rain_days": 8},
    "April": {"high": 22, "low": 7, "rain_days": 7},
    "May": {"high": 26, "low": 12, "rain_days": 8},
    "June": {"high": 30, "low": 17, "rain_days": 7},
    "July": {"high": 32, "low": 20, "rain_days": 8},
    "August": {"high": 31, "low": 19, "rain_days": 7},
    "September": {"high": 27, "low": 15, "rain_days": 6},
    "October": {"high": 22, "low": 8, "rain_days": 5},
    "November": {"high": 17, "low": 3, "rain_days": 6},
    "December": {"high": 12, "low": -1, "rain_days": 7},
}

# Simulate weather for one day
def simulate_weather(date, month):
    avg = monthly_averages[month]
    temp = round(random.uniform(avg["low"], avg["high"]), 1)
    humidity = random.randint(40, 80)
    rain_chance = random.randint(1, 30)
    precip = round(random.uniform(0, 20), 2) if rain_chance <= avg["rain_days"] else 0.0
    return {
        "date": date.strftime("%Y-%m-%d"),
        "city": "Durham, North Carolina",
        "temperature_c": temp,
        "humidity": humidity,
        "precipitation_mm": precip,
    }

# Simulate the next 365 days of weather
start_date = datetime.strptime(last_365_data["date"].max(), "%Y-%m-%d") + timedelta(days=1)
simulated_weather = []

for i in range(365):
    current_date = start_date + timedelta(days=i)
    month_name = current_date.strftime("%B")
    simulated_weather.append(simulate_weather(current_date, month_name))

# Save simulated data to CSV
simulated_df = pd.DataFrame(simulated_weather)
simulated_df.to_csv("durham_weather_simulated_next_365_days.csv", index=False)
print("Simulated weather data saved to 'durham_weather_simulated_next_365_days.csv'")
