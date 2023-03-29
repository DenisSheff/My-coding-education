from Model.Goods.Drinkables import Drinkables


class BottleOfWater(Drinkables):
    def __init__(self, name, price, volume):
        super().__init__(name, price, volume)

    def __str__(self):
        return super().__str__()