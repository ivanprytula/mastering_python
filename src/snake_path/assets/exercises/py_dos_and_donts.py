# flake8: noqa
# type: ignore
# 1. Testing for equality with more than one possible value

# not-so-good-way
user_type = "regular"

if user_type == "admin" or user_type == "superadmin" or user_type == "moderator":
    give_access()

# the better way
allowed_user_types = ["admin", "superadmin", "moderator"]

if user_type in allowed_user_types:
    print("give_access")

# 2. Got lots of ‘elifs’ for your if statement? Use a dictionary!

# not-so-good-way
def show_info_about_item(chosen_item="phone"):
    if chosen_item == "phone":
        return "Handheld communication device"
    elif chosen_item == "car":
        return "Self-propelled ground vehicle"
    elif chosen_item == "dinosaur":
        return "Extinct lizard"
    else:
        return "No info available"


# the better way
def show_info_about_item(chosen_item="phone"):
    info_dict = {
        "phone": "Handheld communication device",
        "car": "Self-propelled ground vehicle",
        "dinosaur": "Extinct lizard",
    }

    return info_dict.get(chosen_item, "No info available")


# 3. Want to execute a function dynamically? Use a dictionary (again)!


def add_one(x):
    return x + 1


def divide_by_two(x):
    return x / 2


def square(x):
    return x**2


# The not-so-good way:
def perform_operation(x, chosen_operation="add_one"):
    if chosen_operation == "add_one":
        x = add_one(x)
    elif chosen_operation == "divide_by_two":
        x = divide_by_two(x)
    elif chosen_operation == "square":
        x = square(x)
    else:
        raise Exception("Invalid operation")

    return x


# the better way
def invalid_op(x):
    raise Exception("Invalid operation")


# The better way:
def perform_operation(x, chosen_operation="add_one"):
    ops = {"add_one": add_one, "divide_by_two": divide_by_two, "square": square}

    chosen_operation_function = ops.get(chosen_operation, invalid_op)

    return chosen_operation_function(x)


# Bonus: Dynamic functions with custom arguments -> dict unpacking
def user_print(user_name, user_type="regular", user_logged_in=False):
    return f"{user_name} is a(n) {user_type} user and they are {'not ' if not user_logged_in else ''}logged in."


# 1. Without dictionary unpacking:
user_print(user_name="testuser1", user_type="admin", user_logged_in=True)

# 2. With dictionary unpacking:
args = {"user_name": "testuser1", "user_type": "admin", "user_logged_in": True}
user_print(**args)


def add(x, to=1):
    return x + to


def divide(x, by=2):
    return x / by


def square(x):
    return x**2


def invalid_op(x):
    raise Exception("Invalid operation")


def perform_operation(x, chosen_operation, operation_args=None):
    # If operation_args wasn't provided (i.e. it is None), set it to be an empty dictionary
    operation_args = operation_args or {}

    ops = {"add": add, "divide": divide, "square": square}

    chosen_operation_function = ops.get(chosen_operation, invalid_op)

    return chosen_operation_function(x, **operation_args)


def example_usage():
    x = 1
    x = perform_operation(x, "add", {"to": 4})  # Adds 4
    x = perform_operation(x, "add")  # Adds 1 since that's the default for 'add'
    x = perform_operation(x, "divide", {"by": 2})  # Divides by 2
    x = perform_operation(x, "square")  # Squares the number
