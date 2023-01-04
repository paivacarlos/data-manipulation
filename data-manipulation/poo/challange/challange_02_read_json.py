import json

with open("utilis_challange/data.json", "r") as file:
    text = file.read()
    data = json.loads(text)

print(data)

