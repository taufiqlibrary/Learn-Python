import matplotlib.pyplot as plt
import pandas as pd

# Import the dataframe
eq = pd.read_csv('Ch03_Earthquake_database.csv')

# Describe the dataframe
#eq.describe()

# Convert years to dates
eq['year'] = pd.to_datetime(eq['Date']).dt.year

# Filter on earthquakes with magnitude of 7 or higher
eq = eq[eq['Magnitude'] >= 7]

# Compute a count of earthquakes per year
earthquakes_per_year = eq.groupby('year').count()

# Remove erroneous values for year
earthquakes_per_year = earthquakes_per_year.iloc[1:-2, 0]

# Make a plot of earthquakes per year
ax = earthquakes_per_year.plot()
ax.set_ylabel("Number of Earthquakes")
plt.show()