import csv
import random
import string



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

    print(question_ans)

    print("Question: Which Country has the capital {}?".format(question))
    user_answer = input("Answer: ")
    if user_answer.casefold() == answer.casefold():
        print("Correct!")
        score += 1
    else:
        print("Incorrect, the correct answer is {}".format(answer))

total_score= score/15
print("You managed to get {} right out of 15, {:.2f}% correct".format(score,total_score))


