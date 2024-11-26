# Weather in Durham, North Carolina Dataset
## Executive Summary

Weather impacts almost every aspect of our daily lives, yet finding a combined dataset of historical and forecasted weather data that is organized and ready to use can be challenging. This project aims to solve that gap by creating a comprehensive dataset of weather data for Durham, NC, that spans a full year of historical data and a full year of simulated future weather data.

This dataset can serve as a valuable resource for researchers, data scientists, and weather enthusiasts interested in analyzing trends and patterns in temperature, precipitation, and humidity. Potential applications include climate research, predictive modeling, agricultural planning, and even urban development projects. The dataset brings together reliable past weather records and forecasted trends using NOAA’s averages for Durham, NC.

## Description of Data

This dataset includes:

- *Historical Data*: 365 days of actual weather data, collected using public APIs, WeatherAPI. The data includes daily temperature (°C), precipitation (mm), and humidity (%).

- *Forecast Data*: 365 days of simulated weather data based on NOAA’s monthly averages for Durham, NC. The simulated data includes the same metrics as the historical data: temperature (°C), precipitation (mm), and humidity (%). Future trends were modeled to reflect seasonal patterns and weather variability.

## Data Structure

The dataset is organized into the following columns:
- date: The date of the weather observation or forecast
- temperature_c: The average temperature in degrees Celsius for the day
- precipitation_mm: The total precipitation in millimeters for the day
- humidity: The average humidity percentage for the day

The data is stored in two CSV files:
- durham_weather_data_last_365_days.csv: Contains historical data
- durham_weather_simulated_next_365_days.csv: Contains simulated forecast data based on NOAA averages

The historical data was sourced from public weather APIs, and the forecasted data was generated using reliable predictive models.

## Review of Previous Datasets
Review of Previous Datasets

Existing weather datasets, such as those available from NOAA or WeatherAPI, focus heavily on raw historical data or rely on incomplete forecast models. While these datasets are useful, they often:

- Lack an integrated structure combining past and future trends
- Require significant cleaning and processing for analysis
- Do not provide pre-simulated future data based on trusted local averages

This dataset is unique in that it combines historical data with simulated future weather based on Durham’s NOAA averages. The data is pre-processed, labeled, and ready for analysis, making it a one-stop resource for studying year-long weather patterns in Durham.

## Power Analysis
To ensure the dataset is meaningful for trend analysis, a power analysis was conducted. The goal was to have sufficient sample size to observe seasonal patterns and test for differences between historical and forecast data. By including one full year of historical and forecasted data, the dataset covers all seasons, allowing for reliable comparisons across months and seasons.

Key considerations:
- Sample Size: A full year (365 days) ensures enough data to detect significant seasonal trends
- Effect Size: Seasonal differences in temperature, humidity, and precipitation were modeled to detect meaningful variations
- Power Level: Using an 80% power threshold, the chosen sample size supports robust statistical tests

The choice of 365 days for both historical and simulated data ensures full seasonal coverage. This decision was made to:

- Capture all seasonal variations and annual trends, such as summer highs and winter lows
- Provide a robust basis for studying year-to-year differences in weather trends
- Ensure there are enough data points to build meaningful statistical models and visualizations


## Sample Size Justification
A sample size of 365 days for each dataset (historical and forecasted) ensures adequate representation of all four seasons while preventing over-reliance on specific months. This is critical because smaller datasets would fail to capture seasonal trends, while larger datasets could introduce redundancy and increase storage requirements unnecessarily.

## Statistical Power
Power analysis ensures that we have enough data to detect meaningful differences between historical and forecasted weather patterns. With 365 days of data, I can confidently:

- Detect statistically significant seasonal differences (ex. summer vs. winter temperatures)
- Compare historical and simulated weather trends with enough data points to avoid p-hacking or misinterpretations

## Tools Used to Source Data
- Historical Data: Collected using the WeatherAPI with Durham, NC, as the location. The API allows retrieval of daily weather records, which were compiled into a CSV file.
- Simulated Forecast Data: Simulated using NOAA's historical monthly averages for Durham, NC. Random variations were added to replicate realistic weather conditions while adhering to NOAA’s seasonal trends.

The script for data sourcing and simulation is included in the GitHub repository (https://github.com/dayeon3117/weather-dataset/tree/main).

## Exploratory Data Analysis (EDA)
Key Findings:
1) Temperature Trends
- Historical and forecasted temperatures exhibit a typical seasonal cycle, with peaks in summer and troughs in winter.
- Forecasted temperatures align well with historical trends but show slightly less variability.

2) Humidity Trends
- Historical humidity shows moderate fluctuations, peaking in summer.
- Forecasted humidity is consistent but slightly lower on average.

3) Precipitation Trends
- Precipitation is sporadic, with historical data showing more pronounced spikes (ex. September rain events)
- Forecasted precipitation trends are smoother due to modeling constraints.

Statistical Analysis:
1) Correlation Analysis
- Temperature and humidity are weakly correlated, with stronger relationships between humidity and precipitation.
- Forecast data shows similar correlation patterns but with reduced variability.

2) Boxplots
- Clear seasonal and inter-year variability in temperature, humidity, and precipitation

3) Extreme Weather Events
- Analyzed outliers in temperature and precipitation to identify "extreme" weather days

4) Seasonal Decomposition
- Temperature decomposition revealed a clear seasonal trend with minor residual variability

## Visualizations
A variety of visualizations support the analysis and findings:

- Line graphs for monthly temperature, humidity, and precipitation trends.
- Correlation heatmaps to reveal relationships between variables.
- Boxplots highlighting interquartile ranges for historical vs. forecast data.
- Scatter plots for extreme weather analysis.
- Bar charts comparing seasonal averages.

## Ethics Statement

The data for this project was sourced ethically:

- Historical data was collected via WeatherAPI, which permits non-commercial use of its data.
- Forecast data was generated using NOAA's publicly available historical averages for Durham, NC.
- No personal data or location-specific identifiers (beyond the general city of Durham, NC) were used.

Biases and Limitations include:

- Forecast Accuracy: The forecasted data is simulated and based on averages. While it follows realistic trends, it does not account for sudden, extreme weather events (ex. hurricanes).
- Geographic Limitation: The dataset focuses exclusively on Durham, NC, and may not generalize to other locations.

Mitigations:
- Clear labeling distinguishes historical data from simulated data to ensure transparency.
- Potential inaccuracies in simulated data are noted, and users are encouraged to validate findings against real forecasts when possible.

## GitHub

https://github.com/dayeon3117/weather-dataset/tree/main

## Open Source License

This dataset is licensed under CC BY 4.0. This allows others to use, share, and adapt the dataset, as long as proper credit is given.
