import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def main():
    st.title('Bike Sharing Data Visualization')

    # Visualization 1: Bar Plot for Weather Situation
    st.header('Visualization 1: Bar Plot for Weather Situation')
    weather_cnt_means = df.groupby('weathersit')['cnt'].mean().reset_index()
    weather_labels = {1: 'Clear, Few clouds', 2: 'Mist + Cloudy', 3: 'Light Snow, Light Rain', 4: 'Heavy Rain + Thunderstorm + Mist, Snow + Fog'}
    weather_cnt_means['weathersit_label'] = weather_cnt_means['weathersit'].map(weather_labels)

    custom_palette = {'Clear, Few clouds': 'red', 'Mist + Cloudy': 'grey', 'Light Snow, Light Rain': 'grey', 'Heavy Rain + Thunderstorm + Mist, Snow + Fog': 'grey'}

    plt.figure(figsize=(10, 6))
    sns.barplot(x='weathersit_label', y='cnt', data=weather_cnt_means, palette=custom_palette)
    plt.title('Average Count of Rental Bikes for Each Weather Situation')
    plt.xlabel('Weather Situation')
    plt.ylabel('Average Count of Rental Bikes')
    st.pyplot(plt.gcf())

    # Visualization 2: Bar Plot for Working Day vs. Weekend/Holiday
    st.header('Visualization 2: Bar Plot for Working Day vs. Weekend/Holiday')
    workingday_cnt_means = df.groupby('workingday')['cnt'].mean().reset_index()
    workingday_labels = {0: 'Weekend/Holiday', 1: 'Working Day'}
    workingday_cnt_means['workingday_label'] = workingday_cnt_means['workingday'].map(workingday_labels)

    custom_palette = {'Working Day': 'red', 'Weekend/Holiday': 'grey'}

    plt.figure(figsize=(8, 5))
    sns.barplot(x='workingday_label', y='cnt', data=workingday_cnt_means, palette=custom_palette)
    plt.title('Average Count of Rental Bikes for Working Day vs. Weekend/Holiday')
    plt.xlabel('Day Type')
    plt.ylabel('Average Count of Rental Bikes')
    st.pyplot(plt.gcf())

    # Visualization 3: Line Chart for Count Over the Year
    st.header('Visualization 3: Line Chart for Count Over the Year')
    df['dteday'] = pd.to_datetime(df['dteday'])
    yearly_cnt_sum = df.groupby(['yr', 'dteday'])['cnt'].sum().reset_index()
    year_labels = {0: 2011, 1: 2012}
    yearly_cnt_sum['year_label'] = yearly_cnt_sum['yr'].map(year_labels)

    custom_palette = {2011: 'grey', 2012: 'red'}

    plt.figure(figsize=(12, 6))
    sns.lineplot(x='dteday', y='cnt', hue='year_label', data=yearly_cnt_sum, palette=custom_palette)
    plt.title('Count of Rental Bikes Over the Year')
    plt.xlabel('Date')
    plt.ylabel('Count of Rental Bikes')
    plt.legend(title='Year')
    st.pyplot(plt.gcf())

if __name__ == '__main__':
    main()

st.pyplot(fig)

st.caption('Copyright © RD 2023')
