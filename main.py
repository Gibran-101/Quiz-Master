from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Creating an instance of the QuizBrain class with the populated question_bank lis
quiz = QuizBrain(question_bank)
# As quiz is an object of class QuizBrain, the class QuizInterface only accepts the obects
# of that particular class only.
quiz_ui = QuizInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
