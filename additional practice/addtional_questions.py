"""
CPS 109 suggested Programming Exercises
addtional practice

NOTE: These are old test questions from past exams/test in beginner python CS courses (@uni lvl). For some questions,
values have been changed from og question, but these should all be doable!

Instructions
===============================
THESE ARE VERY COMMON STRUCT TO TEST QUESTIONS.
This module contians addtional questions to help prep for midterm 1.

To test the functions, just run cell, and the auto test should occur
if you are in pycharm, right click and press run file (or run doctests)

i.e of fully passed:
    37 tests in 13 items.
    37 passed and 0 failed.
    Test passed.

i.e of failure:

    1 items had failures:
       1 of   3 in __main__.makes10
    37 tests in 13 items.
    36 passed and 1 failed.
    ***Test Failed*** 1 failures.

    ^ that is refering to this test:
    #>>> makes10(9, 10)
    False

This file is an open resource for your learning! I will also provide
file with all the blank fxns and the unit test file to simulate a test
env.
==============================
@author: Emaan Iqbal
https://github.com/emaaniqbal
"""

# MC examples
"""
Without using the Python console, consider what these staments would return.
Use a rough paper if needed.

>>> 10 * (2 ** 2)
a) error
b) 40
c) 400
d) 14

>>> len('CPS109') + len({'lmnop'})
a) 6
b) 11
c) 8
d) error

>>> sum({x ** 2 for x in range(1, 5)})
a) 55
b) error
c) 20
d) 30

>>> {'bat': 1, 'bog': 5, 'flat': 2, 'fog': 2}[2]
a) error
b) flat
c) key error
d) 2

>>> [x + 10 for x in [10, 30, 40] if x > 20]
a) [20, 50]
b) error
c) [40, 50]
d) [20, 40, 50]
"""

"""
The function below has an incomplete def/header. 

def func1(...):
   if course[index] == "CPS"
        return "This is our course!"
    else:
        return "Not our course :(" 
     
Answer the following, without using the Python console:
   
 a) What is the function name?
 
 b) what does the function return?
 
 c) What are the parameter names and types? 
 
 d) Give an example of an argument. Give one for each condtion. 
 
 e) What is this function doing?
 
"""
"""
Given: 
>>> n = -5
>>> numbers_list = [1, 10, n]
>>> numbers_set = {100, n, 200}

Answer the following, without using the python console:
>>> abs(n)

>>> sorted(numbers_list)

>>> sorted(numbers_set) + sorted(numbers_list)

>>> len(numbers_set)

>>> len(numbers_list) == n

>>> sum(numbers_set) - n
"""


# Comprehensions
def comp1(nums):
    """
    Returns a list of cubes of integers from 1 to 3.

    >>> comp1([1,2,3])
    [1, 8, 27]
    """
    pass


def comp2(nums):
    """
    Returns a dictionary that maps integers from 1 to 3 to their multiples of 3.

    >>> comp2([1, 2, 3])
    {1: 3, 2: 6, 3: 9}
    >>> comp2([4, 5])
    {4: 12, 5: 15}
    """
    pass


def comp3(nums):
    """
    Returns a dictionary that swaps keys and values from the output of comp2.

    >>> comp3([1, 2, 3])
    {3: 1, 6: 2, 9: 3}
    >>> comp3([4, 5])
    {12: 4, 15: 5}
    """
    pass


# Programming / func examples

def count_duplicates_v1(lst):
    """
    Return the number of duplicates in lst.
    Precondition: each item in lst occurs either once or twice.
    >>> count_duplicates_v1([1, 2, 3, 4])
    0
    >>> count_duplicates_v1([2, 4, 3, 3, 1, 4])
    2
    """


