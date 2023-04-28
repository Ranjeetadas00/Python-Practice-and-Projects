from Menue import Menu, MenuItem
from Coffee_Maker import CoffeeMaker
from Money_Machine import MoneyMachine

coffee_machine = """

  ___      __  __           __  __         _    _          
  / __|___ / _|/ _|___ ___  |  \/  |__ _ __| |_ (_)_ _  ___ 
 | (__/ _ \  _|  _/ -_) -_) | |\/| / _` / _| ' \| | ' \/ -_)
  \___\___/_| |_| \___\___| |_|  |_\__,_\__|_||_|_|_||_\___|
                                                            

"""
print(coffee_machine)

my_moneyMachine = MoneyMachine()
my_coffee_Maker =CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        my_coffee_Maker.report()
        my_moneyMachine.report()
    else:
        drink = menu.find_drink(choice)
        
        if my_coffee_Maker.is_resource_sufficient(drink) and my_moneyMachine.make_payment(drink.cost):
          my_coffee_Maker.make_coffee(drink)
