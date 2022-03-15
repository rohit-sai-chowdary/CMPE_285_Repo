# CMPE 285 - HW2 - Rohit_Sai
# Necessary Imports
import yfinance as yf
from datetime import datetime

while True:
    # Accept a stock symbol from the user
    print("Please enter a symbol: ")
    sym = input()

    # To break out of the loop
    if sym == 'exit':
        break

    # Exception handling incase of any problems with fetching the data
    try:
        stock = yf.Ticker(sym)
    except ConnectionError as e:
        print("Connection Error", e)
        break

    # Current date and time at the time of checking
    now = datetime.now()
    # Format the string
    current_time = now.strftime("%d %b %Y  %H:%M:%S")
    print("Current Time = {} \n".format(current_time))

    if not stock.info['regularMarketPrice']:
        print("Invalid Symbol. Please type a valid symbol to get the price.\n")
        break
    else:
        print(stock.info['longName'])

    curr_price = stock.info['currentPrice']
    prev_day_price = stock.info['previousClose']
    price_diff = curr_price - prev_day_price
    percent_diff = (abs(price_diff) / prev_day_price) * 100

    if price_diff > 0:
        print("Current Stock Price: {} USD".format(curr_price))
        print("Price Difference: +{} USD".format(round(price_diff, 2)))
        print("Percentage Difference: +{}%".format(round(percent_diff, 2)))
    else:
        print("Current Stock Price: {} USD".format(curr_price))
        print("Price Difference: -{} USD".format(round(abs(price_diff), 2)))
        print("Percentage Difference: -{}% \n".format(round(percent_diff, 2)))