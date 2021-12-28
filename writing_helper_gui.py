from tkinter import Tk, Label, Text, INSERT, END

# Constants
WHITE = "#DDE5E7"
FONT = "Courier"
BLACK = '#080808'


class WritingHelperGUI:
    def __init__(self):
        # UI setup
        # Window
        self.window = Tk()
        self.window.title("Writing Helper")
        self.window.config(width=500, height=500,
                           background=BLACK, pady=50, padx=50)

        # Title
        self.title_label = Label(text="Writing Helper",
                                 font=(FONT, 50, "bold"), fg=WHITE, bg=BLACK)
        self.title_label.grid(column=0, row=0, pady=(0, 50))

        # Input text box
        self.text = Text(self.window, fg=BLACK, bg=WHITE, height=5, width=52, font=(FONT, 30),
                         wrap="word", highlightthickness=0)
        self.text.grid(column=0, row=2)
        self.text.focus()
        self.text.bind("<Key>", self.start)

        # Timer
        self.timer_label = Label(text="5", font=(
            FONT, 30, "bold"), fg=WHITE, bg=BLACK)
        self.timer_label.grid(column=0, row=1)

        self.after_id = None

        self.window.mainloop()

    def start(self, key):
        # kill the old timer
        if self.after_id is not None:
            self.window.after_cancel(self.after_id)
        self.count_down(5)

    # Count down mechanism

    def count_down(self, count):
        if count > 0:
            self.after_id = self.window.after(1000, self.count_down, count - 1)
            self.timer_label.config(text=count)
        else:
            self.after_id = None
            self.text.delete('1.0', END)
            self.timer_label.config(text='5')


test = WritingHelperGUI()
