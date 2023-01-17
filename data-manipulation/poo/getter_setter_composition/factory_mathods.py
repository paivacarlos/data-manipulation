
class People:
    year = 2023

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def person_say_hi(cls):
        print("Hi!")

    @classmethod
    def person_is_50_years(cls, name):
        return cls(name, 50)


person_01 = People('Carlos', 34)
print(person_01.name)
print(person_01.age)
person_01.person_say_hi()

person_02 = People.person_is_50_years('Paiva')
print(person_02.name, person_02.age)


