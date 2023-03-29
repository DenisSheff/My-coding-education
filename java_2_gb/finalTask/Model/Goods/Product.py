class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @price.setter
    def price(self, new_price):
        self._price = new_price

    def __str__(self) -> str:
        return f"Название: {self.name}, цена: {self.price}"