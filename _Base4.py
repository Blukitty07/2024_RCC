# libraries go here
import pandas
import re


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


# currency formatting
def currency(x):
    return "${:.2f}".format(x)

# not being used anymore

# string checker [also works for yes/no]
# def string_checker(question, valid_responses, error):
    #   while True:
    #   response = input(question).lower()

    #   for item in valid_responses:
    #       if response == item:
    #           return item

#   print(error)


# round numbers up to two dp
# def two_decimals(x):
    # return "{:.2f}".format(x)


# from chat gpt, extracts answers from a input string after every number


def extract_amount_unit(input_str):
    # Define regular expression patterns for number and unit
    pattern = r'(\d+(\.\d+)?)\s*(\D+)'
    # Search for matches
    match = re.match(pattern, input_str)
    if match:
        # Extract groups
        amount = float(match.group(1))
        unit = match.group(3)
        return amount, unit
    else:
        return None, None
# [above] separates an input after every number


# figure out how to input for each question
# checks if the extracted parts contain a number and a valid weight
def check1(question, append_to, second_append, error):
    while True:
        user_input = input(question)
        if user_input[0] == "-":
            print("Please enter a valid number, that is more than 0.")
            continue
        amount, unit = extract_amount_unit(user_input)
        if amount is not None and unit is not None:
            if unit in weight_list:
                if unit in ['kg', 'kilograms'] or unit in ['l', 'liters']:
                    digit = amount * 1000
                    second_append.append(digit)
                    if unit in ['kg', 'kilograms']:
                        append_to.append((digit, "g"))
                        break
                    if unit in ['l', 'liters']:
                        append_to.append((digit, "mL"))
                        break
                else:
                    append_to.append((amount, unit))
                    second_append.append(amount)
                    break

            else:
                print(error)

        else:
            check2(user_input, append_to, second_append, "Please enter a valid weight [list of accepted weights "
                                                         "'grams', 'kilograms', 'milliliters', 'liters', "
                                                         "'individual', 'pieces'")
            break

    # carries on from check1 making sure that a valid weight gets inputted


# carries on from check1 making sure that a valid weight gets inputted
def check2(user_input, append_to, second_append, error):
    while True:
        try:
            user_input = int(user_input)
            if user_input <= 0:
                print("Please enter a valid number, that is more than 0.")
                continue
        except ValueError:
            user_input = input("Please enter a valid number, that is more than 0. ")
            continue
        weight1 = input("What measurement is this in? ").lower()
        if weight1 in weight_list:
            if weight1 in ['kg', 'kilograms'] or weight1 in ['l', 'liters']:
                new_answer = float(user_input) * 1000
                second_append.append(new_answer)
                if weight1 in ['kg', 'kilograms']:
                    append_to.append((new_answer, "g"))
                    break
                if weight1 in ['l', 'liters']:
                    append_to.append((new_answer, "mL"))
                    break

            else:
                append_to.append((user_input, weight1))
                second_append.append(user_input)
                break
        else:
            print(error)
            continue


# set up blank dictionaries and lists
ingredient_list = []
amount_needed = []
amount_have = []
ingredient_cost = []
have_numbers = []
need_numbers = []

ingredient_dict = {
    "Ingredient Name": ingredient_list,
    "Ingredients needed": amount_needed,
    "Ingredients on hand": amount_have,
    "Cost of ingredient": ingredient_cost
}

number_dict = {
    "Numbers for Needed": need_numbers,
    "Numbers for Have": have_numbers
}

# list of valid weights
weight_list = ['grams', 'g', 'kg', 'kilograms', 'milliliters', 'ml', 'liters', 'l', 'individual', 'pieces', 'piece']

# Main routine goes here
# asks if user wants instructions
want_instructions = yes_no("Do you want to read the instructions? ").lower()
if want_instructions == "yes":
    print()
    print("This is a Recipe Cost Calculator.")
    print("In this you will be asked you recipes name, serving size and ingredients.")
    print("You'll be asked for your ingredients name, the amount the recipe needs, the amount that you have on hand, "
          "and the cost of the ingredient.")
    print("To stop inputting more ingredients you can enter 'xxx' when it asks for the ingredients name.")
    print("It'll then print out both on here and on a file [titled the name of the recipe]")
    print("the recipes name, serving size, ingredients [names, amounts needed and on hand and the cost], the amount of")
    print("ingredients used in this recipe and the total cost of the recipe and the cost per serving.")
    print()

