# import libraries
import pandas


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
# loop to get ingredient name, amount needed, amount have and ingredient cost
item_name = " "
while item_name.lower() != "xxx":
    print()
    # get name, quantity and item
    # get ingredients name, amount needed and have and ingredient cost
    ingredient_name = not_blank("Ingredient name: ", "")

    if ingredient_name.lower() == "xxx":
        break

    needed = num_check("Amount needed: ", "Must be a number more than 0", float)

    have = num_check("Amount have: ", "Must be a number more than 0", float)

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

