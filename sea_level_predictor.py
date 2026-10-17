import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Import the data
    df = pd.read_csv('epa-sea-level.csv')

    # Create the scatter plot
    fig, ax = plt.subplots()

    ax.scatter(
        df['Year'],
        df['CSIRO Adjusted Sea Level']
    )

    # Calculate the line of best fit using all available data
    slope, intercept, r_value, p_value, std_err = linregress(
        df['Year'],
        df['CSIRO Adjusted Sea Level']
    )

    # Generate x-values from 1880 through 2050
    years = pd.Series(range(1880, 2051))

    # Plot the first line of best fit
    ax.plot(
        years,
        slope * years + intercept,
        color='red',
        label='Best fit: 1880–2050'
    )

    # Filter data from the year 2000 onward
    recent_df = df[df['Year'] >= 2000]

    # Calculate the line of best fit using recent data
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(
        recent_df['Year'],
        recent_df['CSIRO Adjusted Sea Level']
    )

    # Plot the second line of best fit through 2050
    recent_years = pd.Series(range(2000, 2051))

    ax.plot(
        recent_years,
        slope_recent * recent_years + intercept_recent,
        color='green',
        label='Best fit: 2000–2050'
    )

    # Set title and axis labels
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    # Save and return the plot
    fig.savefig('sea_level_plot.png')

    return fig