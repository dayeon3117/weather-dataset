import requests
import pandas as pd
from datetime import datetime, timedelta

# Step 1: Set up API key and base URL
API_KEY = "abd882d5f30e477d91d45604242511"  # Replace with your WeatherAPI key
BASE_URL = "http://api.weatherapi.com/v1/forecast.json"

# Step 2: Function to fetch forecasted weather data for a specific date
def fetch_forecast_data(city, days=10):
    params = {
        "key": API_KEY,
        "q": city,
        "days": days
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        forecast_data = []
        for day in data["forecast"]["forecastday"]:
            forecast_data.append({
                "date": day["date"],
                "city": city,
                "temperature_c": day["day"]["avgtemp_c"],
                "humidity": day["day"]["avghumidity"],
                "precipitation_mm": day["day"]["totalprecip_mm"]
            })
        return forecast_data
    else:
        print(f"Failed to fetch forecast data. Status code: {response.status_code}")
        return []

# Step 3: Fetch forecasted data for the next 300 days
def collect_forecast_data(city, total_days=300):
    forecast_data = []
    days_per_request = 10  # Maximum allowed forecast days per API call
    current_date = datetime.today()
    
    while total_days > 0:
        print(f"Fetching forecast data for next {min(days_per_request, total_days)} days starting {current_date}...")
        data = fetch_forecast_data(city, days=min(days_per_request, total_days))
        if data:
            forecast_data.extend(data)
        total_days -= days_per_request
        current_date += timedelta(days=days_per_request)
    
    return forecast_data

# Step 4: Main script for fetching and saving forecast data
if __name__ == "__main__":
    city = "Durham, North Carolina"
    total_days = 300  # Forecast for the next 300 days

    print("Starting forecast data collection...")
    forecast_weather_data = collect_forecast_data(city, total_days=total_days)
    
    # Save to CSV
    if forecast_weather_data:
        df_forecast = pd.DataFrame(forecast_weather_data)
        df_forecast.to_csv("durham_weather_forecast_next_300_days.csv", index=False)
        print("Forecast data saved to 'durham_weather_forecast_next_300_days.csv'.")
    else:
        print("No forecast data collected.")
