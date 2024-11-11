"""
class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def update_stock(self, quantity):
        self.stock_quantity += quantity

class ProductManager:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product

    def edit_product(self, product_id, **kwargs):
        if product_id in self.products:
            product = self.products[product_id]
            for key, value in kwargs.items():
                setattr(product, key, value)
        else:
            raise ValueError("Product not found")

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
        else:
            raise ValueError("Product not found")
"""

class Product:
    def __init__(self, product_id, name, category, price, stock):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Category: {self.category}, Price: {self.price}, Stock: {self.stock}"

class ProductManager:
    def __init__(self):
        self.products = {}
        self.next_id = 1

    def add_product(self, name, category, price, stock):
        product = Product(self.next_id, name, category, price, stock)
        self.products[self.next_id] = product
        self.next_id += 1

    def get_all_products(self):
        return list(self.products.values())
