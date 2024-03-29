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
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some Question Text", fill=THEME_COLOR,
                                                     font=("Arial", 15, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_card = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 10, "bold"))
        self.score_card.grid(row=0, column=1)

        self.wrong_button_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_button_img, highlightthickness=0, command=self.wrong_clicked)
        self.wrong_button.grid(row=2, column=0)

        self.right_button_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_button_img, highlightthickness=0, command= self.correct_clicked)
        self.right_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        # Get the next question from the QuizBrain and update the canvas
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_card.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def correct_clicked(self):
        # Handle the click on the True button
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong_clicked(self):
        # Handle the click on the False button
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, valid):
        # Provide feedback by changing the canvas background color and move to the next question
        if valid:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        # Use window.after to delay getting the next question for 1000 milliseconds.
        self.window.after(1000, self.get_next_question)

