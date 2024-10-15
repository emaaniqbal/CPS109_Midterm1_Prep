"""
CPS 109 suggested Programming Exercises
Logic 2

Instructions
===============================

This module contians the solutions to all the Logic 2 coding bat questions
which were suggested for midterm 1 preperation.

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


def make_bricks(small, big, goal):
    """
    Determine if it is possible to make a row of bricks that is exactly 'goal' inches long
    using the given number of small and big bricks.

    Each small brick has a length of 1 inch, and each big brick has a length of 5 inches.
    The function returns True if it is possible to achieve the goal length with the available
    bricks, and False otherwise.

    The key points to consider are:
    - You can use up to 'big' big bricks, each contributing 5 inches to the total length.
    - The remaining length to reach 'goal' must be achievable using 'small' small bricks.

    >>> make_bricks(3, 1, 8)
    True
    >>> make_bricks(3, 1, 9)
    False
    >>> make_bricks(3, 2, 10)
    True
    >>> make_bricks(0, 2, 10)
    True
    >>> make_bricks(5, 1, 11)
    False
    >>> make_bricks(7, 1, 11)
    True
    """


def lone_sum(a, b, c):
    """
    Calculate the sum of three integer values a, b, and c. If any of the values are the same
    as another, they do not contribute to the sum.

    The function checks for duplicates among the three values and only includes the unique
    values in the total sum.

    >>> lone_sum(1, 2, 3)
    6
    >>> lone_sum(3, 2, 3)
    2
    >>> lone_sum(3, 3, 3)
    0
    >>> lone_sum(1, 1, 2)
    2
    >>> lone_sum(4, 5, 5)
    4
    >>> lone_sum(10, 20, 10)
    20
    """


def lucky_sum(a, b, c):
    """
    Calculate the sum of three integer values a, b, and c, with a special condition regarding the value 13.

    If any of the values is 13, that value and all values to its right do not count towards the sum.
    For example, if b is 13, then both b and c will be excluded from the sum.

    >>> lucky_sum(1, 2, 3)
    6
    >>> lucky_sum(1, 2, 13)
    3
    >>> lucky_sum(1, 13, 3)
    1
    >>> lucky_sum(13, 2, 3)
    0
    >>> lucky_sum(1, 13, 13)
    1
    >>> lucky_sum(2, 3, 5)
    10
    """


def no_teen_sum(a, b, c):
    """
    Calculate the sum of three integer values a, b, and c, with special handling for "teen" values.

    In this context, a teen value is defined as any integer in the range of 13 to 19 inclusive,
    except for the values 15 and 16, which are not considered teens for the purpose of this sum.
    The function returns the sum of the values, counting teen values as 0 (except for 15 and 16).

    The function uses a helper function `fix_teen(n)` to apply the teen rules for each value.

    >>> no_teen_sum(1, 2, 3)
    6
    >>> no_teen_sum(2, 13, 1)
    3
    >>> no_teen_sum(2, 1, 14)
    3
    >>> no_teen_sum(15, 16, 17)
    31
    >>> no_teen_sum(19, 19, 19)
    0
    >>> no_teen_sum(10, 12, 13)
    22
    """


def fix_teen(n):
    """
    Fix the value n according to the teen rule.

    If n is a teen (in the range of 13 to 19), return 0, except for the values 15 and 16,
    which are returned as is.

    >>> fix_teen(13)
    0
    >>> fix_teen(15)
    15
    >>> fix_teen(17)
    0
    >>> fix_teen(16)
    16
    >>> fix_teen(10)
    10
    """


def round_sum(a, b, c):
    """
    Calculate the sum of three integer values a, b, and c, rounded to the nearest multiple of 10.

    The rounding rules are as follows:
    - If the rightmost digit of the number is 5 or more, round up to the next multiple of 10.
    - If the rightmost digit of the number is less than 5, round down to the previous multiple of 10.

    This function utilizes a helper function `round10(num)` to perform the rounding for each of the three values.

    >>> round_sum(16, 17, 18)
    60
    >>> round_sum(12, 13, 14)
    30
    >>> round_sum(6, 4, 4)
    10
    >>> round_sum(15, 25, 35)
    80
    >>> round_sum(0, 5, 10)
    20
    >>> round_sum(11, 21, 31)
    60
    """


def round10(num):
    """
    Round the given integer num to the nearest multiple of 10.

    The rounding is performed based on the following rules:
    - If the rightmost digit of num is 5 or more, round up to the next multiple of 10.
    - If the rightmost digit of num is less than 5, round down to the previous multiple of 10.

    >>> round10(12)
    10
    >>> round10(15)
    20
    >>> round10(27)
    30
    >>> round10(30)
    30
    >>> round10(44)
    40
    >>> round10(55)
    60
    """


def close_far(a, b, c):
    """
    Determine if one of the two integers (b or c) is "close" to the integer a,
    while the other is "far" from both a and the first integer.

    A number is considered "close" if it differs from a by at most 1 (i.e., |a - b| ≤ 1 or |a - c| ≤ 1).
    A number is considered "far" if it differs from both a and the other number by 2 or more.

    >>> close_far(1, 2, 10)
    True
    >>> close_far(1, 2, 3)
    False
    >>> close_far(4, 1, 3)
    True
    >>> close_far(5, 4, 6)
    False
    >>> close_far(10, 8, 12)
    False
    >>> close_far(0, 1, 3)
    True
    """


def make_chocolate(small, big, goal):
    """
    Determine the number of small chocolate bars needed to reach a target weight,
    prioritizing the use of big chocolate bars.

    The function calculates the number of small (1 kilo each) and big (5 kilos each)
    chocolate bars needed to achieve the specified goal weight in kilos. The function
    attempts to use as many big bars as possible before resorting to small bars. If
    the goal cannot be met with the given bars, the function returns -1.

    >>> make_chocolate(4, 1, 9)
    4
    >>> make_chocolate(4, 1, 10)
    -1
    >>> make_chocolate(4, 1, 7)
    2
    >>> make_chocolate(0, 2, 10)
    0
    >>> make_chocolate(3, 2, 8)
    3
    >>> make_chocolate(1, 1, 6)
    -1
    """


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
