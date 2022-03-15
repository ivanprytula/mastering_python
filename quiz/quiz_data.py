# junior_level = {
#     "objectives": [
#         """The fundamentals of computer programming, i.e.:
#    how the computer works,
#    how the program is executed,
#    how the programming language is defined and constructed,
#    what the difference is between compilation and interpretation,
#    what Python is, how it is positioned among other PLs, and what distinguishes the
#    different versions of Python""",
#     ],
#     "syllabus": {
#         "name": "Basic Concepts",
#         "items": [
#
#         ]
#
#     },
# }
#
# intermediate_level = {
#     "objectives": "",
#     "syllabus": [],
# }
#
# senior_level = {
#     "objectives": "",
#     "syllabus": [],
# }

import pypandoc

certifications_levels = {
    "PCEP": "Certified Entry-Level Python Programmer",
    "PCAP": "Certified Associate in Python Programming",
    "PCPP1": "Certified Professional in Python Programming 1",
    "PCPP2": "Certified Professional in Python Programming 2",
}

data = pypandoc.convert_file("Mastering_Python_overview.md", to="rst")

print(data)


question_data = [1, 2, 3]
