import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(15,10))
    plt.scatter(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]
    result = linregress(x, y)

    predt_x = pd.Series([i for i in range(1880,2051)])
    predt_y = result.intercept + result.slope * predt_x
    
    plt.plot(predt_x, predt_y , 'r', label='fitted line')
    plt.legend()

    # Create second line of best fit
    df_fit = df[df["Year"] >= 2000 ]

    x_fit = df_fit["Year"]
    y_fit = df_fit["CSIRO Adjusted Sea Level"]
    
    result2 = linregress(x_fit, y_fit)
    
    predt2_x = pd.Series([i for i in range(2000,2051)])
    predt2_y = result2.intercept + result2.slope * predt2_x
    
    
    plt.plot(predt2_x, predt2_y , 'g', label='fitted line')
    plt.legend()

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()