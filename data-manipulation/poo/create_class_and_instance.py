#criando uma classe no python
class People:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

#instanciando a classe
p1 = People('Carlos', 'Paiva')
print(type(p1))
print(p1.first_name, p1.last_name)

class Car:
    def __init__(self, model='car default value'):
        self.model = model

    def drive(self):
        print(f'{self.model} is driving!')

car_without_model = Car()
print(car_without_model.model)

car_with_model = Car('Volvo')
print(car_with_model.model)

#printing the method of the class
car_with_model.drive()