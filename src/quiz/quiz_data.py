import pypandoc
from knowledge_base.three_levels_syllabus import (
    junior_level_syllabuses,
    intermediate_level_syllabuses,
    senior_level_syllabuses,
)

# data = pypandoc.convert_file("Mastering_Python_overview.md", to="rst")

levels_code_abstraction = {"syntax", "idioms", "design patterns", "architectural"}


syllabuses_data = [
    *junior_level_syllabuses,
    *intermediate_level_syllabuses,
    *senior_level_syllabuses,
]
