import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource
import altair as alt
from scipy.stats import ttest_ind
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

sns.set(style="whitegrid")

# Load data
historical_data = pd.read_csv("data/durham_weather_data_last_365_days.csv")
forecast_data = pd.read_csv("data/durham_weather_simulated_next_365_days.csv")

# Check missing values
print("Missing values in historical data")
print(historical_data.isnull().sum())

print("Missing values in forecast data")
print(forecast_data.isnull().sum())

# Get summary statistics
print(historical_data.describe())
print(forecast_data.describe())

# Combine historical and forecast data
combined_data = pd.concat([historical_data, forecast_data]).reset_index(drop=True)
historical_data['source'] = 'Historical'
forecast_data['source'] = 'Forecasted'

# 'month' column is added to datasets
historical_data.loc[:, 'month'] = pd.to_datetime(historical_data['date']).dt.month
forecast_data.loc[:, 'month'] = pd.to_datetime(forecast_data['date']).dt.month

# Group by month to calculate averages
historical_monthly_avg = historical_data.groupby('month')[['temperature_c', 'humidity', 'precipitation_mm']].mean()
forecast_monthly_avg = forecast_data.groupby('month')[['temperature_c', 'humidity', 'precipitation_mm']].mean()

# Combine into a single DataFrame for comparison
monthly_comparison = pd.DataFrame({
    'Historical Temperature_c': historical_monthly_avg['temperature_c'],
    'Forecast Temperature_c': forecast_monthly_avg['temperature_c'],
    'Historical Humidity': historical_monthly_avg['humidity'],
    'Forecast Humidity': forecast_monthly_avg['humidity'],
    'Historical Precipitation_mm': historical_monthly_avg['precipitation_mm'],
    'Forecast Precipitation_mm': forecast_monthly_avg['precipitation_mm']
}).reset_index()

# Line Graphs for each variable
for col in ['temperature_c', 'humidity', 'precipitation_mm']:
    plt.figure(figsize=(10, 5))
    
    # Plot historical data
    plt.plot(
        range(1, 13),
        monthly_comparison[f'Historical {col.capitalize()}'],
        label=f'Historical {col.capitalize()}',
        marker='o'
    )
    
    # Plot forecasted data
    plt.plot(
        range(1, 13),
        monthly_comparison[f'Forecast {col.capitalize()}'],
        label=f'Forecast {col.capitalize()}',
        marker='o'
    )
    
    # Set the title and labels
    if col == 'temperature_c':
        plt.title("Monthly Average Temperature: Historical vs Forecast")
        plt.ylabel("Temperature (°C)")
    elif col == 'humidity':
        plt.title("Monthly Average Humidity: Historical vs Forecast")
        plt.ylabel("Humidity (%)")
    elif col == 'precipitation_mm':
        plt.title("Monthly Average Precipitation: Historical vs Forecast")
        plt.ylabel("Precipitation (mm)")
    
    plt.xlabel("Month")
    plt.xticks(range(1, 13), ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], rotation=45)
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()


# Calculate correlation matrices
historical_corr = historical_data[['temperature_c', 'humidity', 'precipitation_mm']].corr()
forecast_corr = forecast_data[['temperature_c', 'humidity', 'precipitation_mm']].corr()

