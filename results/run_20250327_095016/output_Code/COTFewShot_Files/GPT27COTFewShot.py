class CurrencyConverter:
    def __init__(self):
        self.rates = {
            'USD': 1.0,
            'EUR': 0.85,
            'GBP': 0.72,
            'JPY': 110.15,
            'CAD': 1.23,
            'AUD': 1.34,
            'CNY': 6.40,
        }

    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.rates or to_currency not in self.rates:
            return None
        usd_amount = amount / self.rates[from_currency]
        return usd_amount * self.rates[to_currency]

    def get_supported_currencies(self):
        return list(self.rates.keys())

    def add_currency_rate(self, currency, rate):
        if currency in self.rates:
            return False
        self.rates[currency] = rate

    def update_currency_rate(self, currency, new_rate):
        if currency not in self.rates:
            return False
        self.rates[currency] = new_rate