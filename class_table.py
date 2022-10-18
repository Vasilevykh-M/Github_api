class Supply():
    def __init__(self, a, b, c, d, e, f):
        self.id_country = a
        self.id_city = b
        self.id_store = c
        self.id_product = d
        self.shipping_date = e
        self.count_product = f

class Country:
    def __init__(self, a, b):
        self.id_country = a
        self.country = b

class City:
    def __init__(self, a, b):
        self.id_city = a
        self.city = b

class Store:
    def __init__(self, a, b):
        self.id_store = a
        self.store = b

class Product_group:
    def __init__(self, a, b):
        self.id_product_group = a
        self.product_group = b

class Product:
    def __init__(self, a, b, c, d):
        self.id_product = a
        self.product = b
        self.price = c
        self.id_product_group = d