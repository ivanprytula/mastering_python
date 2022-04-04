import sys

from question_models import LevelSyllabus
from quiz_data import syllabuses_data, syllabuses_levels_full_names
from quiz_brain import QuizBrain
from quiz_ui import QuizInterface

question_bank = []
for syllabus in syllabuses_data:
    new_syllabus = LevelSyllabus(syllabus)
    question_bank.append(new_syllabus)

quiz = QuizBrain(question_bank, syllabuses_levels_full_names)

quiz_ui = QuizInterface(quiz)

# If this program was run (instead of imported), run the game:
if __name__ == "__main__":
    try:
        quiz_ui.start_the_game()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
