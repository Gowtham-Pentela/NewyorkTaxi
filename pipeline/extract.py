import requests
url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet"
r = requests.get(url, stream=True)

with open("data/yellow_tripdata_2023-01.parquet", "wb") as f:
    for chunk in r.iter_content(chunk_size=1024*1024):
        f.write(chunk)
