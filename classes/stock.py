class Stock:
    symbol = None
    company_name = None
    price_history = []
    current = {}
    edit_lock = False

    def __init__(self, symbol, company_name):
        self.symbol = symbol
        self.company_name = company_name

    def __str__(self):
        message = "Symbol: " + self.symbol + "\n" + \
            "Company Name: " + self.company_name + "\n" + \
            "Current Price: " + str(self.current.get("price") or "None") + "\n"
        return message

    def set_current_price(self, price, timestamp):
        try:
            if self.edit_lock == False:
                self.edit_lock = True
            else:
                return False

            if len(self.current) == 0 or self.current['timestamp'] < timestamp:
                self.current = {
                    'price': price,
                    'timestamp': timestamp
                }
                self.price_history.append(self.current)
                return True
            else:
                return False
        except Exception as e:
            print("Error: " + str(e))
        finally:
            self.edit_lock = False
    
    def get_current_price(self):
        return self.current

    def get_symbol(self):
        return self.symbol

    def get_company_name(self):
        return self.company_name

    def get_price_history(self):
        return self.price_history

    def get_price_history_without_timestamp(self):
        return map(lambda x: x['price'], self.price_history)



    