# gets the name of the recipe
recipe_name = not_blank("What is the name of your recipe? ",
                        "the recipe name cannot be blank")

# gets the serving size of the recipe
serving_size = num_check("What is the serving size of this recipe? ", "The serving size must be an integer"
                                                                      " that's more than 0 ", int)

# loop to get ingredients name, amount needed for recipe, amount the user has on hand and ingredient cost
item_name = " "
while item_name.lower() != "xxx":
    print()
    # get name, quantity and item
    # get ingredients name, amount needed and have and ingredient cost
    # print inbetween for nicer reading
    print("Respond with 'xxx' to stop inputting ingredients")
    ingredient_name = not_blank("Ingredient name: ", "")
    print()

    if ingredient_name.lower() == "xxx":
        break

# Asking for the need amount [error message only asks for number to make it easy to read and less confusing,
    # but will accept a number and valid weight
    check1("How much do you need? ", amount_needed, need_numbers, "This is an Invalid Input, please enter a valid "
                                                                  "number")
    print()


# Asking for the have amount [error message only asks for number to make it easy to read and less confusing,
    # but will accept a number and valid weight
    check1("How much did you buy / do you have on hand? ", amount_have, have_numbers, "This is an Invalid Input "
                                                                                      "please enter a valid number")
    print()

    cost = num_check("How much did the ingredient on hand cost? ", "Must be a number more than 0", float)
    print()

    # append responses not already append into list
    ingredient_list.append(ingredient_name)
    ingredient_cost.append(cost)

# make the panda frames
ingredient_frame = pandas.DataFrame(ingredient_dict)
numbers_frame = pandas.DataFrame(number_dict)


# Ensures that the cost column is numeric for equations
ingredient_frame['Cost of ingredient'] = pandas.to_numeric(ingredient_frame['Cost of ingredient'])

# Ensures that the numbers are numeric for equations
numbers_frame['Numbers for Needed'] = pandas.to_numeric(numbers_frame['Numbers for Needed'])
numbers_frame['Numbers for Have'] = pandas.to_numeric(numbers_frame['Numbers for Have'])


# calculating the cost of each ingredient in regard to the recipe
ingredient_frame['Cost to make'] = (ingredient_frame['Cost of ingredient'] / numbers_frame['Numbers for Have']) \
                                   * numbers_frame['Numbers for Needed']


# calculate total cost
total_cost = ingredient_frame['Cost to make'].sum()

# calculate cost per serving
total_cost_per_serve = total_cost / serving_size

# applying the currency to the costs
ingredient_frame['Cost of ingredient'] = ingredient_frame['Cost of ingredient'].apply(currency)
ingredient_frame['Cost to make'] = ingredient_frame['Cost to make'].apply(currency)
total_cost = currency(total_cost)
total_cost_per_serve = currency(total_cost_per_serve)

# set index at end (before printing)
ingredient_frame = ingredient_frame.set_index('Ingredient Name')

# strings for printing / exporting set up area
Heading_string = f"* * * * Recipe Cost Calculator {recipe_name} * * * *"
recipe_name_string = f"Recipe name: {recipe_name}"
serving_string = f"Serving size: {serving_size}"

ingredient_txt = pandas.DataFrame.to_string(ingredient_frame)


total_string = f"Total cost: {total_cost}"
cost_per_serve_string = f"Cost per serving: {total_cost_per_serve}"

# Set pandas options to display all columns
pandas.set_option('display.max_columns', None)


to_write = [Heading_string, recipe_name_string, serving_string, ingredient_txt, total_string, cost_per_serve_string]

# * * * Printing area * * *
# write output to file
# create file to hold data
file_name = f"{recipe_name} .txt"
text_file = open(file_name, "w+")

# printing output for the file
for item in to_write:
    text_file.write(item)
    text_file.write("\n\n")

# close the file
text_file.close()

# Print stuff
for item in to_write:
    print(item)
    print()
