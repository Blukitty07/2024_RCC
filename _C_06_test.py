import re
import pandas


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


# Test the function with example inputs
inputs = ["6kg", "6 kg", "6kilograms", "6 kilograms"]
for input_str in inputs:
    amount, unit = extract_amount_unit(input_str)
    print(f"Input: {input_str}, Amount: {amount}, Unit: {unit}")

    # second testing area for integrating code

    # figure out how to input for each question
    # checks if the extracted parts contain a number and a valid weight


def check1(user_input, append_to):
    amount, unit = extract_amount_unit(user_input)
    if amount is not None and unit is not None:
        print("Amount:", amount)
        print("Unit:", unit)
        if unit in weight_list:
            print("yay")
            if unit in ['kg', 'kilograms'] or unit in ['l', 'liters']:
                digit = amount * 1000
                if unit in ['kg', 'kilograms']:
                    append_to.append((digit, "g"))
                if unit in ['l', 'liters']:
                    append_to.append((digit, "mL"))
            else:
                append_to.append((amount, unit))
        else:
            print("nay")
    else:
        check2(user_input, append_to)

    # carries on from check1 making sure that a valid weight gets inputted


def check2(user_input, append_to):
    weight1 = input("What measurement is this in? ").lower()
    if weight1 in weight_list:
        print("yay")
        if weight1 in ['kg', 'kilograms'] or weight1 in ['l', 'liters']:
            new_answer = float(user_input) * 1000
            if weight1 in ['kg', 'kilograms']:
                append_to.append((new_answer, "g"))
            if weight1 in ['l', 'liters']:
                append_to.append((new_answer, "mL"))

        else:
            append_to.append((user_input, weight1))
    else:
        print("Invalid Input")


amount_needed = []

weight_list = ['grams', 'g', 'kg', 'kilograms', 'milliliters', 'ml', 'liters', 'l', 'individual', 'pieces']

# gets the serving size

need = input("How much do you need? ")
if need[0] == "-":
    print("Please enter a number more than 0")
else:
    check1(need, amount_needed)

print(amount_needed)