# Now you can plot heatmaps
plt.figure(figsize=(8, 6))
sns.heatmap(historical_corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix (Historical Data)")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
sns.heatmap(forecast_corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix (Forecast Data)")
plt.tight_layout()
plt.show()

# Add 'source' column
historical_data['source'] = 'Historical'
forecast_data['source'] = 'Forecasted'

# Combine datasets
combined_data = pd.concat([historical_data, forecast_data], ignore_index=True)

#Boxplots for temperature
plt.figure()
sns.boxplot(data=combined_data, x='source', y='temperature_c')
plt.title("Temperature: Historical vs Forecasted")
plt.show()

# Boxplots for humidity
plt.figure()
sns.boxplot(data=combined_data, x='source', y='humidity')
plt.title("Humidity: Historical vs Forecasted")
plt.show()

# Boxplot for precipitation
plt.figure()
sns.boxplot(data=combined_data, x='source', y='precipitation_mm', width=0.5, fliersize=3)
sns.stripplot(data=combined_data, x='source', y='precipitation_mm', color='black', alpha=0.4, jitter=0.2)
plt.title("Precipitation Distribution: Historical vs Forecasted")
plt.xlabel("Source")
plt.ylabel("Precipitation (mm)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Define thresholds for extreme weather
extreme_precipitation = combined_data[combined_data['precipitation_mm'] > combined_data['precipitation_mm'].quantile(0.95)]
extreme_temperature = combined_data[(combined_data['temperature_c'] < combined_data['temperature_c'].quantile(0.05)) | 
                                     (combined_data['temperature_c'] > combined_data['temperature_c'].quantile(0.95))]

# Scatter plot
plt.figure(figsize=(12, 6))
plt.scatter(combined_data['date'], combined_data['temperature_c'], color='gray', alpha=0.5, label='Normal Days')
plt.scatter(extreme_precipitation['date'], extreme_precipitation['temperature_c'], color='blue', label='Extreme Precipitation')
plt.scatter(extreme_temperature['date'], extreme_temperature['temperature_c'], color='red', label='Extreme Temperature')
plt.title('Extreme Weather Days')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(alpha=0.3)
plt.show()


# Add 'season' column to both datasets
def assign_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Fall'

historical_data['season'] = historical_data['month'].apply(assign_season)
forecast_data['season'] = forecast_data['month'].apply(assign_season)

# Group by season and calculate average temperature
historical_seasonal_temp = historical_data.groupby('season')['temperature_c'].mean()
forecast_seasonal_temp = forecast_data.groupby('season')['temperature_c'].mean()

historical_seasonal_precip = historical_data.groupby('season')['precipitation_mm'].mean()
forecast_seasonal_precip = forecast_data.groupby('season')['precipitation_mm'].mean()

historical_seasonal_humidity = historical_data.groupby('season')['humidity'].mean()
forecast_seasonal_humidity = forecast_data.groupby('season')['humidity'].mean()

# Combine into a DataFrame
seasonal_temp_comparison = pd.DataFrame({
    'Historical': historical_seasonal_temp,
    'Forecasted': forecast_seasonal_temp
})
seasonal_precip_comparison = pd.DataFrame({
    'Historical': historical_seasonal_precip,
    'Forecasted': forecast_seasonal_precip
})

seasonal_humidity_comparison = pd.DataFrame({
    'Historical': historical_seasonal_humidity,
    'Forecasted': forecast_seasonal_humidity
})

# Plot for temperature
seasonal_temp_comparison.plot(kind='bar', figsize=(8, 5))
plt.title("Seasonal Average Temperature: Historical vs Forecasted", fontsize=14)
plt.xlabel("Season")
plt.ylabel("Average Temperature (°C)")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Plot for Precipitation
seasonal_precip_comparison.plot(kind='bar', figsize=(8, 5))
plt.title("Seasonal Average Precipitation: Historical vs Forecasted", fontsize=14)
plt.xlabel("Season")
plt.ylabel("Average Precipitation (mm)")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Plot for Humidity
seasonal_humidity_comparison.plot(kind='bar', figsize=(8, 5))
plt.title("Seasonal Average Humidity: Historical vs Forecasted", fontsize=14)
plt.xlabel("Season")
plt.ylabel("Average Humidity (%)")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# --- Statistical Tests ---
print("\n--- Statistical Tests ---")
for variable in ['temperature_c', 'humidity', 'precipitation_mm']:
    t_stat, p_value = ttest_ind(
        historical_data[variable],
        forecast_data[variable],
        equal_var=False
    )
    print(f"{variable.capitalize()} T-Test: t-statistic = {t_stat:.3f}, p-value = {p_value:.3e}")


# --- Variability Analysis ---
print("\n--- Variability Analysis ---")
for dataset, name in [(historical_data, "Historical"), (forecast_data, "Forecasted")]:
    print(f"\n{name} Data Variability:")
    print(dataset[['temperature_c', 'humidity', 'precipitation_mm']].agg(['std', 'var']))


# --- Seasonal Decomposition ---
print("\n--- Seasonal Decomposition ---")
historical_temp = historical_data.set_index('date')['temperature_c']
seasonal_decompose_result = seasonal_decompose(historical_temp, model='additive', period=12)

# Plot Seasonal Components
seasonal_decompose_result.plot()
plt.tight_layout()
plt.show()
