# import libraries
import pandas
import math


def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter 'Yes' or 'No'")


def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def not_blank(question, error):
    while True:
        response = input(question)

        if response == "":
            print(f"{error} Sorry but this cannot be blank. Please retry")

        elif response == " ":
            print(f"{error}. Sorry but this cannot be blank. PLease retry")

        else:
            return response


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# test functions
def name_question(question, error):
    while True:
        response = input(question)

        if response == "":
            print(f"{error} Sorry but this cannot be blank. Please retry")

        elif response == " ":
            print(f"{error}. Sorry but this cannot be blank. PLease retry")

        else:
            return response



def need_question(question, error, num_type):
    pass


def have_question(question, error, num_type):
    pass


def cost_question(question, error, num_type):
    pass


# trying out
def kilograms(question, error):
    response = input("How much of the ingredient do you need?")
    if response >10:
        yes_no("Did you mean {response}kg? Y / N")


# have nothing in them
def grams(question, error):
    pass


def cups(question, error):
    pass


def individual(question, error):
    pass


# set up blank dictionaries
ingredient_list = []
amount_needed = []
amount_have = []
ingredient_cost = []

ingredient_dict = {
    "ingredient": ingredient_list,
    "need": amount_needed,
    "have": amount_have,
    "cost": ingredient_cost
}

# test main code area
# loop to get ingredient name, amount needed, amount have and ingredient cost
item_name = " "
while item_name.lower() != "xxx":
    print()


# Notes
# could use an Identify list thingy
# Could just make a function that asked if it was grams or kg

while True:
    # get name, quantity and item
    # get ingredients name, amount needed and have and ingredient cost
    ingredient_name = not_blank("Ingredient name: ", "").lower()

    if ingredient_name.lower() == "xxx":
        break

    response = input,num_check("Amount needed: ","Please enter integer more than 0", float).lower()
    # Checks if the last letter is kg
     if response[-2:] == "kg":
         needed_weight = "kilograms"
         # Get amount
         amount = response[:-2]

        # Check if last character is g
     elif response[-2:] == " g":
         needed_weight = "grams"
         # Get amount
         amount = response[:-2]

    else:
        # set response to amount for now
        profit_type = "unknown"
        amount = response


    if response == "unknown" and amount <= 10:
        weight_kilo = yes_no(f"Do you mean {amount:.2f}kg? y / n ")

        # set profit type
        if weight_kilo == "yes":
            profit_type = "kilograms"
        else:
            profit_type = "g"

    elif response == "unknown" and amount > 10:
        percent_type = yes_no(f"Do you mean {amount}g? y / n ")
        if percent_type == "yes":
            profit_type = "grams"
        else:
            profit_type = "kilograms"

    response2 = input,num_check("Amount have: ", "Must be a number more than 0", float).lower()
    # Checks if the last letter is kg
    if response[-2:] == "kg":
        needed_weight = "kilograms"
        # Get amount
        amount = response[:-2]

    # Check if last character is g
    elif response[-2:] == " g":
        profit_type = "grams"
        # Get amount
        amount = response[:-2]

    else:
        # set response to amount for now
        profit_type = "unknown"
        amount = response

    if response == "unknown" and amount <= 10:
        weight_kilo = yes_no(f"Do you mean {amount:.2f}kg? y / n ")

        # set profit type
        if weight_kilo == "yes":
            profit_type = "kilograms"
        else:
            profit_type = "g"

    elif response == "unknown" and amount > 10:
        percent_type = yes_no(f"Do you mean {amount}g? y / n ")
        if percent_type == "yes":
            profit_type = "grams"
        else:
            profit_type = "kilograms"

    cost = currency,num_check("Ingredient cost: ", "Must be a number more than 0", float)




    # append responses into list
    ingredient_list.append(ingredient_name)
    amount_needed.append(response)
    amount_have.append(response2)
    ingredient_cost.append(cost)

ingredient_frame = pandas.DataFrame(ingredient_dict)

# * * * Printing area * * *
print(ingredient_frame)
print()
