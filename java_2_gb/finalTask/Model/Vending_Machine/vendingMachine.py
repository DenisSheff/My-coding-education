from Model.Goods.Product import Product


class VendingMachine:
    def __init__(self):
        list_products = list()
        self._list_products = list_products

    @property
    def list_products(self):
        return self._list_products

    @list_products.setter
    def list_products(self, new_list_products):
        self._list_products = new_list_products

    def add_at_list(self, product: Product):
        self._list_products.append(product)

    def get_product(self, name):
        for el in self.list_products:
            if el.name == name:
                return el
        else:
            return "Не найдено!"