import os
import pandas as pd
import requests

PATH = './uploads/'

def loop():
    while True:
        if len(os.listdir(PATH)) != 0:
            return os.listdir(PATH)

while True:
    dir = loop()

    df = pd.read_csv(PATH + str(dir[0]))
    try:
        if df.columns.tolist() != odf.columns.tolist():
            requests.post("https://trainable.studio:8443/column-selector", json={'columns': df.columns.tolist()})
    except:
        requests.post("https://trainable.studio:8443/column-selector", json={'columns': df.columns.tolist()})
    odf = df