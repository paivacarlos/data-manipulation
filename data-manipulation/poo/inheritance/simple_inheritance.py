class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def talk_name_and_class(self):
        print(self.first_name, self.last_name, self.__class__.__name__)

class Client(Person):
    ...

class Student(Person):
    ...

c1 = Client('Carlos', 'Paiva')
c1.talk_name_and_class()

s1 = Student('Adolfo', 'De Mello')
s1.talk_name_and_class()

help(Student)