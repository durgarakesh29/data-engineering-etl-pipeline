import pandas as pd

def extract_data():
    df = pd.read_csv("data/raw_sales.csv")
    print("Data Extracted")
    return df