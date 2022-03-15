from question_model import Question
from quiz_data import question_data
from quiz_brain import QuizBrain
from quiz_ui import QuizInterface
from random import shuffle

question_bank = []
for question in question_data:
    new_question = Question(question)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)
