# import pandas
import pandas


# functions go here

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
            if parts[1] in ['kg', 'kilograms'] or parts[1] in ['l', 'liters']:
                unit = float(parts[0]) * 1000
                group1.append(unit)
                if parts[1] in ['kg', 'kilograms']:
                    group2.append("g")
                if parts[1] in ['l', 'liters']:
                    group2.append("ml")
            else:
                group1.append(parts[0])
                group2.append(parts[1])

        else:
            print("nay")

    else:
        weight1 = input("What measurement is this in? ").lower()
        if weight1 in weight_list:
            print("yay")
            if weight1 in ['kg', 'kilograms'] or weight1 in ['l', 'liters']:
                unit = float(parts[0]) * 1000
                group1.append(unit)
                if weight1 in ['kg', 'kilograms']:
                    group2.append("g")
                if weight1 in ['l', 'liters']:
                    group2.append("ml")
            else:
                group1.append(parts[0])
                group2.append(weight1)
        else:
            print("nay")

# Construct DataFrame after the loop
test_frame = pandas.DataFrame(Test_dict)
print(test_frame)
