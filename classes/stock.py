
class Stock:
    symbol = None
    company_name = None
    price_history = []
    current = {}
    edit_lock = False

    def __init__(self, symbol, company_name):
        self.symbol = symbol
        self.company_name = company_name

    def set_current_price(self, price, timestamp):
        try:
            if self.edit_lock == False:
                self.edit_lock = True
            else:
                return False

            if len(self.current) == 0 or self.current[timestamp] < timestamp:
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



    