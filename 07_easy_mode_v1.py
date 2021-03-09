from tkinter import *
import csv
import random


class Start:
    def __init__(self):
        # Start GUI
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Country Capital Quiz Heading row 0
        self.capital_label = Label (self.start_frame, text="Country Capital Quiz",
                                    font= "Helvetica 20 bold")
        self.capital_label.grid(row=0)

        # to_game button row 1
        self.easy_button = Button(text="Easy", command= self.to_game)
        self.easy_button.grid(row=1)

    def to_game(self):
        Game()

class Game:
    def __init__(self):

        # Import the csv file, name of csv file goes here...
        with open('country-list.csv', 'r') as f:
            # make csv file into list
            file = csv.reader(f)
            next(f)
            my_list = list(file)

        # choose an item from the main list, this item is itself a list
        question_ans = random.choice(my_list)
        print(question_ans)

        # Inital Score
        self.score = 0

        # Amounts of games played
        self.played = 0

        # first item in small list
        question = question_ans[1]
        self.answer = question_ans[0]

        # GUI Setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid(padx=10, pady=10)

        # Capital Label row 0
        self.capital_label = Label(self.game_frame, text=question,
                                   font="Helvetica 15 bold")
        self.capital_label.grid(row=0)

        # Setup grid for answer buttons row 2
        self.top_answers_frame = Frame(self.game_box)
        self.top_answers_frame.grid(row=2, padx=5)

        # Top level answers buttons row 2.0
        self.top_left_answer_button = Button(self.top_answers_frame, text="Top left",
                                             font="Helvetica 10 bold", padx=5, pady=5,
                                             command=lambda: self.reveal_answer(0))
        self.top_left_answer_button.grid(column=0, row=0,padx=5,pady=5)

        self.top_right_answer_button = Button(self.top_answers_frame, text="Top right",
                                             font="Helvetica 10 bold", padx=5,pady=5,
                                             command=lambda: self.reveal_answer(1))
        self.top_right_answer_button.grid(column=1, row=0,padx=5,pady=5)

        # Bottom level answers buttons row 2.1
        self.bottom_left_answer_button = Button(self.top_answers_frame, text="Bottom left",
                                             font="Helvetica 10 bold", padx=5, pady=5,
                                             command=lambda: self.reveal_answer(2))
        self.bottom_left_answer_button.grid(column=0, row=1,padx=5,pady=5)

        self.bottom_right_answer_button = Button(self.top_answers_frame, tex t="Bottom right",
                                              font="Helvetica 10 bold", padx=5, pady=5,
                                              command=lambda: self.reveal_answer(3))
        self.bottom_right_answer_button.grid(column=1, row=1,padx=5,pady=5)


    def reveal_answer(self, location):
        # Print corresponding number based on location
        # TL = 0 TR =1 BL = 2 BR = 3
        print(location)





# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Quiz")
    something = Start()
    root.mainloop()

