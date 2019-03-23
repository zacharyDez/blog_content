# Python Exemption Handling - A Practical Introduction
This post was originally posted on [my site](zacharydeziel.com)
## Project Setup

It is assumed that you have a working version of Python3 on your machine. 
Only packages from the standard library are used in the article.

## Defining the problem

A student from the introduction to geospatial programming course for which 
I am a tutor asked me to help him with the following exercise. 

#### The problem to be resolved was presented in the following manner:

Write a program that generates a password respecting the following conditions:

1. Contains at least one uppercase and lowercase letter
2. Contains at least one number
3. Contains at least one symbol of the following: ` ! " ? $ ? % ^ & * ( ) _ - + = { [ } ] : ; @ ' ~ # | \ < , > . ? /
4. The size of the password must be determined by the user

#### Some thoughts

The student had no difficulty understanding the problem, he had established clean pseudo-code. He had a working solution, 
but it was difficult to read, partially hardcoded and longer than necessary. Yet the solution worked and is part of a 
normal learning process to writing better code in the future. 

The trouble I found the student was having (and one I constantly go through) 
was missing experience reading quality code examples.

The objective is to explain practical code examples more in depth that will help students grasp certain programming 
concepts. Hopefully, starting some reflexions on not just developing programs
that work (for a moment in time) but programs that are somewhat optimized and easier to maintain in the future.


#### Pseudo-code

1. Get user input
2. Declare possible characters
3. Generate password
4. Check if password conditions are met

#### 1. Get user input

```python
password_length = 1

while password_length < 10 or password_length > 20:

    try:
        password_length = int(input('\nEnter password between 10 et 20 caracters: '))

    # casting to integer will return a ValueError if else than a number
    except ValueError:
        print("You entered something other than a number")
```

There's a lot going on... Initially we set the password length to 1 to ensure that the *while* condition is entered at 
least once. We then ask the user for his input. This is where an interesting example of exception handling goes on.

Input in Python3 is considered as a string. 
The difficulty of this problem is to effectively filter user input when it is a number. 
'Try and excepts' are highly effective at this task. 

When casting the input to an integer, an error of type 'ValueError' will be raised if the input is not a number. 
The value of password length is only changed if the casting of the input is accepted. 
Otherwise, we simply output a message and the password_length variable remains of value 1. 
Thus, the *while* loop is executed again and again until the user input is correct.

#### WARNING: Do not use general exceptions! 

##### Example:

```python
    try:
        password_length = int(input('\nEnter password between 10 et 20 caracters: '))

    # casting to integer will return a ValueError if else than a number
    except:
        print("You entered something other than a number")
```

#### What's wrong?
Error messages are valuable. When using a general except clause, all error messages are silenced.
 
This can lead to our code breaking unexpectedly and the cause of the break being buried deep inside your program.

Don't assume that a single type of error is the only one that could occur. 

Prepare multiple except statements to handle multiple error types. 

Do not use a general exception statement. It will save you time in the future and your code will be much more explicit.

#### 2. Declare possible characters

```python
# letters
alpha_low = string.ascii_lowercase
alpha_up = string.ascii_uppercase

# numbers
numbers = [str(x) for x in range(0, 10)]

# symbols
symbols = """` ! " ? $ ? % ^ & * ( ) _ - + = { [ } ] : ; @ ' ~ # | \ < , > . ? /"""
symbols = symbols.split(' ')
```

Declaring the possible characters of the password is used to check if the password conditions are met afterwards.
One way to obtain this list would be to explicitly enter them one by one in a list or a string. 
This is far from optimal and simply boring. 
Knowing some standard library tricks is always helpful in this situation.

For the numbers category, we are using a list comprehension to cast elements of our in range statement to strings. 
List comprehensions are powerful, read more about them: 
*[list comprehensions](https://realpython.com/lessons/writing-your-first-list-comprehension/), 
[generators](https://realpython.com/introduction-to-python-generators/)*.

The symbols were already explicitly entered in the problem description: 
we simply copied and paste them and applied the 'split' string method to convert it to a list.

#### 3. Generate password and verify password conditions

```python
password = ''
count = {
    'symbols': 0,
    'numbers': 0,
    'alpha_low': 0,
    'alpha_up': 0
}

while 0 in count.values():
    for i in range(password_length):
        categories = [alpha_up, alpha_low, numbers, symbols]
        picked_element = choice(choice(categories))
        password += str(picked_element)

    print(password)

    for element in password:
        if element in alpha_low:
            count['alpha_low'] += 1

        elif element in alpha_up:
            count['alpha_up'] += 1

        elif element in numbers:
            count['numbers'] += 1

        else:
            count['symbols'] += 1

    print(count)
```

The idea is the following:
1. Create a count dictionary containing our categories
2. Initialize the password to an empty string
4. Iterate password_length number of times to:
    - Pick a random element of a random category (using choice() function)
    - Add the element to the password
    - Add one to the pick category
5. The while loop will be executed again if the password does not match the conditions (low probability)

There are other ways to keep counts but dictionaries are an optimal and readable solution. 
In Python 2, there used to be a trade-off between memory and speed where dictionaries were faster but demanded more memory.
Since Python 3, there is no longer that trade-off. Dictionaries are simply more efficient and readable.

## Conclusion

This was a practical example to introduce Python exception handling. 

If you have any other questions or comments on the post do not hesitate to reach out!

This post was originally posted on [my site](zacharydeziel.com).

The full code example is available on [github](https://github.com/zacharyDez/blog_content).




