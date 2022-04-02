from typing import Union, Optional

from question_models import LevelSyllabus


class QuizBrain:
    def __init__(self, syllabuses_data: list, levels_full_names: dict) -> None:
        self.syllabuses = syllabuses_data
        self._levels = levels_full_names
        self.question_no = 0
        self.score = 0
        # self.current_question = None

    def get_exams_codes(self) -> list[str]:
        return [syllabus.exam_code for syllabus in self.syllabuses]

    def get_exams_statuses(self) -> list[str]:
        return [syllabus.get_block_status() for syllabus in self.syllabuses]

    def get_exam_by_code(self, exam_code: str) -> Optional[LevelSyllabus]:
        for syllabus in self.syllabuses:
            if exam_code == syllabus.exam_code:
                return syllabus

    def get_exams_levels_full_names(self) -> list:
        return [self._levels[exam_code]["full_name"] for exam_code in self._levels]
