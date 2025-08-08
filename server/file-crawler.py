import os
import pandas as pd
import requests

PATH = './uploads/'

def loop():
    while True:
        if len(os.listdir(PATH)) != 0:
            return os.listdir(PATH)

dir = loop()

df = pd.read_csv(PATH + str(dir[0]))

requests.post("http://localhost:8443/column-selector", json={'columns': df.columns.tolist()})