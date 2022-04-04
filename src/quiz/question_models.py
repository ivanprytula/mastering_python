from typing import Generator
from knowledge_base.exercises import *
from knowledge_base.idioms import *


class LevelSyllabus:
    def __init__(self, data: dict) -> None:
        self.syllabus_info = data

    def get_blocks_titles(self) -> Generator:
        for block in self.syllabus_info[self.exam_code]["blocks"]:
            yield block["title"]

    def get_block_items(self, block_title: str) -> list:
        return [
            block["items"]
            for block in self.syllabus_info[self.exam_code]["blocks"]
            if block_title == block["title"]
        ][0]

    def get_block_status(self) -> str:
        return self.syllabus_info[self.exam_code].get("status")

    @property
    def exam_code(self) -> str:
        return list(self.syllabus_info.keys())[0]


class Exercise:
    """Represents examples of: code block, expression, keyword, idioms, etc."""