def str_compaare(s1, s2, diff):
    """
    See if the difference of s1 to s2 is greater than or equal to the difference.

    Doctest example:
    >>> str_compaare('hello', 'world', 0)
    False
    >>> str_compaare('hello', 'world!', 1)
    True
    >>> str_compaare('hi', 'hello', 3)
    True
    >>> str_compaare('apple', 'banana', 3)
    False
    """
    pass

    """
    Bonus for str_compaare()
    
    Answer without using the Python console:
    
    a) What is the function name?
 
     b) what does the function return?
     
     c) What are the parameter names and types? 
     
     d) Give an example of an argument. Give one for each condtion. 
     
     e) What is this function doing?
    """


# Complete this function according to its docstring description.
def sum_of_digits(message):
    """
    (str ) -> int
    Precondition: len(message ) > 0
    Return the sum of the digits in message.
    >>> sum_of_digits('abcl2341')
    10
    >>> sum_of_digits('hi')
    0
    """


def smallest_five(scores):
    """
    (list of int) -> list of int
    Precondition: len(scores) >= 5 and each number in scores is unique
    Return a new list that contains the five smallest numbers from scores in
    ascending order.

    >>> smallest_five([1, 2, 3, 4, 5, 6, 7])
    [1, 2, 3, 4, 5]
    >>> smallest_five ( [6, 2, 11, 12, 7, 12, -3])
    [-3, 2, 6, 7, 11]
"""


def is_palindrome(s) -> bool:
    """
    A palindrome is a string that is read the same from front-to-back and back-to-front. For example, noon
    and racecar are both palindromes.
    There are several ways to check whether a string is a palindrome. One algorithm compares the first letter
    to the last letter, the second letter to the second last letter, and so on, stopping when the middle of the
    string is reached or when a mismatch is found.

    Return True if and only if s is a palindrome.

    >>> is_palindrome('noon')
    True
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('dented')
    False
    """


def prnt_lastname(suname):
    """

    Write a python program which asks the user to input their last name.
    The program should output their name one per line.
    The user can input anything. Make sure to print "ERROR" if the datatype given is invalid,
    of it the string provided has non alpha chars.

    For example:
    >>>  prnt_lastname("ALEX")
    A
    L
    E
    X
    """


# Debugging

"""
The following function does pass the doctest example, but actually has a subtle error, and so is
not correct on all possible inputs to the function:

def calculate_average(numbers):
    Calculate the average of a list of numbers.

    Parameters:
    numbers (list): A list of numerical values.

    Returns:
    float: The average of the numbers in the list.

    Doctest example:
    >>> calculate_average([1, 2, 3, 4, 5])
    3.0
    >>> calculate_average([10, 20, 30])
    20.0
    
    total = 0
    for num in numbers:
        total += num
        
    average = total / len(numbers) 
    return average

a) Explain the error and give a test case that fails (without using the Python console)

b) Write a correct function implementation for calculate_average() below.
"""


def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Parameters:
    numbers (list): A list of numerical values.

    Returns:
    float: The average of the numbers in the list.

    Doctest example:
    >>> calculate_average([1, 2, 3, 4, 5])
    3.0
    >>> calculate_average([10, 20, 30])
    20.0
    """


# Loops
def long_greeting(names):
    """
    Return a greeting message that greets every person in names.
    Each greeting should have the form "Hello <name>! " (note the space at the
    end).
    The returned string should be the concatenation of all the greetings.

    >>> long_greeting(['Cat', 'Dog']) # Note the "extra" space at the end
    'Hello Cat! Hello Dog! '
    """


"""
There is an issue with this code! 
Identify the problem and explain it below.

def is_IP_address(address: str) -> bool:

    Return whether address contains only digits and periods.

    for ch in address:
    
        if ch in '0123456789.':
            return True
        else:
            return False
"""


def is_IP_address(address):
    """
    Return whether address contains only digits and periods.
    """


"""
State the outputs:
a)  n1 = 45
    n2 = n1
    n2 = n1 + 1
    print(n1) # state output here:
    print(n2) # state output here:

b)
    L = [2, 4, 6, 8]
    for item in range(len(L)):
        item = item + 1
    print(L) # state output here:
"""

if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
