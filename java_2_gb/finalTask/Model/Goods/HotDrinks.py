from Model.Goods.Drinkables import Drinkables


class HotDrinks(Drinkables):
    def __init__(self, name, price, volume, temperature):
        super().__init__(name, price, volume)
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, new_temperature):
        self._temperature = new_temperature

    def __str__(self) -> str:
        return f"{super().__str__()}, температура: {self.temperature}"