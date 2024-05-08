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
    amount, unit = extract_amount_unit(answer1)
    if amount is not None and unit is not None:
        print("Amount:", amount)
        print("Unit:", unit)
        if unit in weight_list:
            print("yay")
            if unit in ['kg', 'kilograms'] or unit in ['l', 'liters']:
                unit = amount * 1000
                group1.append(unit)
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
        weight1 = input("What measurement is this in? ").lower()
        if weight1 in weight_list:
            print("yay")
            if weight1 in ['kg', 'kilograms'] or weight1 in ['l', 'liters']:
                unit = float(amount) * 1000
                group1.append(unit)
                if weight1 in ['kg', 'kilograms']:
                    group2.append("g")
                if weight1 in ['l', 'liters']:
                    group2.append("ml")
            else:
                group1.append(amount)
                group2.append(weight1)
        else:
            print("Invalid Input")

# Construct DataFrame after the loop
test_frame = pandas.DataFrame(Test_dict)
print(test_frame)
