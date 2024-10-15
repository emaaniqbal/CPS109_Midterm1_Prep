"""
CPS 109 suggested Programming Exercises
Logic 1

Instructions
===============================

This module contians the solutions to all the Logic 1 coding bat questions
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


def cigar_party(cigars, is_weekend):
    """
    Determine whether a squirrel party is successful based on the number of cigars and whether it is the weekend.

    A squirrel party is considered successful if the number of cigars is between 40 and 60, inclusive.
    If it is the weekend, there is no upper limit on the number of cigars, but there must be at least 40 cigars.
    >>> cigar_party(30, False)
    False
    >>> cigar_party(50, False)
    True
    >>> cigar_party(70, True)
    True
    >>> cigar_party(60, True)
    True
    >>> cigar_party(40, False)
    True
    >>> cigar_party(61, False)
    False
    >>> cigar_party(39, True)
    False
    """


def date_fashion(you, date):
    """
    Determine if you and your date can get a table at a restaurant based on your stylishness.

    The stylishness of your clothes is represented by the parameter 'you', and your date's stylishness
    is represented by the parameter 'date'. The result of getting the table is represented as an integer:
    - 0 means "no" (you cannot get a table),
    - 1 means "maybe" (uncertain if you can get a table),
    - 2 means "yes" (you can get a table).

    The rules are as follows:
    - If either you or your date has a stylishness of 8 or more, the result is 2 (yes).
    - If either you or your date has a stylishness of 2 or less, the result is 0 (no).
    - Otherwise, the result is 1 (maybe).

    >>> date_fashion(5, 10)
    2
    >>> date_fashion(5, 2)
    0
    >>> date_fashion(5, 5)
    1
    >>> date_fashion(8, 3)
    2
    >>> date_fashion(1, 7)
    0
    >>> date_fashion(10, 10)
    2
    """


def squirrel_play(temperature, is_summer):
    """
    Determine if squirrels play based on the temperature and whether it is summer.

    The squirrels play if the temperature is between 60 and 90 degrees inclusive.
    However, if it is summer, the upper limit increases to 100 degrees.

    >>> squirrel_play(70, False)
    True
    >>> squirrel_play(95, False)
    False
    >>> squirrel_play(95, True)
    True
    >>> squirrel_play(60, False)
    True
    >>> squirrel_play(90, False)
    True
    >>> squirrel_play(100, True)
    True
    >>> squirrel_play(101, True)
    False
    >>> squirrel_play(59, False)
    False
    """


def caught_speeding(speed, is_birthday):
    """
    Determine the ticket status based on the speed of the vehicle and whether it is the driver's birthday.

    The ticket status is encoded as an integer:
    - 0 for no ticket,
    - 1 for a small ticket,
    - 2 for a big ticket.

    The rules are as follows:
    - If the speed is 60 or less, the result is 0 (no ticket).
    - If the speed is between 61 and 80 (inclusive), the result is 1 (small ticket).
    - If the speed is 81 or more, the result is 2 (big ticket).
    - If it is the driver's birthday, the speed limits are increased by 5.

    >>> caught_speeding(60, False)
    0
    >>> caught_speeding(65, False)
    1
    >>> caught_speeding(65, True)
    0
    >>> caught_speeding(80, False)
    1
    >>> caught_speeding(81, False)
    2
    >>> caught_speeding(85, True)
    1
    >>> caught_speeding(90, True)
    2
    """


def sorta_sum(a, b):
    """
    Calculate the sum of two integers, a and b. If the sum falls within the range 10 to 19 inclusive,
    return 20 instead.
    >>> sorta_sum(3, 4)
    7
    >>> sorta_sum(9, 4)
    20
    >>> sorta_sum(10, 11)
    21
    >>> sorta_sum(5, 5)
    20
    >>> sorta_sum(15, 5)
    20
    >>> sorta_sum(2, 3)
    5
    """


def alarm_clock(day, vacation):
    """
    Determine the alarm clock time based on the day of the week and vacation status.

    The day is encoded as follows:
    - 0 = Sunday
    - 1 = Monday
    - 2 = Tuesday
    - 3 = Wednesday
    - 4 = Thursday
    - 5 = Friday
    - 6 = Saturday

    The alarm clock behaves as follows:
    - On weekdays (Monday to Friday), the alarm should ring at "7:00" unless it is vacation, in which case it should ring at "10:00".
    - On weekends (Saturday and Sunday), the alarm should ring at "10:00" unless it is vacation, in which case it should be "off".

    >>> alarm_clock(1, False)
    '7:00'
    >>> alarm_clock(5, False)
    '7:00'
    >>> alarm_clock(0, False)
    '10:00'
    >>> alarm_clock(6, True)
    'off'
    >>> alarm_clock(3, True)
    '10:00'
    >>> alarm_clock(5, True)
    '10:00'
    """


def love6(a, b):
    """
    Determine if the number 6 is involved in a relationship with two integers, a and b.

    The function returns True if:
    - Either a or b is equal to 6.
    - The sum of a and b is equal to 6.
    - The absolute difference between a and b is equal to 6.

    Examples:
    >>> love6(6, 4)
    True
    >>> love6(4, 5)
    False
    >>> love6(1, 5)
    True
    >>> love6(2, 4)
    False
    >>> love6(7, -1)
    True
    >>> love6(0, 6)
    True
    """


def in1to10(n, outside_mode):
    """
    Determine if a number n is in a specified range based on the outside_mode flag.

    The function behaves as follows:
    - If outside_mode is False, return True if n is in the range 1 to 10 (inclusive).
    - If outside_mode is True, return True if n is less than or equal to 1, or greater than or equal to 10.

    >>> in1to10(5, False)
    True
    >>> in1to10(11, False)
    False
    >>> in1to10(11, True)
    True
    >>> in1to10(0, True)
    True
    >>> in1to10(10, True)
    True
    >>> in1to10(1, False)
    True
    >>> in1to10(1, True)
    True
    """


def near_ten(num):
    """
    Determine if a non-negative number is within 2 of a multiple of 10.

    The function checks if the remainder when num is divided by 10 is either 0, 1, or 2,
    which indicates that num is within 2 of the nearest multiple of 10.

    >>> near_ten(12)
    True
    >>> near_ten(17)
    False
    >>> near_ten(19)
    True
    >>> near_ten(20)
    True
    >>> near_ten(22)
    True
    >>> near_ten(23)
    False
    >>> near_ten(30)
    True
    >>> near_ten(31)
    True
    >>> near_ten(32)
    False
    """


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
