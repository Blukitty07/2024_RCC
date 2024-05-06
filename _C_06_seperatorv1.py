# import pandas
import pandas


# functions go here
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


# string checker [also works for yes/no]
def string_checker(question, valid_responses, error):
    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item:
                return item

        print(error)


# set up blank dictionaries / lists
group1 = []
group2 = []

Test_dict = {
    "test 1": group1,
    "test 2": group2
}

weight_list = ['grams', 'g', 'kg', 'Kilograms', 'milliliters', 'ml', 'liters', 'l', 'individual', 'pieces']

# how to group those inside the list to equal to below need to figure out
kilograms = 1000
liters = 1000
grams = 1
milliliters = 1
individual = 1

# Main code
item_name = " "
while item_name.lower() != "xxx":
    answer1 = input("How much do you need?[please add a space inbetween the amount and the unit] ").lower()
    if answer1 == "xxx":
        break
    parts = answer1.split()
    # Split the input string by spaces
    print(parts)

    # returning infinite of the unit need to fix
    if len(parts) >= 2:
        if parts[1] in weight_list:
            print("yay")
            if parts[1] == "Kg" or "L":
                unit = parts[0] * 1000
                group1.append(unit)
            else:
                group1.append(parts[0])
            group2.append(parts[1])

        else:
            print("nay")

    else:
        weight1 = input("What measurement is this in? ").lower()
        if weight1 in weight_list:
            print("yay")
            group2.append(weight1)
            if weight1 == "Kg" or "L":
                unit = parts[0] * 1000
                group1.append(unit)
            else:
                group1.append(parts[0])
            group2.append(weight1)
        else:
            print("nay")

# Construct DataFrame after the loop
test_frame = pandas.DataFrame(Test_dict)
print(test_frame)
