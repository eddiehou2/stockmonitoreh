import requests

BASE_URL = "https://www.alphavantage.co/query"
INTRADAY = "TIME_SERIES_INTRADAY"
DAILY_ADJUSTED = "TIME_SERIES_DAILY_ADJUSTED"
BATCH_QUOTES = "BATCH_STOCK_QUOTES"
API_KEY = None

def get_intraday_stock_price(symbol, interval=1, outputsize="full"):
    """
        Gets the intraday stock price for one symbol for either 100 last quotes or full history
        * Granularity: 1min, 5min, 15min, 30min, or 60min
        * Returns: open, close, low, high, volume, timestamp
    """
    results = []

    # Making sure values are correct
    if interval not in [1, 5, 15, 30, 60]:
        interval = 1
    if outputsize not in ["full", "compact"]:
        outputsize = "compact"

    # Key to get the time series dictionary
    TIME_SERIES_KEY = "Time Series (" + str(interval) + "min)"

    # Sending request to get intraday data
    params = {
        'function': INTRADAY,
        'symbol': symbol,
        'interval': str(interval) + 'min',
        'outputsize': outputsize,
        'apikey': API_KEY
    }
    r = requests.get(BASE_URL, params=params)

    # Formatting results from dictionary to array going from earliest to latest
    price_dict = r.json().get(TIME_SERIES_KEY)
    sorted_timestamp = sorted(price_dict)
    for timestamp in sorted_timestamp:
        current_price = {}
        current_price['open'] = price_dict[timestamp].get('1. open')
        current_price['high'] = price_dict[timestamp].get('2. high')
        current_price['low'] = price_dict[timestamp].get('3. low')
        current_price['close'] = price_dict[timestamp].get('4. close')
        current_price['volume'] = price_dict[timestamp].get('5. volume')
        current_price['timestamp'] = timestamp
        results.append(current_price)

    return results

def get_daily_stock_price(symbol, outputsize="full"):
    """
        Gets the daily stock price for one symbol for either 100 last quotes or 20 years
        * Granularity: 1day
        * Returns: open, close, low, high, volume, timestamp
    """
    results = []

    # Making sure values are correct
    if outputsize not in ["full", "compact"]:
        outputsize = "compact"

    # Key to get the time series dictionary
    TIME_SERIES_KEY = "Time Series (Daily)"

    # Sending request to get intraday data
    params = {
        'function': DAILY_ADJUSTED,
        'symbol': symbol,
        'outputsize': outputsize,
        'apikey': API_KEY
    }
    r = requests.get(BASE_URL, params=params)

    # Formatting results from dictionary to array going from earliest to latest
    price_dict = r.json().get(TIME_SERIES_KEY)
    sorted_timestamp = sorted(price_dict)
    for timestamp in sorted_timestamp:
        current_price = {}
        current_price['open'] = price_dict[timestamp].get('1. open')
        current_price['high'] = price_dict[timestamp].get('2. high')
        current_price['low'] = price_dict[timestamp].get('3. low')
        current_price['close'] = price_dict[timestamp].get('4. close')
        current_price['volume'] = price_dict[timestamp].get('5. volume')
        current_price['timestamp'] = timestamp
        results.append(current_price)

    return results

def current_stock_prices_simple(symbols):
    """
        Gets the real-time stock price for multiple symbols
        * Granularity: 1 sec
        * Returns: price, timestamp
    """
    results = {}

    # Check for correct params
    if type(symbols) is not list or len(symbols) < 1:
        return None
    
    # Sending request to get current quote data
    params = {
        'function': BATCH_QUOTES,
        'symbols': ','.join(symbols),
        'apikey': API_KEY
    }
    r = requests.get(BASE_URL, params=params)

    # Formatting results to use symbol as key
    quotes_array = r.json().get('Stock Quotes')
    for quote in quotes_array:
        results[quote['1. symbol']] = {
                'price': quote['2. price'],
                'timestamp': quote['4. timestamp']
            }
    
    return results

def load_api_key():
    global API_KEY
    if API_KEY:
        return
    
    api_key_file = open('../configs/api_key', 'r')
    API_KEY = api_key_file.read()