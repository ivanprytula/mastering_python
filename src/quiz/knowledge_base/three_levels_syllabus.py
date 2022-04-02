certifications_levels_desc: dict[str, dict] = {
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
                        "lists in detail: indexing, slicing, basic methods (**append("
                        "), insert(), index()**) and functions (**len(), sorted()**, "
                        "etc.), **del** instruction, iterating lists with the **for** "
                        "loop, initializing, **in** and **not** in operators, "
                        "list comprehension, copying and cloning",
                        "lists in lists: matrices and cubes",
                        "tuples: indexing, slicing, building, immutability",
                        "tuples vs. lists: similarities and differences, lists inside "
                        "tuples and tuples inside lists",
                        "dictionaries: building, indexing, adding and removing keys, "
                        "iterating through dictionaries as well as their keys and "
                        "values, checking key existence, **keys(), items()** and "
                        "**values()** methods",
                        "strings in detail: escaping using the '' character, "
                        "quotes and apostrophes inside strings,; multi-line strings, "
                        "basic string functions",
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
                        "converting generator objects into lists using the **list()** "
                        "function",
                        "name scopes, name hiding (shadowing), the **global** keyword",
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
                    "items": [
                        "PCEP 1.1 Understand fundamental terms and definitions - "
                        "interpreting and the interpreter, compilation and the "
                        "compiler, lexis, syntax and semantics",
                        "PCEP 1.2 Understand Python’s logic and structure - keywords, "
                        "instructions, indenting, comments",
                        "PCEP 1.3 Introduce literals and variables into code and use "
                        "different numeral systems - Boolean, integers, "
                        "floating-point numbers, scientific notation, strings, "
                        "binary, octal, decimal, and hexadecimal numeral system, "
                        "variables, naming conventions, implementing PEP-8 "
                        "recommendations",
                        "PCEP 1.4 Choose operators and data types adequate to the "
                        "problem - numeric operators: ** * / % // + –, "
                        "string operators: * +, assignments and shortcut operators, "
                        "operators: unary and binary, priorities and binding, "
                        "bitwise operators: ~ & ^ | << >>, Boolean operators: not and "
                        "or, Boolean expressions, relational operators ( == != > >= < "
                        "<= ), the accuracy of floating-point numbers, type casting",
                        "PCEP 1.5 Perform Input/Output console operations - print(), "
                        "input() functions, sep= and end= keyword parameters, "
                        "int() and float() functions",
                    ],
                },
                {
                    "order": 2,
                    "title": "Control Flow – Conditional Blocks and Loops",
                    "items": [
                        "PCEP 2.1 Make decisions and branch the flow with the if "
                        "instruction - conditional statements: if, if-else, if-elif, "
                        "if-elif-else, multiple conditional statements, nesting "
                        "conditional statements",
                        "PCEP 2.2 Perform different types of iterations - the *pass* "
                        "instruction, building loops with while, for, range(), "
                        "and in; iterating through sequences, expanding loops with "
                        "while-else and for-else, nesting loops and conditional "
                        "statements, controlling loop execution with break and "
                        "continue",
                    ],
                },
                {
                    "order": 3,
                    "title": "Data Collections – Tuples, Dictionaries, Lists, "
                    "and Strings",
                    "items": [
                        "PCEP 3.1 Collect and process data using lists - constructing "
                        "vectors, indexing and slicing, the len() function, "
                        "basic list methods (append(), insert(), index()) and "
                        "functions (len(), sorted(), etc.), the del instruction; "
                        "iterating through lists with the for loop, initializing "
                        "loops; in and not in operators, list comprehensions; copying "
                        "and cloning, lists in lists: matrices and cubes",
                        "PCEP 3.2 Collect and process data using tuples - tuples: "
                        "indexing, slicing, building, immutability; tuples vs. lists: "
                        "similarities and differences, lists inside tuples and tuples "
                        "inside lists",
                        "PCEP 3.3 Collect and process data using dictionaries - "
                        "dictionaries: building, indexing, adding and removing keys; "
                        "iterating through dictionaries and their keys and values, "
                        "checking the existence of keys; keys(), items() and values() "
                        "methods",
                        "PCEP 3.4 Operate with strings - constructing strings, "
                        r"indexing, slicing, immutability; escaping using the \ "
                        r"character; quotes and apostrophes inside strings, "
                        r"multi-line strings, basic string functions and methods",
                    ],
                },
                {
                    "order": 4,
                    "title": "Functions and Exceptions",
                    "items": [
                        "PCEP 4.1 Decompose the code using functions - defining and "
                        "invoking user-defined functions and generators; the return "
                        "keyword, returning results, the None keyword, recursion",
                        "PCEP 4.2 Organize interaction between the function and its "
                        "environment - parameters vs. arguments; positional, keyword and "
                        "mixed argument passing; default parameter values, name scopes, "
                        "name hiding (shadowing), the global keyword",
                        "PCEP 4.3 Python Built-In Exceptions Hierarchy - BaseException, "
                        "Exception, SystemExit, KeyboardInterrupt, abstractive "
                        "exceptions, ArithmeticError, LookupError along with IndexError "
                        "and KeyError; TypeError and ValueError exceptions, "
                        "the AssertError exception along with the assert keyword",
                        "PCEP 4.4 Basics of Python Exception Handling - try-except, "
                        "try-except Exception, ordering the except branches, propagating "
                        "exceptions through function boundaries; delegating "
                        "responsibility for handling exceptions",
                    ],
                },
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
                        "literals: Boolean, integer, floating-point numbers, "
                        "scientific notation, strings",
                        "operators: unary and binary, priorities and binding",
                        "numeric operators: ** * / % // + –",
                        "bitwise operators: ~ & ^ | << >>",
                        "string operators: * +",
                        "Boolean operators: **not and or**",
                        "relational operators ( == != > >= < <= ), building complex "
                        "Boolean expressions",
                        "assignments and shortcut operators",
                        "accuracy of floating-point numbers",
                        "basic input and output: **input(), print(), int(), float(), "
                        "str()** functions",
                        "formatting **print()** output with **end=** and **sep=** "
                        "arguments",
                        "conditional statements: **if, if-else, if-elif, "
                        "if-elif-else**",
                        "the **pass** instruction",
                        "simple lists: constructing vectors, indexing and slicing, "
                        "the **len()** function",
                        "simple strings: constructing, assigning, indexing, slicing "
                        "comparing, immutability",
                        "building loops: **while, for, range(), in**, iterating "
                        "through sequences",
                        "expanding loops: **while-else, for-else**, nesting loops and "
                        "conditional statements",
                        "controlling loop execution: **break, continue**",
                    ],
                },
                {
                    "oder": 2,
                    "title": "Data Aggregates",
                    "items": [
                        "strings in detail: ASCII, UNICODE, UTF-8, immutability, "
                        r"escaping using the '\' character, quotes and apostrophes "
                        r"inside strings, multiline strings, copying vs. cloning, "
                        r"advanced slicing, string vs. string, string vs. non-string, "
                        r"basic string methods (**upper(), lower(), isxxx(), "
                        r"capitalize(), split(), join()**, etc.) and functions (len("
                        r"), chr(), ord()), escape characters",
                        "lists in detail: indexing, slicing, basic methods (**append("
                        "), insert(), index()**) and functions (**len(), sorted()**, "
                        "etc.), **del** instruction, iterating lists with the **for** "
                        "loop, initializing, **in** and **not in** operators, "
                        "list comprehension, copying and cloning",
                        "lists in lists: matrices and cubes",
                        "tuples: indexing, slicing, building, immutability",
                        "tuples vs. lists: similarities and differences, lists inside "
                        "tuples and tuples inside lists",
                        "dictionaries: building, indexing, adding and removing keys, "
                        "iterating through dictionaries as well as their keys and "
                        "values, checking key existence, **keys(), items()** and "
                        "**values()** methods",
                    ],
                },
                {
                    "oder": 3,
                    "title": "Functions and Modules",
                    "items": [
                        "defining and invoking your own functions and generators",
                        "**return** and **yield** keywords, returning results, "
                        "the **None** keyword, recursion",
                        "parameters vs. arguments, positional keyword and mixed "
                        "argument passing, default parameter values",
                        "converting generator objects into lists using the **list()** "
                        "function",
                        "name scopes, name hiding (shadowing), the **global** keyword",
                        "**lambda** functions, defining and using **map(), filter(), "
                        "reduce(), reversed(), sorted()** functions, and the **sort("
                        ")** method",
                        "the **if** operator",
                        "import directives, qualifying entities with module names, "
                        "initializing modules",
                        r"writing and using modules, the **\__name\__** variable",
                        "**pyc** file creation and usage",
                        r"constructing and distributing packages, packages vs. "
                        r"directories, the role of the **\__init\__.py** file",
                        "hiding module entities",
                        "Python hashbang, using multiline strings as module "
                        "documentation",
                    ],
                },
                {
                    "oder": 4,
                    "title": "Classes, Objects, and Exceptions",
                    "items": [
                        "defining your own classes, superclasses, subclasses, "
                        "inheritance, searching for missing class components, "
                        "creating objects",
                        "class attributes: class variables and instance variables, "
                        "defining, adding and removing attributes, explicit "
                        "constructor invocation",
                        "class methods: defining and using, the **self** parameter "
                        "meaning and usage",
                        "inheritance and overriding, finding class/object components",
                        "single inheritance vs. multiple inheritance",
                        "name mangling",
                        "invoking methods, passing and using the **self** "
                        "argument/parameter",
                        r"the **\__init\__** method",
                        r"the role of the **\__str\__** method",
                        r"introspection: **\__dict\__**, **\__name\__**, "
                        r"**\__module\__**, **\__bases\__** properties, examining "
                        r"class/object structure",
                        "writing and using constructors",
                        "**hasattr(), type(), issubclass(), isinstance(), super()** "
                        "functions",
                        "using predefined exceptions and defining your own ones",
                        "the **try-except-else-finally** block, the **raise** "
                        "statement, the **except-as** variant",
                        "exceptions hierarchy, assigning more than one exception to "
                        "one **except** branch",
                        "adding your own exceptions to an existing hierarchy",
                        "assertions",
                        "the anatomy of an exception object",
                        "input/output basics: opening files with the **open()** "
                        "function, stream objects, binary vs. text files, newline "
                        "character translation, reading and writing files, "
                        "**bytearray** objects",
                        "**read(), readinto(), readline(), write(), close()** methods",
                    ],
                },
            ],
        }
    },
    {
        "PCAP-31-03": {
            "status": "(PVTCs, OnVUE)",
            "blocks": [
                {
                    "order": 1,
                    "title": "Modules and Packages",
                    "items": [
                        "import variants; advanced qualifying for nested modules",
                        "dir(); sys.path variable",
                        "math: ceil(), floor(), trunc(), factorial(), hypot(), sqrt(); "
                        "random: random(), seed(), choice(), sample()",
                        "platform: platform(), machine(), processor(), system(), version("
                        "), python_implementation(), python_version_tuple()",
                        "idea, __pycache__, __name__, public variables, __init__.py",
                        "searching for modules/packages; nested packages vs directory tree",
                    ],
                },
                {
                    "order": 2,
                    "title": "Exceptions",
                    "items": [
                        "except, except:-except; except:-else:, except (e1,e2)",
                        "the hierarchy of exceptions",
                        "raise, raise ex, assert",
                        "event classes, except E as e, arg property",
                        "self-defined exceptions, defining and using",
                    ],
                },
                {
                    "order": 3,
                    "title": "Strings",
                    "items": [
                        "ASCII, UNICODE, UTF-8, codepoints, escape sequences",
                        "ord(), chr(), literals",
                        "indexing, slicing, immutability",
                        "iterating through,",
                        "concatenating, multiplying, comparing (against strings and "
                        "numbers)",
                        "in, not in",
                        ".isxxx(), .join(), .split()",
                        ".sort(), sorted(), .index(), .find(), .rfind()",
                    ],
                },
                {
                    "order": 4,
                    "title": "Object-Oriented Programming",
                    "items": [
                        "ideas: class, object, property, method, encapsulation, "
                        "inheritance, grammar vs class, superclass, subclass",
                        "instance vs class variables: declaring, initializing",
                        "__dict__ property (objects vs classes)",
                        "private components (instance vs classes), name mangling",
                        "methods: declaring, using, self parameter",
                        "instrospection: hasattr() (objects vs classes), __name__, "
                        "__module__, __bases__ properties",
                        "inheritance: single, multiple, isinstance(), overriding, "
                        "not is and is operators",
                        "inheritance: single, multiple, isinstance(), overriding, "
                        "not is and is operators",
                        "constructors: declaring and invoking",
                        "polymorphism",
                        "__name__, __module__, __bases__ properties, __str__() method",
                        "multiple inheritance, diamonds",
                    ],
                },
                {
                    "order": 5,
                    "title": "Miscellaneous (List Comprehensions, Lambdas, Closures, "
                    "and I/O Operations)",
                    "items": [
                        "list comprehension: if operator, using list comprehensions",
                        "lambdas: defining and using lambdas, self-defined functions "
                        "taking lambda as as arguments; map(), filter();",
                        "closures: meaning, defining, and using closures",
                        "I/O Operations: I/O modes, predefined streams, handles; "
                        "text/binary modes",
                        "open(), errno and its values; close()",
                        ".read(), .write(), .readline(); readlines() (along with "
                        "bytearray())",
                    ],
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
                    "items": [
                        "Classes, Instances, Attributes, Methods;",
                        "Working with class and instance data;",
                        "Copying object data using _shallow_ and _deep_ operations;",
                        "Inheritance and Polymorphism;",
                        "Different faces of Python methods: _static_ and _class_ methods;",
                        "Abstract classes vs. method overloading;",
                        "Composition vs. Inheritance – two ways to the same destination;",
                        "Implementing Core Syntax;",
                        "Subclassing built-ins;",
                        "Attribute Encapsulation;",
                        "Advanced techniques of creating and serving exceptions;",
                        "Serialization of Python objects using the _pickle_ module;",
                        "Making Python object persistent using the _shelve_ module;",
                        "Metaprogramming (function decorators, class decorators, metaclasses.)",
                    ],
                },
                {
                    "oder": 2,
                    "title": "Python Enhancement Proposals (PEP)",
                    "items": [
                        "What is PEP?",
                        "Coding conventions – not only style and naming;",
                        "_PEP 20_ – The Zen of Python: a collection of principles that influences the design of Python code;",
                        "_PEP 8_ – Style Guide for Python Code: coding conventions for code comprising the STL in the main Python distribution;",
                        "_PEP 257_ – Docstring Conventions: what is _docstring_, and some semantics as well as conventions associated with them;",
                        "A tour of other important PEPs.",
                    ],
                },
                {
                    "oder": 3,
                    "title": "GUI Programming",
                    "items": [
                        "What is GUI and where it comes from;",
                        "Constructing a GUI – basic blocks and conventions;",
                        "Event-driven programming;",
                        "Popular GUI environments and toolkits;",
                        "_tkinter_  Python interface to Tcl/Tk ( tkinter’s application life cycle; widgets, windows and events; sample applications)",
                        "_pygame_ – a simple way of developing multimedia applications.",
                    ],
                },
                {
                    "oder": 4,
                    "title": "The Elements of Network Programming: Working with "
                    "RESTful APIs",
                    "items": [
                        "the basic concepts of network programming, REST, network sockets, and client-server communication;",
                        "How to use and create sockets in Python;",
                        "how to establish and close the connection with a server;",
                        "JSON and XML files, and how they can be used in network communication;",
                        "HTTP methods, and how to say anything in HTTP;",
                        "How to build a sample testing environment;",
                        "CRUD;",
                        "How to build a simple REST client;",
                        "how to fetch and remove data from servers;",
                        "how to add new data to servers and update the already-existing data.",
                    ],
                },
                {
                    "oder": 5,
                    "title": "File Processing and Communicating with a Program’s "
                    "Environment",
                    "items": [
                        "Processing files:_sqlite3_ – interacting with SQLite databases; _xml_ – creating and processing XML files; _csv_ – CSV file reading and writing; _logging_ – basics logging facility for Python; _configparser_ – configuration file parser.",
                        "Communicating with a program’s environment: _os_ – interacting with the operating system; _datetime_ – manipulating with dates and time; _io_ – working with streams; _time_ – time access and conversions.",
                    ],
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
                    "items": [
                        "Using _pip_",
                        "Basic directory structure",
                        "The _setup.py_ file",
                        "Sharing, storing, and installing packages",
                        "Documentation",
                        "License",
                        "Testing principles and techniques: - **unittest** – Unit "
                        "testing framework; **Pytest** – framework to write tests",
                    ],
                },
                {
                    "oder": 2,
                    "title": "Design Patterns",
                    "items": [
                        "Object-oriented design principles and the concept of design patterns",
                        "The _Singleton_ Design Pattern",
                        "The _Factory_ Pattern",
                        "The _Façade_ Pattern",
                        "The _Proxy_ Pattern",
                        "The _Observer_ Pattern",
                        "The _Command_ Pattern",
                        "The _Template Method_ Pattern",
                        "Model-View-Controller",
                        "The _State Design_ Pattern",
                    ],
                },
                {
                    "oder": 3,
                    "title": "Interprocess Communication",
                    "items": [
                        "multiprocessing — Process-based parallelism",
                        "threading — Thread-based parallelism",
                        "subprocess — Subprocess management",
                        "Multiprocess synchronisation: **queue** — A synchronized "
                        "queue class; **socket** — Low-level networking interface; "
                        "**mmap** — Memory-mapped file support",
                    ],
                },
                {
                    "oder": 4,
                    "title": "Python Network Programming",
                    "items": [
                        "Python Socket Module: Introduction to sockets; Server Socket Methods; Client socket methods; General socket methods; Client-Server vs. Peer-to-peer; Other Internet modules"
                    ],
                },
                {
                    "oder": 5,
                    "title": "Python-MySQL Database Access",
                    "items": [
                        "Relational databases – fundamental principles and how to work with them",
                        "MySQL vs. rest of the world",
                        "**CRUD** Application: db connection, db create, db insert, "
                        "db read, db update, db delete,",
                    ],
                },
            ],
        }
    },
]
