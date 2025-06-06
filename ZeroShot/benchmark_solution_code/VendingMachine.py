'''
# This is a class to simulate a vending machine, including adding products, inserting coins, purchasing products, viewing balance, replenishing product inventory, and displaying product information.

class VendingMachine:
    def __init__(self):
        """
        Initializes the vending machine's inventory and balance.
        """
        self.inventory = {}
        self.balance = 0

    def add_item(self, item_name, price, quantity):
        """
        Adds a product to the vending machine's inventory.
        :return: None

        """

    def insert_coin(self, amount):
        """
        Inserts coins into the vending machine.
        :return: The balance of the vending machine after the coins are inserted, float.
        
        """

    def purchase_item(self, item_name):
        """
        Purchases a product from the vending machine and returns the balance after the purchase and display purchase unsuccessful if the product is out of stock.
        :return: If successful, returns the balance of the vending machine after the product is purchased, float,otherwise,returns False.

        """

    def restock_item(self, item_name, quantity):
        """
        Replenishes the inventory of a product already in the vending machine.
        :return: If the product is already in the vending machine, returns True, otherwise, returns False.
        """

    def display_items(self):
        """
        Displays the products in the vending machine.
        :return: If the vending machine is empty, returns False, otherwise, returns a list of the products in the vending machine, str.

        """
'''

class VendingMachine:
    def __init__(self):
        self.inventory = {}
        self.balance = 0

    def add_item(self, item_name, price, quantity):
        if not self.restock_item(item_name, quantity):
            self.inventory[item_name] = {'price': price, 'quantity': quantity}

    def insert_coin(self, amount):
        self.balance += amount
        return self.balance

    def purchase_item(self, item_name):
        if item_name in self.inventory:
            item = self.inventory[item_name]
            if item['quantity'] > 0 and self.balance >= item['price']:
                self.balance -= item['price']
                item['quantity'] -= 1
                return self.balance
            else:
                return False
        else:
            return False

    def restock_item(self, item_name, quantity):
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] += quantity
            return True
        else:
            return False

    def display_items(self):
        if not self.inventory:
            return False
        else:
            items = []
            for item_name, item_info in self.inventory.items():
                items.append(f"{item_name} - ${item_info['price']} [{item_info['quantity']}]")
            return "\n".join(items)