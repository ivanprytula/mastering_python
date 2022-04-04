import logging
import sys
from typing import Union, Iterable, Optional

from rich.console import Console
from rich.theme import Theme
from rich.syntax import Syntax

from question_models import LevelSyllabus
from quiz_brain import QuizBrain

INPUT_ATTEMPTS_LIMIT = 3
RESTART_MESSAGE = "You have used all your attempts to enter.\nGame is restarting..."
AFFIRMATIVE_RESPONSES = ("y", "yes")
NEGATIVE_RESPONSES = ("n", "no")
QUIT_RESPONSES = ("q", "quit")
YES_NO_QUESTION_SUFFIX = "yes|y / no|n"

logger = logging.getLogger(__name__)

custom_theme = Theme(
    {
        "h1": "bold blue",
        "h2": "bold italic yellow",
        "h3": "bold green",
        "h4": "bold gold3",
        "info": "bold navajo_white1",
        "question": "italic light_steel_blue1",
        "warning": "magenta",
        "danger": "bold red",
        "as_list": "bold green4",
        "quit_quiz": "bold dark_olive_green1",
    }
)
console = Console(theme=custom_theme)

PYTHON_ASCII_LOGO_BANNER_SHADOW = """
        ██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗
        ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║
        ██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║
        ██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║
        ██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║
        ╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
"""

