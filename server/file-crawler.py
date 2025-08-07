import os

def loop():
    while True:
        if len(os.listdir('../uploads/')) != 0:
            return os.listdir('../uploads/')

print(loop())