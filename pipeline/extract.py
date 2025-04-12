import os
import requests

def download_trip_data(url, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    r = requests.get(url, stream=True)
    with open(output_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            f.write(chunk)
    print(f"Downloaded data from {url} to {output_path}")