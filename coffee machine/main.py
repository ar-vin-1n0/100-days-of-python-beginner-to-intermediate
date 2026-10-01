from data import menu,machine

class MenuItem:
    def __init__(self,name,cost,ingredients):
        self.name = name
        self.ingredients = {}
        self.cost = 0

class Menu:
    def get_items(self,menu_items):
        print("---MENU---")
        for key, value in menu.items():
            print(f"{key} : {value.get("cost")} $")



def print_menu ():
    print("---MENU---")
    for key,value in menu.items():
        print(f"{key} : {value.get("cost")} $")

def check_machine(order):
    for item in order["ingredients"]:
        if machine[item] < order["ingredients"][item]:
            return False
    return True

def transaction(order_item,payment):
    if order_item["cost"] > payment:
        return False
    return True

def make_order(order_item):
    for i in order_item["ingredients"]:
        machine[i] -= order_item["ingredients"][i]
    return True


def main():
    on = True
    while on:
        print_menu()
        order = input("Enter your order  [off to turn off ]: ").lower()

        if order == "report":
            for key, value in machine.items():
                print(f"{key} : {value}")
            continue

        elif order == "off":
            on = False

        elif order not in menu.keys():
            print("Invalid order.order from the menu")
            continue

        order_item = menu[order]

        if not check_machine(order_item):
            print("Sorry, resources is not available.")
            continue

        payment = float(input("Enter your payment : "))
        if transaction(order_item,payment):
            print("You have successfully paid")
            print(f" u r {order} is being prepared")



        if not check_machine(order_item):
            print("Sorry, resources is not available.")
            continue

        if make_order(order_item):
            print(f"here is ur {order}")

main()