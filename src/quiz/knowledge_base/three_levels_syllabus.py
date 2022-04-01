certifications_levels: dict[str, dict] = {
    "PCEP": {
        "full_name": "Certified Entry-Level Python Programmer",
        "codes": ["PCEP-30-01", "PCEP-30-02"],
    },
    "PCAP": {
        "full_name": "Certified Associate in Python Programming",
        "codes": ["PCAP-31-02", "PCAP-31-03"],
    },
    "PCPP1": {
        "full_name": "Certified Professional in Python Programming 1",
        "codes": ["PCPP-32-101"],
    },
    "PCPP2": {
        "full_name": "Certified Professional in Python Programming 2",
        "codes": ["PCPP-32-201"],
    },
}

template_level_syllabus: list[dict] = [
    {
        "PCEP-30-0x": {
            "status": "...",
            "blocks": [{"oder": 1, "title": "...", "items": ["description/keywords"]}],
        }
    }
]

junior_level_syllabuses = [
    {
        "PCEP-30-01": {
            "status": "Retiring December 31, 2022",
            "blocks": [
                {
                    "oder": 1,
                    "title": "Basic Concepts",
                    "items": [
                        "fundamental concepts: interpreting and the interpreter, "
                        "compilation and the compiler",
                        "literals: Boolean, integer, floating-point numbers, "
                        "scientific notation, strings",
                        "comments, inline comments",
                        "the **print()** function",
                        "the **input()** function",
                        "numeral systems (binary, octal, decimal, hexadecimal)",
                        "numeric operators: ** * / % // + –",
                        "string operators: * +",
                        "assignments and shortcut operators",
                    ],
                },
                {
                    "oder": 2,
                    "title": "Data Types, Evaluations, and Basic I/O Operations",
                    "items": [
                        "operators: unary and binary, priorities and binding",
                        "bitwise operators: ~ & ^ | << >>",
                        "Boolean operators: **not and or**",
                        "Boolean expressions",
                        "relational operators ( == != > >= < <= ), building complex "
                        "Boolean expressions",
                        "accuracy of floating-point numbers",
                        "basic input and output operations using the **input(), "
                        "print(), int(), float(), str(), len()** functions",
                        "formatting **print()** output with **end=** and **sep=** "
                        "arguments",
                        "type casting",
                        "basic calculations",
                        "simple strings: constructing, assigning, indexing, "
                        "immutability",
                    ],
                },
                {
                    "oder": 3,
                    "title": "Control Flow – loops and conditional blocks",
                    "items": [
                        "conditional statements: **if, if-else, if-elif, "
                        "if-elif-else**",
                        "multiple conditional statements",
                        "the **pass** instruction",
                        "building loops: **while, for, range(), in**",
                        "iterating through sequences",
                        "expanding loops: **while-else, for-else**",
                        "nesting loops and conditional statements",
                        "controlling loop execution: **break, continue**",
                    ],
                },
                {
                    "oder": 4,
                    "title": "Data Collections – Lists, Tuples, and Dictionaries",
                    "items": [
                        "simple lists: constructing vectors, indexing and slicing, "
                        "the **len()** function",
                        "lists in detail: indexing, slicing, basic methods ("
                        "**append("
                        "), "
                        "insert(), index()**) and functions (**len(), sorted()**, "
                        "etc.), "
                        "**del** instruction, iterating lists with the **for** "
                        "loop, "
                        "initializing, **in** and **not** in operators, "
                        "list comprehension, copying and cloning",
                        "lists in lists: matrices and cubes",
                        "tuples: indexing, slicing, building, immutability",
                        "tuples vs. lists: similarities and differences, "
                        "lists inside "
                        "tuples and tuples inside lists",
                        "dictionaries: building, indexing, adding and removing "
                        "keys, "
                        "iterating through dictionaries as well as their keys and "
                        "values, "
                        "checking key existence, **keys(), items()** and "
                        "**values()** "
                        "methods",
                        "strings in detail: escaping using the '' character, "
                        "quotes and "
                        "apostrophes inside strings,; multi-line strings, "
                        "basic string "
                        "functions",
                    ],
                },
                {
                    "oder": 5,
                    "title": "Functions",
                    "items": [
                        "defining and invoking your own functions and generators",
                        "**return** and **yield** keywords, returning results,",
                        "the **None** keyword,",
                        "recursion",
                        "parameters vs. arguments,",
                        "positional keyword and mixed argument passing,",
                        "default parameter values",
                        "converting generator objects into lists using the "
                        "**list()** "
                        "function",
                        "name scopes, name hiding (shadowing), the **global** "
                        "keyword",
                    ],
                },
            ],
        }
    },
    {
        "PCEP-30-02": {
            "status": "Active",
            "blocks": [
                {
                    "order": 1,
                    "title": "Computer Programming and Python Fundamentals",
                    "items": [],
                },
                {
                    "order": 2,
                    "title": "Control Flow – Conditional Blocks and Loops",
                    "items": [],
                },
                {
                    "order": 3,
                    "title": "Data Collections – Tuples, Dictionaries, Lists, "
                    "and Strings",
                    "items": [],
                },
                {"order": 4, "title": "Functions and Exceptions", "items": []},
            ],
        }
    },
]

