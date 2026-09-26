from abc import ABC, abstractmethod
class Product:
    def __init__(self, product_id, product_name, category_name, cost_price, retail_price, stock_quantity, minimum_stock_threshold, supplier_id):
        self.product_id = product_id
        self.product_name = product_name
        self.category_name = category_name
        self._cost_price = float(cost_price)
        self._retail_price = float(retail_price)
        self._stock_quantity = int(stock_quantity)
        self.minimum_stock_threshold = int(minimum_stock_threshold)
        self.supplier_id = supplier_id

    @property
    def stock_quantity(self):
        return self._stock_quantity

    @stock_quantity.setter
    def stock_quantity(self, new_quantity):
        if new_quantity < 0:
            raise ValueError("Stock quantity cannot be negative!")
        self._stock_quantity = new_quantity

    @property
    def retail_price(self):
        return self._retail_price

    @retail_price.setter
    def retail_price(self, new_price):
        if new_price < 0:
            raise ValueError("Retail price cannot be negative!")
        self._retail_price = new_price

    def to_dictionary(self):
        return {
            "product_id": self.product_id,
            "product_name": self.product_name,
            "category_name": self.category_name,
            "cost_price": self._cost_price,
            "retail_price": self._retail_price,
            "stock_quantity": self._stock_quantity,
            "minimum_stock_threshold": self.minimum_stock_threshold,
            "supplier_id": self.supplier_id
        }

class Supplier(ABC):
    def __init__(self, supplier_id, company_name, contact_email, lead_time_days):
        self.supplier_id = supplier_id
        self.company_name = company_name
        self.contact_email = contact_email
        self.lead_time_days = int(lead_time_days)

    @abstractmethod
    def get_delivery_terms(self):
        pass