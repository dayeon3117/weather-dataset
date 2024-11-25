import requests
import pandas as pd
from datetime import datetime, timedelta

# Step 1: Set up API key and base URL
API_KEY = "abd882d5f30e477d91d45604242511"  # Replace with your WeatherAPI key
BASE_URL = "http://api.weatherapi.com/v1/history.json"

# Step 2: Function to fetch weather data for a specific date
def fetch_weather_data(city, date):
    params = {
        "key": API_KEY,
        "q": city,
        "dt": date
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "date": date,
            "city": city,
            "temperature_c": data["forecast"]["forecastday"][0]["day"]["avgtemp_c"],
            "humidity": data["forecast"]["forecastday"][0]["day"]["avghumidity"],
            "precipitation_mm": data["forecast"]["forecastday"][0]["day"]["totalprecip_mm"]
        }
    else:
        print(f"Failed to fetch data for {date}. Status code: {response.status_code}")
        return None

# Step 3: Collect data for the last 365 days
def collect_weather_data(city, start_date, end_date):
    current_date = start_date
    weather_data = []
    
    while current_date <= end_date:
        print(f"Fetching data for {current_date}...")
        data = fetch_weather_data(city, current_date.strftime("%Y-%m-%d"))
        if data:
            weather_data.append(data)
        current_date += timedelta(days=1)  # Move to the next day
    
    return weather_data

# Step 4: Main script
if __name__ == "__main__":
    # Define city and date range
    city = "Durham, North Carolina"
    end_date = datetime.today()
    start_date = end_date - timedelta(days=365)  # Limit to the last 365 days
    
    # Fetch weather data
    print("Starting data collection...")
    weather_data = collect_weather_data(city, start_date, end_date)
    
    # Save to CSV
    if weather_data:
        df = pd.DataFrame(weather_data)
        df.to_csv("durham_weather_data_last_365_days.csv", index=False)
        print("Weather data saved to 'durham_weather_data_last_365_days.csv'.")
    else:
        print("No data collected.")
