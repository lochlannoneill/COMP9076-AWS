def read_input(prompt, validation_func, error_message):
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        else:
            print(error_message)

def read_nonempty_string(prompt):
    return read_input(
        prompt, 
        lambda s: len(s.replace(' ', '')) > 0, 
        "Please type letters only"
    )

def read_nonempty_alphabetical_string(prompt):
    return read_input(
        prompt, 
        lambda s: len(s) > 0 and s.replace(" ", "").isalpha(), 
        "Letters only please..."
    )

def read_integer(prompt):
    return int(read_input(
        prompt, 
        lambda s: s.isdigit() or (s.startswith('-') and s[1:].isdigit()), 
        "Must be numeric..."
    ))

def read_positive_integer(prompt):
    while True:
        number = read_integer(prompt)
        if number > 0:
            return number
        print("Number must be positive")

def read_nonnegative_integer(prompt):
    while True:
        number = read_integer(prompt)
        if number >= 0:
            return number
        print("Non-negative numbers please...")

def read_range_integer(prompt, min_range, max_range):
    while True:
        number = read_integer(prompt)
        if min_range <= number <= max_range:
            return number
        print("Values out of range...please try again...")

def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Must be numeric...")

def read_nonnegative_float(prompt):
    while True:
        number = read_float(prompt)
        if number >= 0:
            return number
        print("Non-negative numbers please...")

def read_range_float(prompt, min_range, max_range):
    while True:
        number = read_float(prompt)
        if min_range <= number <= max_range:
            return number
        print("Values out of range...please try again...")

def read_percentage_float(prompt):
    return read_range_float(prompt, 0.0, 100.0)
