import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year'] # variable of the column Year
    y = df['CSIRO Adjusted Sea Level'] # variable of the column CSIRO Adjusted Sea Level
    plt.scatter(x, y) # create the plot and define x and y

    # Create first line of best fit
    A = linregress(x,y) # linregress calculates the slope and intercept for a "best fit" line (linear regression)
    xA = np.arange(x.min(), 2051) # Create an array of the years starting from the earliest until 2050 -> values of x that the line will be draw
    yA = A.intercept + A.slope * xA # Equation of the line y = m*x + b, where m = slope and b = intercept -> calculate the predicted sea level for each year
    plt.plot(xA, yA, color="red") # Plot the line

    # Create second line of best fit
    df_recent = df[df["Year"] >= 2000] # Filter of the dataset including only the years greater than or equal to 2000
    B = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"]) # linregress calculating slope and intercept with the filtered data
    xB = np.arange(2000, 2051) # Create an array of years from 2000 up to 2050
    yB = B.intercept + B.slope * xB # line equation (y = m*x + b) with diffrent slope and intercept
    plt.plot(xB, yB, color="green") # Plot the line

    # Add labels and title
    plt.xlabel("Year") # Add label of x
    plt.ylabel("Sea Level (inches)") # Add label of y
    plt.title("Rise in Sea Level") # Add title
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()