# import pandas
import pandas
import re


# functions go here
# from chat gpt, extracts answers from an input string
def separate_amount_unit(input_str):
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


def change_to_smaller_unit(amount, unit):
    weight_conversion = {'kg': 1000, 'kilograms': 1000, 'l': 1000, 'liters': 1000}
    if unit in weight_conversion:
        return amount * weight_conversion[unit], 'g' if unit in ['kg', 'kilograms'] else 'ml'
    else:
        return amount, unit


# set up blank dictionaries / lists
group1 = []
group2 = []

Test_dict = {
    "test 1": group1,
    "test 2": group2
}

weight_list = ['grams', 'g', 'kg', 'kilograms', 'milliliters', 'ml', 'liters', 'l', 'individual', 'pieces']

# Main code
item_name = " "
while item_name.lower() != "xxx":
    answer1 = input("How much do you need? ").lower()
    if answer1 == "xxx":
        break

    # Extract amount and unit using extract_amount_unit function
    amount, unit = separate_amount_unit(answer1)
    if amount is not None and unit is not None:
        if amount is not None and float(amount) >= 0:  # Check if the amount is not negative
            print("Amount:", amount)
            print("Unit:", unit)
            if unit in weight_list:
                print("yay")
                amount, unit = change_to_smaller_unit(amount, unit)
                group1.append(amount)
                group2.append(unit)
            else:
                print("nay")
        else:
            print("Please enter a number more than 0")
    else:
        if answer1 is not None and separate_amount_unit(answer1)[0] is not None \
                and float(answer1) > 0:  # Check if the amount is not negative
            weight1 = input("What measurement is this in? ").lower()
            if weight1 in weight_list:
                print("yay")
                amount, unit = change_to_smaller_unit(answer1, unit)
                group1.append(answer1)
                group2.append(weight1)
            else:
                print("Invalid Input")
        else:
            print("Please enter a number more than 0")

# Construct DataFrame after the loop
test_frame = pandas.DataFrame(Test_dict)
print(test_frame)
