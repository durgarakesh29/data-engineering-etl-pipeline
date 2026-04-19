import pandas as pd

def transform_data(df):
    # Remove duplicate rows
    df = df.drop_duplicates()

    # Fill missing values with 0
    df = df.fillna(0)

    # Convert Order Date to datetime (if exists)
    if 'Order Date' in df.columns:
        df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
        
    # Create summary (Sales by Category)
    if 'Category' in df.columns and 'Sales' in df.columns:
        summary = df.groupby("Category")["Sales"].sum().reset_index()
        summary.to_csv("output/sales_summary.csv", index=False)

        print("Summary file created")

    print("Data Transformed")
    return df
