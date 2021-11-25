import pandas as pd

def readItems(csv):
    df = pd.read_csv(csv)
    print(df)

readItems('availableItems.csv')