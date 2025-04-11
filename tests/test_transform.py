import os
import pandas as pd
import pytest
from pipeline.transform import clean_trip_data
from pyspark.sql import SparkSession

@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder.master("local").appName("TestNYCTransform").getOrCreate()

def test_clean_trip_data(spark):
    input_path = "data/yellow_tripdata_2023-01.parquet"
    output_path = "data/test_output"

    clean_trip_data(input_path, output_path)

    csv_files = [os.path.join(output_path, f) for f in os.listdir(output_path) if f.endswith(".csv")]
    assert len(csv_files) > 0, "No CSV files created by Spark transformation"

    df = pd.concat([pd.read_csv(f) for f in csv_files])
    expected_columns = ["tpep_pickup_datetime", "tpep_dropoff_datetime", "passenger_count", "trip_distance", "fare_amount"]
    assert list(df.columns) == expected_columns, "Unexpected column names in transformed output"
    assert (df["fare_amount"] > 0).all(), "Filtered data contains invalid fare amounts"
