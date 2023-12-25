import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

link = "https://raw.githubusercontent.com/donostdy/Bike-Sharing-Data-Analysis/main/day.csv"
df = pd.read_csv(link)

def main():
    st.title('Bike Sharing Data Visualization')

    st.header('Visualization 1: Line Chart of Count Over Time')
    line_chart = sns.lineplot(x='Date', y='Count', data=df)
    st.pyplot(line_chart.figure)

    st.header('Visualization 2: Scatter Plot of Temperature vs. Count')
    scatter_plot = sns.scatterplot(x='Temperature', y='Count', data=df)
    st.pyplot(scatter_plot.figure)

    st.header('Visualization 3: Histogram of Humidity')
    histogram = sns.histplot(df['Humidity'], kde=True)
    st.pyplot(histogram.figure)

if __name__ == '__main__':
    main()