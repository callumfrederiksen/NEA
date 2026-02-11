import pandas as pd
import requests
import time

PATH = './src/uploads/'
uploaded = False;

def upload_data():
    # Calls the API to see if uploaded
    response = requests.get("http://localhost:8443/has-uploaded")
    response_json = response.json()
    has_uploaded = response_json['hasUploaded']
    file_path = response_json['filePath']

    return has_uploaded, file_path

def get_columns(file_path):
    # Gets the columns from the CSV
    df = pd.read_csv(file_path)
    columns = df.columns.tolist()
    return columns

while not uploaded:
    # Continually checks until data has been uploaded
    uploaded, file_path = upload_data()

    if uploaded:
        columns = get_columns(file_path)
        requests.post("http://localhost:8443/column-selector", json={'columns': columns})

    time.sleep(1)