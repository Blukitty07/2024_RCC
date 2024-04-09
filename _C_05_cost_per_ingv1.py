# import libraries
import math
import pandas


# functions
# checks for a valid integer or float
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


# string checker [also works for yes/no]
def string_checker(question, valid_responses, error):
    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item:
                return item

        print(error)


# identifies and returns ingredients weight
def weight_question(question):
    while True:
        response = num_check(question, "Must be a number more than 0", float)
        weight = string_checker("which unit is this ingredient measured in? [g, ml, kg, l, or individual] ",
                                weight_list, "please enter a valid answer [g, ml, kg, l, or individual] ").lower()
        for item in weight_list:
            if weight == item:
                return response, weight


# set up blank dictionaries and lists
need = []
we_have = []
ing_cost = []
leftover = []
cost_per_1 = []

math_dict = {
    "amount need": need,
    "amount have": we_have,
    "cost": ing_cost,
    "leftover amount": leftover,
    "cost per 1": cost_per_1
}

grams = 1
milliliters = 1
individual = 1
kilograms = 100
liters = 100

weight_list = ["g", "l", "ml", "kg", "individual"]

# main routine
for item in range(0, 6):
    print()
    # get amounts for need, have and cost
    needed = weight_question("How much of the ingredient does the recipe call for? ")
    print()

    have = weight_question("How much of the ingredient do you currently have on hand? ")
    print()

    cost = num_check("How much did the ingredient on hand cost? ", "Must be a number more than 0", float)
    print()

    # append responses into list
    need.append(needed)
    we_have.append(have)
    ing_cost.append(cost)

test_frame = pandas.DataFrame(math_dict)
test_frame = test_frame.set_index('wowie')

# printing area
print()
print(test_frame)