intermediate_level_syllabuses = [
    {
        "PCAP-31-02": {
            "status": "Active PVTCs",
            "blocks": [
                {
                    "oder": 1,
                    "title": "Control and Evaluations",
                    "items": [
                        "basic concepts: interpreting and the interpreter, "
                        "compilation and the compiler, language elements, lexis, "
                        "syntax and semantics, Python keywords, instructions, "
                        "indenting",
                        "short desc/keywords",
                        "short desc/keywords",
                        "short desc/keywords",
                    ],
                },
                {
                    "oder": 2,
                    "title": "Data Aggregates",
                    "items": [
                        "basic concepts: interpreting and the interpreter, "
                        "compilation and the compiler, language elements, lexis, "
                        "syntax and semantics, Python keywords, instructions, "
                        "indenting",
                        "short desc/keywords",
                        "short desc/keywords",
                        "short desc/keywords",
                    ],
                },
                {
                    "oder": 3,
                    "title": "Functions and Modules",
                    "items": [
                        "basic concepts: interpreting and the interpreter, "
                        "compilation and the compiler, language elements, lexis, "
                        "syntax and semantics, Python keywords, instructions, "
                        "indenting",
                        "short desc/keywords",
                        "short desc/keywords",
                        "short desc/keywords",
                    ],
                },
                {
                    "oder": 4,
                    "title": "Classes, Objects, and Exceptions",
                    "items": [
                        "basic concepts: interpreting and the interpreter, "
                        "compilation and the compiler, language elements, lexis, "
                        "syntax and semantics, Python keywords, instructions, "
                        "indenting",
                        "short desc/keywords",
                        "short desc/keywords",
                        "short desc/keywords",
                    ],
                },
            ],
        }
    },
    {
        "PCAP-31-03": {
            "status": "(PVTCs, OnVUE)",
            "blocks": [
                {"order": 1, "title": "Modules and Packages", "items": []},
                {"order": 2, "title": "Modules and Packages", "items": []},
                {"order": 3, "title": "Exceptions", "items": []},
                {"order": 4, "title": "Object-Oriented Programming", "items": []},
                {
                    "order": 5,
                    "title": "Miscellaneous (List Comprehensions, Lambdas, Closures, "
                    "and I/O Operations)",
                    "items": [],
                },
            ],
        }
    },
]

senior_level_syllabuses = [
    {
        "PCPP-32-101": {
            "status": "Active",
            "blocks": [
                {
                    "oder": 1,
                    "title": "Advanced Perspective of Classes and OOP in Python",
                    "items": ["short desc/keywords"],
                },
                {
                    "oder": 2,
                    "title": "Python Enhancement Proposals (PEP)",
                    "items": ["short desc/keywords"],
                },
                {
                    "oder": 3,
                    "title": "GUI Programming",
                    "items": ["short desc/keywords"],
                },
                {
                    "oder": 4,
                    "title": "The Elements of Network Programming: Working with "
                    "RESTful APIs",
                    "items": ["short desc/keywords"],
                },
                {
                    "oder": 5,
                    "title": "File Processing and Communicating with a Program’s "
                    "Environment",
                    "items": ["short desc/keywords"],
                },
            ],
        }
    },
    {
        "PCPP-32-201": {
            "status": "Active",
            "blocks": [
                {
                    "oder": 1,
                    "title": "Creating and Distributing Packages",
                    "items": ["short desc/keywords"],
                },
                {
                    "oder": 2,
                    "title": "Design Patterns",
                    "items": ["short desc/keywords"],
                },
                {
                    "oder": 3,
                    "title": "Interprocess Communication",
                    "items": ["short desc/keywords"],
                },
                {
                    "oder": 4,
                    "title": "Python Network Programming",
                    "items": ["short desc/keywords"],
                },
                {
                    "oder": 5,
                    "title": "Python-MySQL Database Access",
                    "items": ["short desc/keywords"],
                },
            ],
        }
    },
]
