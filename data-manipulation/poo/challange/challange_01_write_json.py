import json

class Car:
    def __init__(self, model, mark):
        self.model = model
        self.mark = mark

car_01 = Car('208', 'pegeout')
#print(vars(car_01))
#print(json.dumps(car_01))

with open("utilis_challange/data.json", "w") as file:
    file.write(json.dumps(car_01.__dict__))