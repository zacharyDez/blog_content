from random import choice
import string

"""
1. Get user input for password length
"""

password_length = 1

while password_length < 10 or password_length > 20:

    try:
        password_length = int(input("\nEnter password between 10 et 20 caracters: "))

    # casting to integer will return a ValueError if else than a number
    except ValueError:
        print("You entered something other than a number")

"""
2. Declare possible characters
"""

# letters
alpha_low = string.ascii_lowercase
alpha_up = string.ascii_uppercase

# numbers
numbers = [str(x) for x in range(0, 10)]

# symbols
symbols = """` ! " ? $ ? % ^ & * ( ) _ - + = { [ } ] : ; @ ' ~ # | \ < , > . ? /"""
symbols = symbols.split(" ")

"""
3. Generate password
"""

password = ""
count = {"symbols": 0, "numbers": 0, "alpha_low": 0, "alpha_up": 0}

"""
4. Verify password conditions
"""
while 0 in count.values():
    for i in range(password_length):
        categories = [alpha_up, alpha_low, numbers, symbols]
        picked_element = choice(choice(categories))
        password += str(picked_element)

    print(password)

    for element in password:
        if element in alpha_low:
            count["alpha_low"] += 1

        elif element in alpha_up:
            count["alpha_up"] += 1

        elif element in numbers:
            count["numbers"] += 1

        else:
            count["symbols"] += 1

    print(count)
