class retail_item:
    def __init__(self, item_desc, units, price):
        self.__item_desc = item_desc
        self.__units = units
        self.__price = price

    def __str__(self):
        return f"Description: {self.__item_desc}, Units in Inventory: {self.__units}, Price: ${self.__price:.2f}"
