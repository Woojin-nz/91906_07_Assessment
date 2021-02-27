from tkinter import *
from functools import partial


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
                                  command=lambda: self.to_game(1), height=2, width=13, borderwidth=2)
        self.easy_button.grid(row=0, column=0, padx=10, pady=5)

        self.hard_button = Button(self.to_game_frame, text="Hard", font=button_font, bg="#FFBAB8",
                                  command=lambda: self.to_game(2), height=2, width=13, borderwidth=2)
        self.hard_button.grid(row=0, column=1, padx=10, pady=5)

        # Help Button row 3
        self.help_button = Button(self.start_frame, text="Help", font="Helvetica 10 bold", height=2, width=10,
                                  borderwidth=3, command=self.help)
        self.help_button.grid(row=3, pady=5)

    def to_game(self, difficulty):
        Game(self,difficulty)

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="The quiz will present you with a capital \n You must identify the "
                                          "corresponding country. \n\n The game has a 30 second timer for each round "
                                          "\n There "
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
        self.help_text = Label(self.help_frame, text="",font="helvetica",
                                width=40, bg=background, wrap=500)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10, bg="maroon",fg="white",
                                  font="Helvetica" "10" "bold", command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()

class Game:
    def __init__(self,partner, difficulty):
        print(difficulty)
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


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Quiz")
    something = Start()
    root.mainloop()
