from Model.Goods.BottleOfWater import BottleOfWater
from Model.Goods.HotDrinks import HotDrinks
from Model.Vending_Machine.vendingMachine import VendingMachine
from UI.UIConsole import UIConsole


class Service:

    def start(self):
        console = UIConsole()
        list_hot_drinks = [HotDrinks('Coffee', 200, 0.3, 80),
                           HotDrinks('Tea', 100, 0.4, 70),
                           HotDrinks('Milk', 300, 1.0, 65)]
        list_bottle_of_water = [BottleOfWater('Cola', 300, 0.5),
                                BottleOfWater('Sprite', 350, 0.45),
                                BottleOfWater('Fanta', 320, 0.43)]
        vending_machine1 = VendingMachine()
        vending_machine2 = VendingMachine()
        console.print_message('-----Лист горячих напитков добавлен в торговый автомат-----')
        vending_machine1.list_products = list_hot_drinks
        console.print_list_product(vending_machine1.list_products)
        console.print_message('-----Лист бутилированных напитков добавлен в торговый автомат-----')
        vending_machine2.list_products = list_bottle_of_water
        console.print_list_product(vending_machine2.list_products)
        console.print_message('-----В горяиче напитки добавлено какао-----')
        vending_machine1.add_at_list(HotDrinks('Какао', 250, 0.5, 70))
        console.print_list_product(vending_machine1.list_products)
        console.print_message('-----В бутилированные напитки добавлена минералка-----')
        vending_machine2.add_at_list(BottleOfWater('Минералка', 150, 0.5))
        console.print_list_product(vending_machine2.list_products)
        console.print_message('-----Получение Tea из торгового автомата-----')
        console.print_message(vending_machine1.get_product('Tea'))
        console.print_message('-----Получение Sprite из торгового автомата-----')
        console.print_message(vending_machine2.get_product('Sprite'))