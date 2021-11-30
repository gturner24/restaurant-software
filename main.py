from menuClasses import menuItem, customerOrder
from restaurantInfo import readRestaurantInfo
import pandas as pd


if __name__ == '__main__':
    menuCSV = 'availableItems.csv'
    restaurantMenu = readRestaurantInfo(menuCSV)
    items = []

    for i in range(len(restaurantMenu[0])):  # finding the length of the menu
        item = (menuItem(restaurantMenu[0][i], restaurantMenu[1][i], restaurantMenu[2][i]))  # defining the items in the menu
        items.append(item)  # creating a list of all available items on the menu with their prices and item category
    for item in items:
        print(item)


