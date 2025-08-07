import os
import pandas as pd

PATH = '../uploads/'

def loop():
    while True:
        if len(os.listdir(PATH)) != 0:
            return os.listdir(PATH)

dir = loop()

df = pd.read_csv(PATH + str(dir[0]))

print(df.columns.tolist())