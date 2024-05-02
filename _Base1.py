# libraries go here
import pandas


# functions go here
# checks for a yes/no answer
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter 'Yes' or 'No'")


# Checks that there is an answer [ie not blank or just a space]
def not_blank(question, error):
    while True:
        response = input(question)

        if response == "":
            print(f"{error}. Sorry but this cannot be blank. Please retry")

        elif response == " ":
            print(f"{error}. Sorry but this cannot be blank. Please retry")

        else:
            return response


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


# identifies and returns ingredients weight
def weight_question(question):
    while True:
        response = num_check(question, "Must be a number more than 0", float)
        weight = string_checker("which unit is this ingredient measured in? [g, ml, kg, l, or individual] ",
                                weight_list, "please enter a valid answer [g, ml, kg, l, or individual] ").lower()
        for item in weight_list:
            if weight == item:
                return response, weight


# round numbers up to two dp
def two_decimals(x):
    return "{:.2f}".format(x)


# set up blank dictionaries
ingredient_list = []
amount_needed = []
amount_have = []
ingredient_cost = []

ingredient_dict = {
    "Ingredient Name": ingredient_list,
    "Ingredients needed": amount_needed,
    "Ingredients on hand": amount_have,
    "Cost of ingredient": ingredient_cost
}

yn_list = ["yes", "no", "y", "n"]
weight_list = ["g", "l", "ml", "kg", "individual"]

# Main routine goes here
# asks if user wants instructions
want_instructions = yes_no("Do you want to read the instructions? ").lower()
if want_instructions == "yes":
    print("instructions go here")
    print("program continues...")
    print()


# gets the name of the recipe
recipe_name = not_blank("What is the name of your recipe? ",
                        "the recipe name cannot be blank")

# gets the serving size
serving_size = num_check("What is the serving size of this recipe? ", "The serving size must be an integer"
                         " that's more than 0 ", int)

# loop to get ingredient name, amount needed, amount have and ingredient cost
item_name = " "
while item_name.lower() != "xxx":
    print()
    # get name, quantity and item
    # get ingredients name, amount needed and have and ingredient cost
    # print inbetween for nicer reading
    ingredient_name = not_blank("Ingredient name: ", "")
    print()

    if ingredient_name.lower() == "xxx":
        break

    needed = weight_question("How much of the ingredient does the recipe call for? ")
    print()

    have = weight_question("How much of the ingredient do you currently have on hand? ")
    print()

    cost = num_check("How much did the ingredient on hand cost? ", "Must be a number more than 0", float)
    print()

    # append responses into list
    ingredient_list.append(ingredient_name)
    amount_needed.append(needed)
    amount_have.append(have)
    ingredient_cost.append(cost)

ingredient_frame = pandas.DataFrame(ingredient_dict)
# ingredient_frame = ingredient_frame.set_index('Ingredient Name')


# calculating the cost of each ingredient in regard to the recipe
ingredient_frame['Cost to make'] = ingredient_frame['Cost of ingredient'] / ingredient_frame['Ingredients on hand']\
                                   * ingredient_frame['Ingredients needed']


# calculate total cost
total_cost = ingredient_frame['Cost to make'].sum()

# calculate cost per serving
total_cost_per_serve = total_cost/serving_size


# applying the currency to the cost
ingredient_frame['Cost of ingredient'] = ingredient_frame['Cost of ingredient'].apply(currency)

# * * * Printing area * * *
print("Recipe name:", recipe_name)
print("Serving size:", serving_size)
print(ingredient_frame)
print("Total Cost:", currency(total_cost))
print("Cost per serving:", currency(total_cost_per_serve))
