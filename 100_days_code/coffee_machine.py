# TODO : Add a dictionary with ingredients, quantity and prices.
# TODO : Add a dictionary for resources and a variable for profit made.
# TODO: 1. Add function to take instructions from user and save it.
# TODO: 2. Add function to check the availability of resources.
# TODO: 3. Add function to process the coins and check if the cost matches.
# TODO: 4. Add function to process the cofee.
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

profit = 0

resources={
    "milk":300,
    "water":200,
    "coffee": 100
}