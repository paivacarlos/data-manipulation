class Shop:
    def __init__(self):
        self._products = []

    def total(self):
        total = sum([p.price for p in self._products])
        return print(total)

    def insert_products(self, *products):
        self._products.extend(products)

    def product_list(self):
        for product in self._products:
            print(product.name, product.price)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

shop = Shop()
p1, p2, p3 = Product('tv', 789.99), Product('Monitor', 888.88), Product('Mouse', 11.99)

shop.insert_products(p1, p2, p3)
shop.product_list()
shop.total()