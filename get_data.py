from binanceapi import client
import pandas as pd
import schedule
import time
from symbols import symbols


# Dictionary to store the price data
data = {}

# Function to retrieve price data
def get_prices():
    for symbol in symbols:
        klines = client.get_klines(symbol=symbol, interval=client.KLINE_INTERVAL_1DAY)
        if len(klines[0]) != 12:
            print(f"Unexpected number of columns for symbol {symbol}:")
            print(klines)
            continue

        df = pd.DataFrame(klines, columns=['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time',
                                           'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume',
                                           'taker_buy_quote_asset_volume', 'ignore'])
        df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
        df.set_index('open_time', inplace=True)

        # Store the data in the dictionary
        data[symbol] = df[['open', 'high', 'low', 'close', 'volume']]

    #print(data)  # Print the populated data dictionary

# Get the initial set of data
get_prices()



# Schedule updates daily at midnight
schedule.every().day.at('00:00').do(get_prices)

# Continuously run scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)