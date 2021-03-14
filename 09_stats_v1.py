# Make an if statement go to the end of game.
x = input("")
if x == "a":
    Hello()
else:
    print("e")


class Hello:
    def __init__(self):
        # End Frame
        self.end_box = Toplevel()
        self.end_frame = Frame(self.end_box)
        self.end_frame.grid(row=0)

        # Heading row 0
        self.end_heading = Label(self.end_frame, text="Thanks for playing!", font="Helvetica 25 bold")
        self.end_heading.grid(row=0)


