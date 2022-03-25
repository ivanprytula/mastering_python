from pprint import pprint

from question_models import LevelSyllabus
from quiz_data import syllabuses_data
from quiz_brain import QuizBrain
from quiz_ui import QuizInterface
from random import shuffle

question_bank = []
for syllabus in syllabuses_data:
    # pprint(syllabus)
    new_syllabus = LevelSyllabus(syllabus)
    question_bank.append(new_syllabus)

# print('question_bank:', question_bank)

quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)

quiz_ui.start_the_game()

# quiz_ui.add_player()
# connected_players = quiz_ui.get_active_players()
# print(connected_players)
