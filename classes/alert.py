from util.decorators import accepts
from classes.stock import Stock

class Alert:
    stock = None
    alert_over = None
    alert_under = None

    @accepts(object, object, int, int)
    def __init__(self, stock, alert_over=None, alert_under=None):
        self.stock = stock
        self.alert_over = alert_over
        self.alert_under = alert_under

    def __str__(self):
        message = "Stock: " + self.stock.get_symbol() + "\n" + \
            "Alert Over: " + str(self.alert_over or "None") + "\n" + \
            "Alert Under: " + str(self.alert_under or "None") + "\n"
        return message
    
    def set_alerts(self,alert_over=None, alert_under=None):
        if alert_over is not None:
            self.alert_over = alert_over
        if alert_under is not None:
            self.alert_under = alert_under
        return True
    
    def get_alert_over(self):
        return self.alert_over

    def get_alert_under(self):
        return self.alert_under

    def check_alerts(self):
        current_price = self.stock.get_current_price()
        if current_price.get("price") is None:
            return False

        if self.alert_over is not None and current_price['price'] > self.alert_over:
            return "Over"
        elif self.alert_under is not None and current_price['price'] < self.alert_under:
            return "Under"
        else:
            return False
