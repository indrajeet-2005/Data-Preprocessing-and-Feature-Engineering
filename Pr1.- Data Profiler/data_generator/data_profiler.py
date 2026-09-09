import pandas as pd
import sqlite3

def load_csv(path):
    return pd.read_csv(path)

def load_json(path):
    return pd.read_json(path)

def load_sqlite(path, table="customers"):
    conn = sqlite3.connect(path)
    try:
        return pd.read_sql_query(f"SELECT * FROM {table}", conn)
    finally:
        conn.close()

def clean_customer_data(df):
    data = df.copy()
    if "Age" in data.columns:
        data["Age"] = data["Age"].fillna(data["Age"].median())
    if "Income" in data.columns:
        data["Income"] = data["Income"].fillna(data["Income"].median())
    if "Gender" in data.columns:
        data["Gender"] = data["Gender"].fillna(data["Gender"].mode()[0])
    data = data.drop_duplicates()
    return data

if __name__ == "__main__":
    print("Data Profiler helper module")
