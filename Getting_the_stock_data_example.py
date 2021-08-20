import pandas as pd
import matplotlib.pyplot as plt

period = ['January', 'February', 'March',
          'April', 'May', 'June',
          'July', 'August', 'September',
          'October', 'November', 'December']

actual = [35, 35, 10,
          5, 8, 10,
          15, 20, 23,
          21, 22, 25]

forecast = [30, 31, 30,
            10, 12, 17,
            18, 27, 29,
            24, 23, 22]

data = pd.DataFrame({
    'period': period,
    'actual': actual,
    'forecast': forecast
    })

ax = data.plot.line(x='period')
ax.set_title('Forecast vs Actual', fontsize=16)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
plt.show()