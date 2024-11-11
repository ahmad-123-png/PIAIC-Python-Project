"""
from product import ProductManager


class Inventory:
    def __init__(self):
        self.product_manager = ProductManager()
        self.low_stock_threshold = 5

    def check_stock(self):
        for product in self.product_manager.products.values():
            if product.stock_quantity <= self.low_stock_threshold:
                print(f"Low stock warning for {product.name}!")
"""

from product import ProductManager

class Inventory:
    def __init__(self):
        self.product_manager = ProductManager()

    def view_all_products(self):
        # Fetch all products from the product manager
        return self.product_manager.get_all_products()

    def add_product(self, name, category, price, stock):
        # Add a product using the product manager
        self.product_manager.add_product(name, category, price, stock)
