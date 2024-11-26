# API key and base URL
API_KEY = "abd882d5f30e477d91d45604242511"
BASE_URL = "http://api.weatherapi.com/v1/history.json"

# Function to get weather data for a specific date
def get_weather(city, date):
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
        print(f"Couldn't get data for {date}. Status: {response.status_code}")
        return None

# Collect weather data for a range of dates
def get_weather_data(city, start_date, end_date):
    current_date = start_date
    all_weather = []
    while current_date <= end_date:
        print(f"Getting weather for {current_date}...")
        weather = get_weather(city, current_date.strftime("%Y-%m-%d"))
        if weather:
            all_weather.append(weather)
        current_date += timedelta(days=1)
    return all_weather

# Main script
if __name__ == "__main__":
    # Define the city and date range
    city = "Durham, North Carolina"
    today = datetime.today()
    last_year = today - timedelta(days=365)

    # Fetch the weather data
    print("Starting to get weather data...")
    weather_data = get_weather_data(city, last_year, today)

    # Save to CSV if we got any data
    if len(weather_data) > 0:
        df = pd.DataFrame(weather_data)
        df.to_csv("durham_weather_data_last_365_days.csv", index=False)
        print("Saved the weather data to 'durham_weather_data_last_365_days.csv'.")
    else:
        print("No weather data found.")
