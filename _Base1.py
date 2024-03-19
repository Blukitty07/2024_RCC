# libraries go here


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

# lists for ingredients


# Main routine goes here
# asks if user wants instructions
want_instructions = yes_no("Do you want to read the instructions? ").lower()
if want_instructions == "yes":
    print("instructions go here")
    print("program continues...")
    print()

# gets the name of the recipe
recipe_name = not_blank("What is the name of your recipe?",
                        "the recipe name cannot be blank")

# gets the serving size
serving_size = num_check("What is the serving size of this recipe?"
                         "The serving size must be an integer that's more than 0",
                         int)


