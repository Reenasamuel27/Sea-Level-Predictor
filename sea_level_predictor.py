import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read the data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')

    # Create first line of best fit (1880 - 2050)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series(range(1880, 2051))
    y_pred = slope * x_pred + intercept
    plt.plot(x_pred, y_pred, 'r', label='Fit: All Data')

    # Create second line of best fit (2000 - most recent year)
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred_recent = pd.Series(range(2000, 2051))
    y_pred_recent = slope_recent * x_pred_recent + intercept_recent
    plt.plot(x_pred_recent, y_pred_recent, 'g', label='Fit: From 2000')

    # Customize plot
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save and return plot
    plt.savefig('sea_level_plot.png')
    return plt.gca()