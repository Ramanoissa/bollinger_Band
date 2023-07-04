import pandas as pd 
import numpy as np
from ta.volatility import BollingerBands


# Generate random data for demonstration
np.random.seed(42)
dates = pd.date_range(start='2023-01-01', periods=100)
close_prices = np.random.uniform(low=100, high=200, size=(100,))

# Create a DataFrame
df = pd.DataFrame({'date': dates, 'close': close_prices})

# Initialize the Bollinger Bands indicator
indicator_bb = BollingerBands(close=df['close'], window=20, window_dev=2)

# Compute the upper, middle, and lower bands
df['bb_upperband'] = indicator_bb.bollinger_hband()
df['bb_middleband'] = indicator_bb.bollinger_mavg()
df['bb_lowerband'] = indicator_bb.bollinger_lband()

# Print the DataFrame with Bollinger Bands
print(df)
