# import libraries
import pandas


# functions here
def two_decimals(x):
    return "{:.2f}".format(x)


# set up lists, values and libraries
divide_answers = []
times_answers = []

test_dict = {
    "Division answers": divide_answers,
    "Multiplication Answers": times_answers
}

bird = 4
spiders = 12

# Main code
Answer_1 = (1 / 8)
Answer_2 = (Answer_1 * 4)
Answer_3 = (spiders / bird)
Answer_4 = (bird * spiders)

# add the answers into the respective lists
divide_answers.append(Answer_1)
times_answers.append(Answer_2)
divide_answers.append(Answer_3)
times_answers.append(Answer_4)

# make it into a frame
math_test_frame = pandas.DataFrame(test_dict)

# Rounding up (uses two decimal function)
to_round = ["Division answers", "Multiplication Answers"]
for item in to_round:
    math_test_frame[item] = math_test_frame[item].apply(two_decimals)


# printing area
print(math_test_frame)