my_code = '''
def iter_first_last(values: Iterable[T]) -> Iterable[Tuple[bool, bool, T]]:
    """Iterate and generate a tuple with a flag for first and last value."""
    iter_values = iter(values)
    try:
        previous_value = next(iter_values)
    except StopIteration:
        return
    first = True
    for value in iter_values:
        yield first, False, previous_value
        first = False
        previous_value = value
    yield first, True, previous_value
'''
syntax = Syntax(my_code, "python", theme="monokai", line_numbers=True)


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain

    @staticmethod
    def _horizontal_chars_deliminator(character: str, length_limit: int) -> None:
        for _ in range(0, length_limit + 10):
            console.print(rf"{character}", end="")

    def _go_to_game_respawn(self, attempts_quantity: int) -> None:
        if attempts_quantity > INPUT_ATTEMPTS_LIMIT:
            console.print(f"{RESTART_MESSAGE}", style="danger")
            self.start_the_game()

    @staticmethod
    def show_headline(
        text: str,
        line_starts_with: str = "-->",
        line_ends_with: str = "<--",
        style_as: str = None,
    ) -> None:
        console.print(f"\n{line_starts_with} {text} {line_ends_with}", style=style_as)

    def quiz_greeting(self) -> None:
        greeting = "Welcome to the quiz!"
        self.show_headline(greeting, style_as="h1")
        self._horizontal_chars_deliminator("~", len(greeting))
        self.show_headline(PYTHON_ASCII_LOGO_BANNER_SHADOW, "", "")

    @staticmethod
    def input_request(question: str, return_as_type: type = str) -> Union[str, int]:
        console.print(f"\n{question}")
        input_answer = console.input(">>> ")
        if return_as_type is int:
            if not input_answer:
                input_answer = 1
            return int(input_answer)
        else:
            return input_answer

    @staticmethod
    def show_as_list(
        items: Iterable, style_as: str, is_numbered: bool = True, separator: str = "--"
    ) -> None:
        for index, item in enumerate(items):
            if is_numbered:
                console.print(f"{index + 1} {separator} {item}", style=style_as)
            else:
                console.print(f" ^ {item}", style=style_as)

    def add_player(self) -> None:
        enter_name_attempts = 1
        while enter_name_attempts <= INPUT_ATTEMPTS_LIMIT:
            try:
                new_player: Union[str, int] = self.input_request(
                    "What's your name? Press Enter to stay anonymous."
                )

                if not new_player:
                    new_player = "Anonymous"
                elif not new_player.isalpha():  # type: ignore[union-attr]
                    raise ValueError(
                        "Player name must be string, not numeric or special "
                        "characters."
                    )

                self.show_headline(f"{new_player}, you are in the Game!", "", "", "h3")
                break
            except ValueError:
                enter_name_attempts += 1
                console.log(
                    "Player name must be string, not numeric or special characters.",
                    style="warning",
                )
        else:
            self._go_to_game_respawn(enter_name_attempts)

    def select_exam(self) -> Optional[LevelSyllabus]:
        """Returns instance of selected syllabus."""
        self.show_headline("List of exams by levels", style_as="h2")

        indexed_exams_codes = {}
        for index, exam_code in enumerate(self.quiz.get_exams_codes()):
            indexed_exams_codes.update({index + 1: exam_code})

        self.show_as_list(self.quiz.get_exams_codes(), "as_list")

        # show full names of exams as note below
        self._horizontal_chars_deliminator("*", 1)
        console.line(1)
        self.show_as_list(self.quiz.get_exams_levels_full_names(), "", False)

        selection_attempts = 1
        while selection_attempts <= INPUT_ATTEMPTS_LIMIT:
            try:
                console.print()
                exam_menu_number = self.input_request(
                    "Select exam to test your knowledge. Press Enter for default 1.",
                    int,
                )
                return self.quiz.get_exam_by_code(indexed_exams_codes[exam_menu_number])
            except KeyError:
                selection_attempts += 1
                console.log(
                    f"Enter number ONLY in range {min(indexed_exams_codes.keys())} "
                    f"... {max(indexed_exams_codes.keys())}",
                    style="warning",
                )
            except ValueError:
                selection_attempts += 1
                console.log("You must enter ONLY numbers.", style="warning")

        self._go_to_game_respawn(selection_attempts)
        return None

    def show_questions_menu(self, syllabus: LevelSyllabus) -> None:
        self.show_headline("Quiz begins!".upper(), "#!/usr/bin/python3", "", "info")
        self.show_headline("Explain the following questions/stuff:", "", "")

        for block_title in syllabus.get_blocks_titles():
            # console.line(2)
            self.show_headline(block_title, "==", "==", "h4")

            for block_item in syllabus.get_block_items(block_title):
                console.print(f"\n{block_item}", style="question")
                self.quiz.question_no += 1

                user_response = self.input_request(
                    f"Next question, skip this block or quit? "
                    f" {YES_NO_QUESTION_SUFFIX} / quit|q?"
                )
                if user_response in AFFIRMATIVE_RESPONSES:
                    continue
                elif user_response in NEGATIVE_RESPONSES:
                    break
                elif user_response in QUIT_RESPONSES:
                    self.show_headline("Oh, no...bye-bye!", ":((", "://", "warning")
                    self.finish_quiz()
                else:
                    console.log(
                        "Unknown character. Quiz turns to next question",
                        style="warning",
                    )
            else:
                console.print(
                    "You have reached last question in this block.",
                    style="bright_white italic",
                )
        self.finish_quiz()

    def finish_quiz(self) -> None:
        self.show_headline(
            f"You tried to answer to {self.quiz.question_no} questions.",
            "@@",
            "@@",
            style_as="quit_quiz",
        )
        sys.exit(0)

    def start_practicing(self, syllabus: LevelSyllabus) -> None:
        user_response = self.input_request(
            f"Show questions by blocks/topics? {YES_NO_QUESTION_SUFFIX}"
        )
        if user_response in AFFIRMATIVE_RESPONSES:

            preview_answer = self.input_request(
                f"Do you want to preview content of all blocks before quiz begins? "
                f"{YES_NO_QUESTION_SUFFIX}"
            )

            if preview_answer in AFFIRMATIVE_RESPONSES:
                with console.pager(styles=True):
                    for block_title in syllabus.get_blocks_titles():
                        self.show_headline(f'Content of "{block_title}"', style_as="h2")
                        self.show_as_list(
                            syllabus.get_block_items(block_title), "as_list"
                        )

            self.show_questions_menu(syllabus)
        else:
            self.show_headline("Oh, no...bye-bye!", ":((", "://", "warning")
            sys.exit(0)

    def show_syllabus_blocks(self, syllabus: LevelSyllabus) -> None:
        self.show_headline(f"List of {syllabus.exam_code} blocks", style_as="h2")
        self.show_as_list(syllabus.get_blocks_titles(), "as_list")
        self.start_practicing(syllabus)

    def start_the_game(self) -> None:
        # console.print(syntax)

        self.quiz_greeting()
        self.add_player()
        self.show_syllabus_blocks(self.select_exam())
