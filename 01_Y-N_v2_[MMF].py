# functions go here
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter 'Yes' or 'No'")


# main routine goes here
for item in range(0, 8):
    want_instructions = yes_no("Do you want to read the instructions? ").lower()

    if want_instructions == "yes":
        print("instructions go here")

    print("program continues...")
    print()
