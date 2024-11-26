# Weather in Durham, North Carolina
## Executive Summary

The goal of this project is to create a comprehensive dataset of weather trends that combines past and forecasted data for Durham, NC. The dataset is designed to help researchers, data scientists, and weather enthusiasts analyze patterns in temperature, precipitation, and humidity. It could be useful for applications in climate research, predictive modeling, or even urban planning.

Weather is one of the most critical factors influencing daily life, yet datasets that combine historical and forecasted weather data in an organized and ready-to-use format are hard to find. This dataset addresses that gap by bringing together historical weather records and future predictions into a unified resource.

## Description of Data

This dataset includes:

*Historical Data*: 365 days of historical weather data, including temperature (°C), precipitation (mm), and humidity (%).

*Forecast Data*: 365 days of weather forecasts with the same metrics.

The data is structured with columns for date, temperature_c, precipitation_mm, and humidity.

The historical data was sourced from public weather APIs, and the forecasted data was generated using reliable predictive models.

## Power Analysis

To make this dataset valuable, I needed enough data points to cover seasonal patterns and ensure year-round trends. Here's why the dataset size works:

365 days of past data ensures a full year of weather trends.
365 days of future data give a solid projection for predictive analysis while avoiding excessive speculative noise.

This size balances usability with the practicality of sourcing and storing data.

## Exploratory Data Analysis

Using visualizations, I explored key weather trends in the dataset. Here’s what I found:

*Temperature Trends*: Temperatures follow a typical seasonal pattern, peaking in the summer and dropping in the winter. Forecasted trends align with historical patterns.
*Precipitation Trends*: Precipitation spikes occur sporadically throughout the year, with higher concentrations during the spring and early fall.
*Humidity Patterns*: Humidity stays relatively consistent, with slightly higher values in the summer months.

Key visualizations:

- Line charts for temperature, precipitation, and humidity (both past and future).
- Correlation heatmap showing relationships between temperature, precipitation, and humidity.
- Stacked area charts illustrating monthly cumulative values.
- Daily heatmaps of temperature trends.

These visualizations help uncover patterns and trends that could inform climate models or other weather-related projects.

## Ethics Statement

The data for this project was sourced ethically:

- Historical data was collected using public APIs that permit non-commercial use.
- Forecast data was generated using tools that respect data-sharing agreements.
- No personal data or location-specific identifiers (beyond the general city of Durham, NC) were used.

Potential biases include:

- Over-reliance on forecast models, which can introduce inaccuracies.
- Limited geographical scope (only Durham, NC) reduces generalizability.

- Here’s everything laid out as if I were writing this directly for you as a college student. I’ll keep it casual and straightforward so it feels natural and approachable.
README for Weather Dataset
Executive Summary

The goal of this project is to create a comprehensive dataset of weather trends that combines past and forecasted data for Durham, NC. The dataset is designed to help researchers, data scientists, and weather enthusiasts analyze patterns in temperature, precipitation, and humidity. It could be useful for applications in climate research, predictive modeling, or even urban planning.

Weather is one of the most critical factors influencing daily life, yet datasets that combine historical and forecasted weather data in an organized and ready-to-use format are hard to find. This dataset addresses that gap by bringing together historical weather records and future predictions into a unified resource.
Description of Data

This dataset includes:

    Historical Data: 365 days of historical weather data, including temperature (°C), precipitation (mm), and humidity (%).
    Forecast Data: 300 days of weather forecasts with the same metrics.
    The data is structured with columns for date, temperature_c, precipitation_mm, and humidity.

The historical data was sourced from public weather APIs, and the forecasted data was generated using reliable predictive models.
Power Analysis

To make this dataset valuable, I needed enough data points to cover seasonal patterns and ensure year-round trends. Here's why the dataset size works:

    365 days of past data ensures a full year of weather trends.
    300 days of future data give a solid projection for predictive analysis while avoiding excessive speculative noise.
    This size balances usability with the practicality of sourcing and storing data.

Exploratory Data Analysis

Using visualizations, I explored key weather trends in the dataset. Here’s what I found:

    Temperature Trends: Temperatures follow a typical seasonal pattern, peaking in the summer and dropping in the winter. Forecasted trends align with historical patterns.
    Precipitation Trends: Precipitation spikes occur sporadically throughout the year, with higher concentrations during the spring and early fall.
    Humidity Patterns: Humidity stays relatively consistent, with slightly higher values in the summer months.

Key visualizations:

    Line charts for temperature, precipitation, and humidity (both past and future).
    Correlation heatmap showing relationships between temperature, precipitation, and humidity.
    Stacked area charts illustrating monthly cumulative values.
    Daily heatmaps of temperature trends.

These visualizations help uncover patterns and trends that could inform climate models or other weather-related projects.
Ethics Statement

The data for this project was sourced ethically:

    Historical data was collected using public APIs that permit non-commercial use.
    Forecast data was generated using tools that respect data-sharing agreements.
    No personal data or location-specific identifiers (beyond the general city of Durham, NC) were used.

Potential biases include:

    Over-reliance on forecast models, which can introduce inaccuracies.
    Limited geographical scope (only Durham, NC) reduces generalizability.

## Open Source License

This dataset is licensed under CC BY 4.0. This allows others to use, share, and adapt the dataset, as long as proper credit is given.
