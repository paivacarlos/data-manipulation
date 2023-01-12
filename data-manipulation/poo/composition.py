class Client:
    def __init__(self, name):
        self.name = name
        self.adress = []

    def insert_address(self, street, number):
        self.adress.append(Adress(street, number))

    def adress_list(self):
        for adress in self.adress:
            print(adress.street, adress.number)

class Adress:
    def __init__(self, street, number):
        self.street = street
        self.number = number

c1 = Client('Paiva')
c1.insert_address('Pio XII', 343)
c1.adress_list()