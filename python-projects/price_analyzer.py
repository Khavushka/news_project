#  https://medium.com/@hannanmentor/10-python-projects-with-code-da82b5ac7304
# analyzing stock prices is crucial for investors and traders. in this project, you will create a stock price analyzer using Python and the Yahoo finance API. you will fetch historical stock data, calculate various financial indicators, and visualize the results using charts. this project will enhance your data analysis and visualization skills


import yfinance as yf
import matplotlib.pyplot as plt

def analyze_stock(symbol, start_date, end_date):
    # Fetch the stock data from Yahoo Finance
    stock_data = yf.download(symbol, start=start_date, end=end_date)

    # Calculate the daily returns
    stock_data['Daily Return'] = stock_data['Close'].pct_change()

    # Plot the closing price and daily returns
    plt.figure(figsize=(10, 5))
    plt.subplot(2, 1, 1)
    plt.plot(stock_data['Close'])
    plt.title('Stock Price')
    plt.ylabel('Price')

    plt.subplot(2, 1, 2)
    plt.plot(stock_data['Daily Return'])
    plt.title('Daily Returns')
    plt.ylabel('Return')

    plt.tight_layout()
    plt.show()

# Example usage
symbol = 'AAPL'  # Stock symbol (e.g., Apple Inc.)
start_date = '2022-01-01'  # Start date of the analysis
end_date = '2022-12-31'  # End date of the analysis

analyze_stock(symbol, start_date, end_date)