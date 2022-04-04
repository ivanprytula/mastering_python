class TestLevelSyllabus:
    # def setup(self, example_syllabus_data):
    #     self.syllabus = LevelSyllabus(example_syllabus_data)

    def test_blocks_titles(self, syllabus):
        assert "Basic Concepts" in syllabus.get_blocks_titles()

    def test_block_items(self, syllabus):
        print(syllabus.get_block_items("Basic Concepts"))
        assert "description/keywords" in syllabus.get_block_items("Basic Concepts")

    def test_block_status(self, syllabus):
        assert syllabus.get_block_status()

    def test_exam_code(self, syllabus):
        assert "PCEP-30-01" == syllabus.exam_code
