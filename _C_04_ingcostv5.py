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
def string_checker(question, valid_responses, error):
    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item:
                return item

        print(error)


# get the given number
# finds out which weight measurement [g/ml/individual]
def weight_question_1(question):
    while True:
        response = num_check(question, "Must be a number more than 0", float)
        weight_check1 = string_checker(
            "Is this ingredient measured in grams/ milliliters / individual? [for example: "
            "food coloring 15mL or 6 eggs] "
            "[y / n] ", yn_list, "please enter a Valid answer [ y / n ] ").lower()
        if weight_check1 == "yes" or weight_check1 == "y":
            weight1 = string_checker("which one? ['g' / 'mL' / 'individual' ] ", weight_q1_list,
                                     "Please enter a valid weight ['g' / 'mL' / 'individual' ] ").lower()
            for item in weight_q1_list:
                if weight1 == item:
                    return response, weight1
        else:
            if weight_check1 == "no" or weight_check1 == "n":
                break  # Exit the loop if the answer is no
    return weight_question_2(response, weight_q2_list)


# finds out which weight measurement [kg/l]
def weight_question_2(response, valid_responses):
    while True:
        weight_check2 = string_checker(
            "is this ingredient measured in Kilograms / Liters? [for example: Milk 2L] [ y / n ] ", yn_list,
            "please enter a Valid answer [ y / n] ").lower()
        if weight_check2 == "yes" or weight_check2 == "y":
            weight2 = string_checker("Which one [ kg / l ]? ", weight_q2_list,
                                     "Please enter a valid weight [ kg / l ]? ] ").lower()
            for item in weight_q2_list:
                if weight2 == item:
                    return response, weight2

        if weight_check2 == "no" or weight_check2 == "n":
            print(
                "The only available units are grams, milliliters, individual, kilograms and liters. Please retry ")
            break  # Exit the loop if the answer is no


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
    "need for recipe": amount_needed,
    "have on hand": amount_have,
    "ingredient cost": ingredient_cost
}

yn_list = ["yes", "no", "y", "n"]
weight_list = ["g", " l", "ml", "kg", "individual"]
weight_q1_list = ["g", "grams", "ml", "milliliters", "individual"]
weight_q2_list = ["l", "liters", "kg", "kilogram"]

# loop to get ingredient name, amount needed, amount have and ingredient cost
item_name = " "
while item_name.lower() != "xxx":
    print()
    # get name, quantity and item
    # get ingredients name, amount needed and have and ingredient cost
    # print inattention for nicer reading
    ingredient_name = not_blank("Ingredient name: ", "")
    print()

    if ingredient_name.lower() == "xxx":
        break

    needed = weight_question_1("How much of the ingredient does the recipe call for? ")
    print()

    have = weight_question_1("How much of the ingredient do you currently have on hand? ")
    print()

    cost = num_check("Ingredient cost: ", "Must be a number more than 0", float)
    print()

    # append responses into list
    ingredient_list.append(ingredient_name)
    amount_needed.append(needed)
    amount_have.append(have)
    ingredient_cost.append(cost)

ingredient_frame = pandas.DataFrame(ingredient_dict)
ingredient_frame = ingredient_frame.set_index('ingredient')

# applying the currency to the cost
ingredient_frame['ingredient cost'] = ingredient_frame['ingredient cost'].apply(currency)

# * * * Printing area * * *
print(ingredient_frame)
print()
