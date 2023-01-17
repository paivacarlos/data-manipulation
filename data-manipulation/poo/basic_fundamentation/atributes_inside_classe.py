class People:
    current_year = 2023

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_year_was_born(self):
        return People.current_year - self.age

people_01 = People('Carlos', 34)
people_02 = People('Pati', 30)

print(people_01.get_year_was_born())
print(people_02.get_year_was_born())
print(people_01.__dict__)
print(vars(people_02))

data = {'name': 'leo', 'age': 26}
people_03 = People(**data)
print(vars(people_03))