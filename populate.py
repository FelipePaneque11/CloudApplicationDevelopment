import csv
import requests
from pathlib import Path

def csvToJson():
    csv_file = Path(__file__).parent / "MOCK_DATA.csv"

    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print("Sending:", row)

            response = requests.post("http://127.0.0.1:8000/items/", json=row, timeout=10)

            print(response.status_code, response.text)

csvToJson()