# conftest.py #3
"""
chat tests would have access to fixtures in tests/conftest.py #1 and
quiz_tests/conftest.py #3
"""
from pytest import fixture
from src.quiz.question_models import LevelSyllabus


@fixture(scope="class")
def syllabus() -> LevelSyllabus:
    template_level_syllabus = {
        "PCEP-30-01": {
            "status": "Active",
            "blocks": [
                {
                    "oder": 1,
                    "title": "Basic Concepts",
                    "items": ["description/keywords", "description 2/keywords 2"],
                }
            ],
        }
    }
    return LevelSyllabus(template_level_syllabus)
