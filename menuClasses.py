class menuItem:
    def __init__(self, itemName, itemPrice, itemCategory):
        self.itemName = itemName
        self.itemPrice = str(itemPrice)
        self.itemCategory = itemCategory

    def setItemName(self, name):
        self.itemName = name

    def setItemPrice(self, price):
        self.itemPrice = price

    def setItemCategory(self, category):
        self.itemCategory = category

    def getItemName(self):
        return self.itemName

    def getItemPrice(self):
        return self.itemPrice

    def getItemCategory(self):
        return self.itemCategory

    def __str__(self):
        itemString = self.itemName + "\n"
        itemString += "Price: " + self.itemPrice + "\n"
        itemString += "Category: " + self.itemCategory + "\n"
        return itemString


class customerOrder:
    def __init__(self, date, items, price):
        self.date = date
        self.items = items
        self.price = price

    def setDate(self, date):
        self.date = date

    def setItems(self, items):
        self.items = items

    def setPrice(self, price):
        self.price = price

    def getDate(self):
        return self.date

    def getItems(self):
        return self.items

    def getPrice(self):
        return self.items

    def __str__(self):


