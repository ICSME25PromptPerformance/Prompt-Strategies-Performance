class CurrencyConverter:
    """
    This is a class for currency conversion, which supports to convert amounts between different currencies, retrieve supported currencies, add new currency rates, and update existing currency rates.
    """

    def __init__(self):
        """
        Initialize the exchange rate of the US dollar against various currencies
        """
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
        """
        Convert the value of a given currency to another currency type
        :param amount: float, The value of a given currency
        :param from_currency: string, source currency type
        :param to_currency: string, target currency type
        :return: float, value converted to another currency type
        """
        # Check if both currencies are supported
        if from_currency not in self.rates or to_currency not in self.rates:
            raise ValueError("Unsupported currency type")
        
        # Convert the amount to USD first, then to the target currency
        amount_in_usd = amount / self.rates[from_currency]
        converted_amount = amount_in_usd * self.rates[to_currency]
        
        return converted_amount

    def get_supported_currencies(self):
        """
        Returns a list of supported currency types
        :return: list, All supported currency types
        """
        return list(self.rates.keys())

    def add_currency_rate(self, currency, rate):
        """
        Add a new supported currency type, return False if the currency type is already in the support list
        :param currency: string, currency type to be added
        :param rate: float, exchange rate for this type of currency
        :return: If successful, returns None; if unsuccessful, returns False
        """
        # Check if the currency already exists
        if currency in self.rates:
            return False
        
        # Add the new currency and its rate
        self.rates[currency] = rate

    def update_currency_rate(self, currency, new_rate):
        """
        Update the exchange rate for a certain currency
        :param currency: string
        :param new_rate: float
        :return: If successful, returns None; if unsuccessful, returns False
        """
        # Check if the currency exists
        if currency not in self.rates:
            return False
        
        # Update the currency rate
        self.rates[currency] = new_rate