# import libraries
import pandas
import math


# checks if a valid number
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


# checks for response being not blank
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


# string checker [also works for yes/no]
def string_checker(question, num_letters, valid_responses, error):
    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item:
                return item

        print(error)


# finds out the number for the weight and starts the measurement indemnifying process
def weight_check(question, valid_responses, num_type, error):
    while True:
        response = num_check(question, "Must be a number more than 0", float)

        for item in valid_responses:
            if response == item:
                return response and item
            else:
                weight_question_1(response)


# looping weirdly
# finds out which weight measurement [g/ml/individual]
def weight_question_1(response):
    while True:
        weight_check1 = string_checker(
            "Is this ingredient measured in grams/ milliliters / individual? [for example: "
            "food coloring 15mL or 6 eggs] "
            "[y / n] ", 0, yn_list, "please enter a Valid answer [ y / n] ").lower()
        if weight_check1 == "yes" or "y":
            weight1 = input("which one? [' g' / 'mL' / 'individual' ] ").lower()
            for item in weight_q1_list:
                if weight1 == item:
                    return response and weight1

        elif weight_check1 == "no" or "n":
            weight_question_2(response, weight_q2_list)


# finds out which weight measurement [kg/l]
def weight_question_2(response, valid_responses):
    weight_check2 = string_checker(
        "is this ingredient measured in Kilograms / Liters? [for example: Milk 2L] ", float, yn_list,
        "please enter a Valid answer [ y / n] ").lower()
    if weight_check2 == "yes" or "y":
        weight2 = input("Which one [Kilograms / Liters]? ").lower()
        for item in weight_q2_list:
            if weight2 == item:
                return response * 100 and weight_check2

    if weight_check2 == "no" or "n":
        print(
            "The only available units are grams, milliliters, individual, kilograms and liters. Please retry ")
        weight_question_1(response)


# set up blank dictionaries
ingredient_list = []
amount_needed = []
amount_have = []
ingredient_cost = []

# to do. . .
# get currency to work properly
# figure out how to add weights onto the end
ingredient_dict = {
    "ingredient": ingredient_list,
    "need": amount_needed,
    "have": amount_have,
    "cost": ingredient_cost
}

yn_list = ["yes", "no", "y", "n"]
weight_list = [" g", " l", "ml", "kg", "individual"]
weight_q1_list = [" g", "grams", "ml", "milliliters", "individual"]
weight_q2_list = ["l", "liters", "kg", "kilogram"]

# loop to get ingredient name, amount needed, amount have and ingredient cost
item_name = " "
while item_name.lower() != "xxx":
    print()
    # get name, quantity and item
    # get ingredients name, amount needed and have and ingredient cost
    ingredient_name = not_blank("Ingredient name: ", "")

    if ingredient_name.lower() == "xxx":
        break

    needed = weight_check("How much of the ingredient does the recipe call for? ", weight_list, float,
                          "An number over 0 is required, please retry")

    have = weight_check("How much of the ingredient do you currently have on hand? ", weight_list, float,
                        "A number over 0 is required. Please retry")

    cost = num_check("Ingredient cost: ", "Must be a number more than 0", float)

    # append responses into list
    ingredient_list.append(ingredient_name)
    amount_needed.append(needed)
    amount_have.append(have)
    ingredient_cost.append(cost)

ingredient_frame = pandas.DataFrame(ingredient_dict)

# * * * Printing area * * *
print(ingredient_frame)
print()
