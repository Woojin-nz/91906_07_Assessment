from tkinter import *
from functools import partial
import csv
import random
import string


class Start:
    def __init__(self):
        background = "#FFF4C3"

        # Start GUI
        self.start_frame = Frame(padx=10, pady=10, bg=background)
        self.start_frame.grid()

        # Country Capital Quiz Heading row 0
        self.capital_label = Label(self.start_frame, text="Country Capital Quiz",
                                   font="Helvetica 30 bold", bg=background)
        self.capital_label.grid(row=0)

        # Sub text and Instructions for the game row 1
        self.subtext_label = Label(self.start_frame, text="How well do you know world's capitals? \n\n"
                                                          "You'll be presented with 15 capitals from a list of 249 "
                                                          "capitals.\n "
                                                          "You'll need to match the capitals with their corresponding "
                                                          "country. \n\n "
                                                          "Please select the difficulty you wish to play.",
                                   font="Arial 10", bg=background)
        self.subtext_label.grid(row=1)

        # to_game button frame row 2
        self.to_game_frame = Frame(self.start_frame, bg=background)
        self.to_game_frame.grid(row=2)

        # Button Font
        button_font = ("Arial 15 bold")

        # to_game buttons row 2.0
        self.easy_button = Button(self.to_game_frame, text="Easy", font=button_font, bg="#99CCFF",
                                  command=self.to_easy, height=2, width=13, borderwidth=2)
        self.easy_button.grid(row=0, column=0, padx=10, pady=5)

        self.hard_button = Button(self.to_game_frame, text="Hard", font=button_font, bg="#FFBAB8",
                                  command=self.to_hard, height=2, width=13, borderwidth=2)
        self.hard_button.grid(row=0, column=1, padx=10, pady=5)

        # Help Button row 3
        self.help_button = Button(self.start_frame, text="Help", font="Helvetica 10 bold", height=2, width=10,
                                  borderwidth=3, command=self.help)
        self.help_button.grid(row=3, pady=5)

    def to_easy(self):
        Easy()

    def to_hard(self):
        Hard()

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="The quiz will present you with a capital \n\n You must identify the "
                                          "corresponding country.\n\n There "
                                          "are a total of 15 rounds.\n\n"
                                          "Easy mode is a multiple choice quiz.\n"
                                          "Hard mode you must type in the answer.")


class Help:
    def __init__(self, partner):
        background = "#FFF4C3"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press 'x' cross at the top, closes help and 'releases' help button.
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Information",
                                 font=("Helvetica", "24", "bold",),
                                 bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="", font="helvetica",
                               width=40, bg=background, wrap=500)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10, bg="maroon", fg="white",
                                  font="Helvetica" "10" "bold", command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


class Easy:
    def __init__(self):
        # Disable the easy game button (not yet implemented)
        # partner.easy_button.config(state=DISABLED)

        # GUI Setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Capital Label row 0
        self.capital_label = Label(self.game_frame, text="Capital",
                                   font="Helvetica 15 bold")
        self.capital_label.grid(row=0)

        # Setup grid for answer buttons row 2
        self.top_answers_frame = Frame(self.game_frame)
        self.top_answers_frame.grid(row=2)

        # Top level answers buttons row 2.0
        self.top_left_answer_button = Button(self.top_answers_frame, text="Top left",
                                             font="Helvetica 10 bold", padx=5, pady=5,
                                             command=lambda: self.reveal_answer(0))
        self.top_left_answer_button.grid(column=0, row=0)

        self.top_right_answer_button = Button(self.top_answers_frame, text="Top right",
                                              font="Helvetica 10 bold", padx=5, pady=5,
                                              command=lambda: self.reveal_answer(1))
        self.top_right_answer_button.grid(column=1, row=0)

        # Bottom level answers buttons row 2.1
        self.bottom_left_answer_button = Button(self.top_answers_frame, text="Bottom left",
                                                font="Helvetica 10 bold", padx=5, pady=5,
                                                command=lambda: self.reveal_answer(2))
        self.bottom_left_answer_button.grid(column=0, row=1)

        self.bottom_right_answer_button = Button(self.top_answers_frame, text="Bottom right",
                                                 font="Helvetica 10 bold", padx=5, pady=5,
                                                 command=lambda: self.reveal_answer(3))
        self.bottom_right_answer_button.grid(column=1, row=1)

    def reveal_answer(self, location):
        # Print corresponding number based on location
        # TL = 0 TR =1 BL = 2 BR = 3
        print(location)


class Hard:
    def __init__(self):

        # Background color is light yellow
        background = "#FFF4C3"

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
        self.game_frame = Frame(self.game_box, bg=background)
        self.game_frame.grid()

        # Capital Label row 0
        self.capital_label = Label(self.game_frame, text=question,
                                   font="Helvetica 15 bold", bg=background)
        self.capital_label.grid(row=0, padx=5, pady=10)

        # Setup Answer Entry row 1
        self.answer_entry = Entry(self.game_frame, font="Helvetica 15 bold")
        self.answer_entry.grid(row=1, pady=10, padx=30)
        self.answer_entry.focus()
        self.answer_entry.bind('<Return>', lambda e:self.check_answer())

        # Buttom frame for "guess" and "next" row 2
        self.button_frame = Frame(self.game_frame, bg=background)
        self.button_frame.grid(row=2)

        # Button to press when users have entered the country row 2.0 column 0
        self.answer_button = Button(self.button_frame, text="Guess", font="Helvetica 10 bold",
                                    command=lambda: self.check_answer())
        self.answer_button.grid(row=0, column=0, padx=5)

        # Button to go to the next question row 2.0 column 1
        self.next_button = Button(self.button_frame, text="Next", font="Helvetica 10 bold",
                                  command=lambda: self.next_question(my_list))
        self.next_button.grid(row=0, column=1, padx=5)
        self.next_button.config(state=DISABLED)
        self.next_button.bind('<Return>', lambda e:self.next_question(my_list))

        # Correct or incorrect Label row 3
        self.answer_box = Label(self.game_frame, text="", font="Helvetica", bg=background)
        self.answer_box.grid(row=3)

        # Total amount of correct answers and games played row 4
        self.points = Label(self.game_frame, text="{} correct / {} rounds played".format(self.score, self.played),
                            font="Helvetica 10", bg=background)
        self.points.grid(row=4)

    def check_answer(self):
        user_answer = self.answer_entry.get()
        self.played += 1
        if user_answer.casefold() == self.answer.casefold():
            self.answer_box.config(text="Correct!", fg="green")
            self.score += 1
            self.answer_entry.config(bg="#ACF392")
        else:
            self.answer_box.config(text="The correct country is {}".format(self.answer), fg="#F62121")
            self.answer_entry.config(bg="#F39292")
        self.next_button.config(state=NORMAL)
        self.answer_button.config(state=DISABLED)
        self.next_button.focus()
        self.points.config(text="{} correct / {} rounds played".format(self.score, self.played))

    def next_question(self, list):
        if self.played == 15:
            print("STOP")
        else:
            question_ans = random.choice(list)
            question = question_ans[1]
            self.answer = question_ans[0]
            self.capital_label.config(text=question)
            self.answer_entry.delete(0, "end")
            self.answer_box.config(text="")
            self.next_button.config(state=DISABLED)
            self.answer_button.config(state=NORMAL)
            self.answer_entry.config(bg="white")
            self.answer_entry.focus()
            print(question_ans)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Quiz")
    something = Start()
    root.mainloop()
