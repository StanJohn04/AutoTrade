import yfinance as yf
import pandas as pd
import os

# We'll use yfinance to fetch daily data for a specific stock, Starting with SPY,
# over a defined period. This data will be the foundation for our backtest.

# 1. Define Parameters - after 2008 market crash through covid
ticker = 'SPY'
start_date = '2010-01-01'
end_date = '2023-12-31'
output_folder = 'data'
output_file = os.path.join(output_folder, f'{ticker}_data.csv')

# 2. Ensure the data directory exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 3. Fetch data using yfinance
print(f"Fetching data for {ticker} from {start_date} to {end_date}...")
stock_data = yf.download(ticker, start=start_date, end=end_date)

# 4. Save the data
stock_data.to_csv(output_file)

# 5. Confirmation
print(f"Data saved successfully to {output_file}")
print("\nFirst 5 rows of the data:")
print(stock_data.head())