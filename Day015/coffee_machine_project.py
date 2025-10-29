# Make 3 flavours of coffee:
# espresso - 50ml water, 18g Coffee - 1.50$
# latte - 200 ml    Water, 24g Coffee, 150ml Milk - 2.50$
# cappuccino - 250ml Water , 24g Coffee, 100 Milk -  3.00$
# 300ml Water, 200ml milk at the begining
# Coin Operation:
#

# Program Requirements:
# 1. Print report
# 2. Check resources sufficent?
# 3. Process coins
# 4. Check Transaction is successful
# 5. Make Coffee

from resources import MENU, resources

cash_register = 0

penny = 0.01
nickel = 0.05
dime = 0.10
quarter = 0.25

# First prompt (shows prices)
menu_options = ", ".join([f"{name.title()} (${MENU[name]['cost']})" for name in MENU])


def prompt_with_prices():
    """Return input prompt string with menu options and prices."""
    return input(f"What would you like to order? ({menu_options})\n").lower()


order = prompt_with_prices()

if order == "off":
    end = True
elif order == "report":
    print(
        f"We have the following resources:\nWater: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g \nMoney: ${resources['money']}"
    )

# (menu_options and prompt_with_prices are defined above)


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * quarter
    total += int(input("How many dimes?: ")) * dime
    total += int(input("How many nickels?: ")) * nickel
    total += int(input("How many pennies?: ")) * penny
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global cash_register
        cash_register += drink_cost
        # Keep resources['money'] in sync with cash_register for reporting
        resources["money"] += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


while True:
    if order == "off":
        break
    if order == "report":
        print(
            f"We have the following resources:\nWater: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g \nMoney: ${resources['money']}"
        )
        order = prompt_with_prices()
        continue

    if order not in MENU:
        print("Sorry, that's not a valid option. Please choose from the menu.")
        order = prompt_with_prices()
        continue

    drink = MENU[order]
    if is_resource_sufficient(drink["ingredients"]):
        payment = process_coins()
        if is_transaction_successful(payment, drink["cost"]):
            make_coffee(order, drink["ingredients"])

    order = prompt_with_prices()
