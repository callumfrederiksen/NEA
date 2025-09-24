import requests

res = requests.get("http://localhost:8443/return-hyperparameters")
print(res.json())