"""
CPS 109 suggested Programming Exercises
Lists 2
Instructions 
===============================

This module contians the solutions to all the Lists 2 coding bat questions 
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
    >>> makes10(9, 10)
    False

This file is an open resource for your learning! I will also provide 
file with all the blank fxns and the unit test file to simulate a test 
env.
==============================
@author: Emaan Iqbal
https://github.com/emaaniqbal
"""

def count_evens(nums):
    """
    Return the number of even integers in the given array.

    >>> count_evens([2, 1, 2, 3, 4])
    3
    >>> count_evens([2, 2, 0])
    3
    >>> count_evens([1, 3, 5])
    0
    >>> count_evens([]) 
    0
    >>> count_evens([1, 2, 3, 4, 5, 6])
    3
    """
    pass

def big_diff(nums):
    """
    Return the difference between the largest and smallest values in the array.
    
    >>> big_diff([10, 3, 5, 6])
    7
    >>> big_diff([7, 2, 10, 9])
    8
    >>> big_diff([2, 10, 7, 2])
    8
    >>> big_diff([1])
    0
    >>> big_diff([-1, -2, -3, -4])
    3
    >>> big_diff([100, 0, 50, 25])
    100
    >>> big_diff([0, 0, 0])
    0
    """
    pass

def centered_average(nums):
    """
    Return the "centered" average of an array of ints, ignoring the largest 
    and smallest values.

    >>> centered_average([1, 2, 3, 4, 100])
    3
    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5
    >>> centered_average([-10, -4, -2, -4, -2, 0])
    -3
    >>> centered_average([1, 1, 1, 1, 1])
    1
    >>> centered_average([10, 5, 4])
    5
    """
    pass

def sum13(nums):
    """
    Return the sum of the numbers in the array, returning 0 for an empty array.
    The number 13 does not count, and numbers that come immediately after a 13 do not count.
    
    >>> sum13([1, 2, 2, 1])
    6
    >>> sum13([1, 1])
    2
    >>> sum13([1, 2, 2, 1, 13])
    6
    >>> sum13([13, 1, 2, 13, 2])
    2
    >>> sum13([13, 13, 2, 1])
    1
    >>> sum13([])
    0
    >>> sum13([13, 13])
    0
    >>> sum13([1, 2, 3, 13, 5, 6])
    6
    """
    pass
  
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)