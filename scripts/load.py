import sqlite3

def load_data(df):
    # Create database connection
    conn = sqlite3.connect("database/sales.db")

    # Load data into table
    df.to_sql("sales", conn, if_exists="replace", index=False)

    # Close connection
    conn.close()

    print("Data Loaded into Database")