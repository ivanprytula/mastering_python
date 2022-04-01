from typing import Generator


class LevelSyllabus:
    def __init__(self, data: dict) -> None:
        # def __init__(self, question: str, correct_answer: str, choices: list):
        self.syllabus_info = data
        # self.correct_answer = correct_answer
        # self.choices = choices

    def get_blocks_titles(self) -> Generator:
        # return [
        #     block["title"] for block in self.syllabus_info[self.exam_code]["blocks"]
        # ]
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
