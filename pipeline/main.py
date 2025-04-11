from extract import download_trip_data
from transform import clean_trip_data
from load import load_to_sqlite

def run_pipeline():
    url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet"
    raw_path = "data/yellow_tripdata_2023-01.parquet"
    clean_path = "data/clean_trip_data.csv"

    print("🚀 Starting data ingestion...")
    download_trip_data(url, raw_path)

    print("🧹 Running transformations...")
    clean_trip_data(raw_path, clean_path)

    print("📦 Loading to SQLite database...")
    load_to_sqlite(clean_path)

    print("✅ Pipeline completed successfully.")

if __name__ == "__main__":
    run_pipeline()
