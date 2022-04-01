import sys

from question_models import LevelSyllabus
from quiz_data import syllabuses_data
from quiz_brain import QuizBrain
from quiz_ui import QuizInterface

question_bank = []
for syllabus in syllabuses_data:
    # pprint(syllabus)
    new_syllabus = LevelSyllabus(syllabus)
    question_bank.append(new_syllabus)

# print('question_bank:', question_bank)

quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)

# connected_players = quiz_ui.get_active_players()
# print(connected_players)

# If this program was run (instead of imported), run the game:
if __name__ == "__main__":
    try:
        quiz_ui.start_the_game()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
