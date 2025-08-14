import os
import pandas as pd
import requests
import time

PATH = './uploads/'
uploaded = False;

def upload_data():
    response = requests.get("http://localhost:8443/has-uploaded")
    reponse_json = response.json()
    has_uploaded = reponse_json['hasUploaded']
    file_path = reponse_json['filePath']

    return has_uploaded, file_path

def get_columns(file_path):
    df = pd.read_csv(file_path)
    columns = df.columns.tolist()
    return columns

while not uploaded:
    uploaded, file_path = upload_data()

    if uploaded:
        columns = get_columns(file_path)
        requests.post("http://localhost:8443/column-selector", json={'columns': columns})

    time.sleep(1)