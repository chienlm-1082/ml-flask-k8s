import requests
import time

start = time.time()
resp = requests.post(
    "http://localhost:5000/predict",
    files={"file": open("/home/yoona/Pictures/072.jpeg", "rb")},
)
print(resp.json())
print(round(time.time() - start, 3))
