from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Master")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_card = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 10, "bold"))
        self.score_card.grid(row=0, column=1)

        self.wrong_button_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_button_img, highlightthickness=0)
        self.wrong_button.grid(row=2, column=0)

        self.right_button_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_button_img, highlightthickness=0)
        self.right_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()
    # It takes the input from the next_question and reflects the question on canvas

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
