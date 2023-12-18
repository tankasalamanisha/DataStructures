# TODO : Add a dictionary with ingredients, quantity and prices. - Done
# TODO : Add a dictionary for resources and a variable for profit made. - Done
# TODO: 1. Add function to take instructions from user and save it. - Done
# TODO: 2. Add function to check the availability of resources - Done
# TODO: 3. Add function to process the coins and check if the cost matches - Done
# TODO: 4. Add function to process the cofee - Done
menu={
    "espresso": {
        "ingredients":{
            "water": 50,
            "coffee": 18
        },
        "price": 1.5
    },
    "latte":{
        "ingredients":{
            "water": 200,
            "coffee": 150,
            "milk": 24,
        },
        "price": 2.5
    },
    "cappucino":{
        "ingredients":{
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "price": 3.0
    }
}

profit = {
    "amount": 0.0
}

resources={
    "milk":300,
    "water":200,
    "coffee": 100
}

def get_beverage(menu:dict)->str:
    """Function to take in the beverage type entered by user.
    Args:
    ----------------------------
    menu: <dictionary>: menu set by the operator.
    Returns:
    ----------------------------
    preferred_beverage: <str>: beverage selected by the user.
    """
    print(f"Beverage options:\n{menu.keys()}\n")
    preferred_beverage = input("Enter the beverage you'd like to enjoy:")
    return preferred_beverage

def check_availability(preferred_beverage:str)->bool:
    """Function to check the availability of ingredients in the resource.
    """
    flag = True
    if preferred_beverage in menu.keys():
        ingredients = menu[preferred_beverage]["ingredients"]
        for ingredient in ingredients.keys():
            if ingredients[ingredient] > resources[ingredient]:
                print(f"Oh oh! no sufficient {ingredient}.")
                print(f"{ingredient} available: {resources[ingredient]}.\n {ingredient} needed: {ingredients[ingredient]}")
                flag =False
    
    return flag
            

def process_coins(coins:float, resource_flag:bool, price:float)->bool:
    """Function to process the coins after fulfilling the resource requirements and to add to the profit made.
    """

    flag = False
    if resource_flag:
        if coins >= price:
            flag= True
            profit["amount"] += coins

    return flag

def process_beverage(coins_flag:bool, preferred_beverage:str)->bool:
    """Function to process beverage and make modifications to resources.
    """
    beverage_processed=False
    if coins_flag:
        print("Processing your request....")
        for _ingrdt, _qty in menu[preferred_beverage]["ingredients"].items():
            orig_qty = resources[_ingrdt]
            resources[_ingrdt] = orig_qty - _qty
        beverage_processed = True
    return beverage_processed

if __name__ == "__main__":
    available_beverages = list(menu.keys())
    print("Menu:")
    for i in range(len(available_beverages)):
        print(f"{i+1}.{available_beverages[i].upper()}")
    overall_flag = True
    while overall_flag:
        preferred_beverage = input(f"What beverage do you want to have?")
        print(f"Your preferred beverage is: {preferred_beverage.upper()}")
        

        print("Checking resource availability...")
        resource_avail_flag = check_availability(preferred_beverage)
        if resource_avail_flag:
            print(f"Resources are available for {preferred_beverage.upper()}.\n Price of {preferred_beverage.upper()}:{menu[preferred_beverage]['price']} $")
            coins_entered = float(input("Please enter the coins:"))
            coins_check = process_coins(coins=coins_entered, resource_flag= resource_avail_flag, price= menu[preferred_beverage]["price"])

            if coins_check:
                whether_processed = process_beverage(coins_flag=coins_check, preferred_beverage=preferred_beverage)
                if whether_processed:
                    print(f"Enjoy your {preferred_beverage.upper()} !")
                    print("Available Resources:")
                    for _item, avail in resources.items():
                        print(f"{_item}:{avail}")
                    another_beverage = input("Do you want another beverage?")
                    if another_beverage.lower() == "no":
                        overall_flag = False
                else:
                    print(f"Oh Oh! No sufficient resources")
                    overall_flag=False
            else:
                print(f"The coins entered: {coins_entered}; Need {menu[preferred_beverage]['price']- coins_entered} more coins.Please try again!")
                overall_flag=False
        else:
            print("The available ingredients aren't sufficient. Please ask the administrator to refil the ingredients and try again!")
            overall_flag=False