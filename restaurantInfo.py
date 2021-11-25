import pandas as pd


def readRestaurantInfo(csv):
    itemList = []  # creating empty lists to store menu items
    itemPrice = []
    itemCategory = []

    df = pd.read_csv(csv)
    itemColumn = df['ItemName']  # selecting specific columns
    for item in itemColumn:
        itemList.append(item)  # adding all values in the specified column to parallel lists
    priceColumn = df['Price']
    for item in priceColumn:
        itemPrice.append(item)
    categoryColumn = df['Category']
    for item in categoryColumn:
        itemCategory.append(item)
    return itemList, itemPrice, itemCategory
