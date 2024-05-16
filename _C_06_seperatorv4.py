# import pandas
import pandas
import re


# functions go here
# from chat gpt, extracts answers from a input string
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


def check1(self):
    amount, unit = extract_amount_unit(answer1)
    if amount is not None and unit is not None:
        print("Amount:", amount)
        print("Unit:", unit)
        if unit in weight_list:
            print("yay")
            if unit in ['kg', 'kilograms'] or unit in ['l', 'liters']:
                digit = amount * 1000
                group1.append(digit)
                if unit in ['kg', 'kilograms']:
                    group2.append("g")
                if unit in ['l', 'liters']:
                    group2.append("ml")
            else:
                group1.append(amount)
                group2.append(unit)
        else:
            print("nay")
    else:
        check2()


def check2():
    weight1 = input("What measurement is this in? ").lower()
    if weight1 in weight_list:
        print("yay")
        if weight1 in ['kg', 'kilograms'] or weight1 in ['l', 'liters']:
            new_answer = float(answer1) * 1000
            group1.append(new_answer)
            if weight1 in ['kg', 'kilograms']:
                group2.append("g")
            if weight1 in ['l', 'liters']:
                group2.append("ml")
        else:
            group1.append(answer1)
            group2.append(weight1)
    else:
        print("Invalid Input")


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
    if answer1[0] == "-":
        print("Please enter a number more than 0")
        continue

    else:
        check1(answer1)

    # Extract amount and unit using extract_amount_unit function

# debugging
print(Test_dict)

# Construct DataFrame after the loop
test_frame = pandas.DataFrame(Test_dict)
print(test_frame)
