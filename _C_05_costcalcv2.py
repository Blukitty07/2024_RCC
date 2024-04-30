# import libraries
import pandas


# functions here
# round numbers up to two dp
def two_decimals(x):
    return "{:.2f}".format(x)


# Checks that an input is a float or integer > 0
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


# set up lists, values and libraries
# preset values
ingredient_on_hand = []
ingredient_needed = []
cost_of_ingredients = []

test_dict = {
    "Ingredients on hand": ingredient_on_hand,
    "Ingredients needed": ingredient_needed,
    "Cost of ingredients": cost_of_ingredients
}

# Main code
serving = num_check("How many servings does this recipe make? ", "must be a number mor than 0", int)

check = " "
while check != "xxx":
    print()

    check = input("Do you have more ingredients? ").lower()

    if check == "xxx":
        break

    need = num_check("How much do you need? ", "must be a number more thant 0", float)

    have = num_check("How much did you buy/ do you have? ", "must be a number more than 0", float)

    cost = num_check("How much did it cost to buy? ", "must be a number more than 0", float)

# add the answers into the respective lists
    ingredient_needed.append(need)
    ingredient_on_hand.append(have)
    cost_of_ingredients.append(cost)

# divide answers to get the cost of each


# make it into a frame
test_frame = pandas.DataFrame(test_dict)


# calculate cost to make each ingredient
test_frame['Cost to make'] = test_frame['Cost of ingredients'] / test_frame['Ingredients on hand'] \
                             * test_frame['Ingredients needed']

# calculate total cost
total_cost = test_frame['Cost to make'].sum()

# Rounding up (uses two decimal function)
to_round = ["Cost of ingredients", "Cost to make"]
for item in to_round:
    test_frame[item] = test_frame[item].apply(two_decimals)

# printing area
print(test_frame)
print("Total Cost:", two_decimals(total_cost))
