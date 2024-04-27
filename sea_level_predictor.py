import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    x_fit = list(range(min(df['Year']), 2051))
    y_fit = [slope * xi + intercept for xi in x_fit]
    plt.plot(x_fit, y_fit, color='red', label='Line of Best Fit')

    # Create second line of best fit
    df_2000_onward = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, _, _, _ = linregress(df_2000_onward['Year'], df_2000_onward['CSIRO Adjusted Sea Level'])
    x_fit_2000 = list(range(2000, 2051))
    y_fit_2000 = [slope_2000 * xi + intercept_2000 for xi in x_fit_2000]
    plt.plot(x_fit_2000, y_fit_2000, color='red', label='Line of Best Fit (2000 onward)')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()