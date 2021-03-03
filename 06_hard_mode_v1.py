import csv
import random

# Get list from csv and import it

# name of csv file goes here...
with open('country-list.csv', 'r') as f:

    # make csv file into list
    file = csv.reader(f)
    next(f)
    my_list = list(file)

score = 0
# Loop the quiz 15 times
for i in range(0,15):
    # choose an item from the main list, this item is itself a list
    question_ans = random.choice(my_list)

    # first item in small list
    question = question_ans[1]
    answer = question_ans[0]

    print("Question:Which Country has the capital {}?".format(question))
    user_answer = input("Answer:")
    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect")

print("You managed to get {} right out of 15".format(score))


