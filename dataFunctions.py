import pandas as pd

class menuItem:
    def __init__(self, itemName, itemPrice, itemCategory):
        self.itemName = itemName
        self.itemPrice = itemPrice
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


