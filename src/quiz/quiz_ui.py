import logging
import random

from rich.console import Console

from question_models import LevelSyllabus
from quiz_brain import QuizBrain

logger = logging.getLogger(__name__)

console = Console()


INPUT_ATTEMPTS_LIMIT = 3
RESTART_MESSAGE = "You used all your attempts to enter.\nGame is restarting..."


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.active_players: list = []

    @staticmethod
    def show_caption(text: str) -> None:
        print(f"\n<<< {text} >>>")

    @staticmethod
    def horizontal_ui_deliminator(character: str) -> None:
        random_range_start = int(random.random() * 100)
        random_range_end = int(random.random() * 100)
        for _ in range(random_range_start, random_range_end):
            print(rf"{character}", end="")

    def quiz_greeting(self) -> None:
        self.horizontal_ui_deliminator("*")
        print("\nWelcome to the quiz!")
        self.horizontal_ui_deliminator("^")

    def add_player(self) -> None:
        enter_name_attempts = 1
        while enter_name_attempts <= INPUT_ATTEMPTS_LIMIT:
            try:
                new_player = input("\nEnter your name: ")

                if not new_player.isalpha():
                    raise ValueError(
                        "Player name must be string, not numeric or special "
                        "characters."
                    )

                self.active_players.append(new_player)
                print("\tYou are in game!")
                break
            except ValueError:
                logger.warning(
                    "Player name must be string, not numeric or special " "characters."
                )
                # print("Player name must be string, not numeric or special "
                #       "characters.")

                enter_name_attempts += 1
        else:
            if enter_name_attempts > 2:
                logger.warning(f"{RESTART_MESSAGE}")
                self.start_the_game()

    def get_active_players(self) -> list:
        return self.active_players

    def select_exam(self) -> LevelSyllabus:
        """Returns instance of selected syllabus."""
        self.show_caption("List of exams by levels")

        indexed_exams_codes = {}
        for index, exam_code in enumerate(self.quiz.get_exams_codes()):
            print(f"{index + 1} -- {exam_code}")
            indexed_exams_codes.update({index + 1: exam_code})

        select_number_attempts = 1
        while select_number_attempts <= INPUT_ATTEMPTS_LIMIT:
            try:
                exam_menu_number = int(
                    input("Select exam to practice in quiz, e.g., 2: ")
                )
                return self.quiz.get_exam_by_code(indexed_exams_codes[exam_menu_number])
            except KeyError:
                select_number_attempts += 1

        if select_number_attempts > INPUT_ATTEMPTS_LIMIT:
            logger.warning(f"{RESTART_MESSAGE}")
            self.start_the_game()

    def show_syllabus_blocks(self, syllabus: LevelSyllabus):
        self.show_caption("List of exam blocks")
        for index, block in enumerate(syllabus.get_blocks_titles()):
            print(f"{index + 1} -- {block}")

    def start_the_game(self):
        # console.print("Where there is a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i].")
        self.quiz_greeting()
        self.add_player()
        self.show_syllabus_blocks(self.select_exam())
