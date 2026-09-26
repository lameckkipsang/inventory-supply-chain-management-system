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