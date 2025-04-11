import os
import pandas as pd
import sqlite3

def load_to_sqlite(csv_dir_path="data/clean_trip_data.csv", db_path="nyc_trips.db"):
    print(f"📁 Looking for CSV files in: {csv_dir_path}")
    
    if not os.path.exists(csv_dir_path):
        print(f"❌ ERROR: Directory '{csv_dir_path}' does not exist.")
        return

    csv_files = [
        os.path.join(csv_dir_path, f)
        for f in os.listdir(csv_dir_path)
        if f.endswith(".csv")
    ]

    if not csv_files:
        print(f"❌ ERROR: No .csv files found in '{csv_dir_path}'.")
        return

    try:
        print(f"📄 Found {len(csv_files)} CSV files. Loading data...")
        df = pd.concat([pd.read_csv(file) for file in csv_files])

        # Optional: rename columns
        df.columns = ["pickup_datetime", "dropoff_datetime", "passenger_count", "trip_distance", "fare_amount"]

        # Save to SQLite
        conn = sqlite3.connect(db_path)
        df.to_sql("trips", conn, if_exists="replace", index=False)
        conn.close()

        abs_path = os.path.abspath(db_path)
        print(f"✅ Loaded {len(df)} rows into database: {abs_path}")

    except Exception as e:
        print(f"❌ ERROR while loading data to SQLite: {e}")

if __name__ == "__main__":
    load_to_sqlite()
