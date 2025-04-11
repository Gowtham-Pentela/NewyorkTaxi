from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def clean_trip_data(input_path, output_path):
    spark = SparkSession.builder.appName("NYCTripETL").getOrCreate()

    df = spark.read.parquet(input_path)
    df_clean = df.filter(col("fare_amount") > 0).select(
        "tpep_pickup_datetime",
        "tpep_dropoff_datetime",
        "passenger_count",
        "trip_distance",
        "fare_amount"
    )
    df_clean.coalesce(1).write.csv(output_path, header=True, mode="overwrite")

    spark.stop()

if __name__ == "__main__":
    clean_trip_data("data/yellow_tripdata_2023-01.parquet", "data/clean_trip_data.csv")
