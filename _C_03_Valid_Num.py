# import libraries

# Functions

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


# main routine
#for serving use
get_int = num_check("how many do you have ",
                    "please enter an integer more than 0\n",
                    int)
#for ingredent use
get_cost = num_check("How much does it cost? $",
                     "Please enter a number more than 0\n",
                     float)
