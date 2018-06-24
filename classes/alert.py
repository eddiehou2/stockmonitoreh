import stock

class Alert:
    stock = None
    alert_over = None
    alert_under = None

    @accepts(object, Stock, alert_over=int, alert_under=int)
    def __init__(self, stock, alert_over=None, alert_under=None):
        self.stock = stock
        self.alert_over = alert_over
        self.alert_under = alert_under
    
    def set_alerts(self,alert_over=None, alert_under=None):
        if alert_over is not None:
            self.alert_over = alert_over
        if alert_under is not None:
            self.alert_under = alert_under
        return True
    
    def get_alert_over(self):
        return self.alert_over

    def get_alert_undert(self):
        return self.alert_under

    def check_alerts(self):
        current_price = stock.get_current_price()
        if alert_over is not None and current_price[price] > alert_over:
            return "Over"
        elif alert_under is not None and current_price[price] < alert_under:
            return "Under"
        else:
            return False
