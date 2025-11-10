import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    # Create first line of best fit
    slope, intercept = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_until_2050 = range(df['Year'].min(), 2051)
    plt.plot(years_until_2050, [slope * x + intercept for x in years_until_2050], color='blue')
    # Create second line of best fit
    slope_new, intercept_new = linregress(df[df['Year'] >= 2000]['Year'], df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])
    years_since_2000 = range(2000, 2051)
    plt.plot(years_since_2000, [slope_new * x + intercept_new for x in years_since_2000], color='black')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()