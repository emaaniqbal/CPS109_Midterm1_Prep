"""
CPS 109 suggested Programming Exercises
List 1

Instructions
===============================

This module contians the solutions to all the List 1 coding bat questions
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


def first_last6(nums):
    """
  Given an array of ints, return True if 6 appears as either the first or
  last element in the array. The array will be length 1 or more.
  >>> first_last6([1, 2, 6])
  True

  >>> first_last6([6, 1, 2, 3])
  True

  >>> first_last6([13, 6, 1, 2, 3])
  False

  >>> first_last6([6])
  True
  """
    pass


def same_first_last(nums):
    """
    Given an array of ints, return True if the array is length 1 or more,
    and the first element and the last element are equal.

    >>> same_first_last([1, 2, 3])
    False

    >>> same_first_last([1, 2, 3, 1])
    True

    >>> same_first_last([1, 2, 1])
    True

    >>> same_first_last([7])
    True

    >>> same_first_last([])
    False
  """
    pass


def common_end(a, b):
    """
  Given 2 arrays of ints, a and b, return True if they have the same first element or
  they have the same last element. Both arrays will be length 1 or more.

  >>> common_end([1, 2, 3], [7, 3])
  True

  >>> common_end([1, 2, 3], [7, 3, 2])
  False

  >>> common_end([1, 2, 3], [1, 3])
  True

  >>> common_end([4], [4])
  True

  >>> common_end([5, 6], [7, 5])
  False
  """
    pass


def sum3(nums):
    """
    Given an array of ints length 3, return the sum of all the elements.

    >>> sum3([1, 2, 3])
    6

    >>> sum3([5, 11, 2])
    18

    >>> sum3([7, 0, 0])
    7
    """
    pass


def rotate_left3(nums):
    """
    Given an array of ints length 3, return an array with the elements "rotated left"
    so {1, 2, 3} yields {2, 3, 1}.

    >>> rotate_left3([1, 2, 3])
    [2, 3, 1]

    >>> rotate_left3([5, 11, 9])
    [11, 9, 5]

    >>> rotate_left3([7, 0, 0])
    [0, 0, 7]

  """
    pass


def reverse3(nums):
    """
    Given an array of ints length 3, return a new array with the elements in reverse order,
    so {1, 2, 3} becomes {3, 2, 1}.

    >>> reverse3([1, 2, 3])
    [3, 2, 1]
    >>> reverse3([5, 11, 9])
    [9, 11, 5]
    """
    pass


def max_end3(nums):
    """
    Given an array of ints length 3, figure out which is larger, the first or last element
    in the array, and set all the other elements to be that value. Return the changed array.

    >>> max_end3([1, 2, 3])
    [3, 3, 3]

    >>> max_end3([11, 5, 9])
    [11, 11, 11]

    >>> max_end3([2, 11, 3])
    [3, 3, 3]
    """
    pass


def sum2(nums):
    """
    Given an array of ints, return the sum of the first 2 elements in the array.
    If the array length is less than 2, just sum up the elements that exist,
    returning 0 if the array is length 0.

    >>> sum2([1, 2, 3])
    3
    >>> sum2([1, 1])
    2
    >>> sum2([1, 1, 1, 1])
    2
    >>> sum2([5])
    5
    >>> sum2([])
    0
    """
    pass


def middle_way(a, b):
    """
    Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.

    >>> middle_way([1, 2, 3], [4, 5, 6])
    [2, 5]

    >>> middle_way([7, 7, 7], [3, 8, 0])
    [7, 8]

    >>> middle_way([5, 2, 9], [1, 4, 5])
    [2, 4]
    """
    pass


def make_ends(nums):
    """
    Given an array of ints, return a new array length 2 containing the first
    and last elements from the original array. The original array will be
    length 1 or more.

    >>> make_ends([1, 2, 3])
    [1, 3]
    >>> make_ends([1, 2, 3, 4])
    [1, 4]
    >>> make_ends([7, 4, 6, 2])
    [7, 2]
    >>> make_ends([5])
    [5, 5]
    """
    pass


def has23(nums):
    """
    Given an int array length 2, return True if it contains a 2 or a 3.

    >>> has23([2, 5])
    True
    >>> has23([4, 3])
    True
    >>> has23([4, 5])
    False
    """
    pass


def xyz_there(s):
    """
    Determine whether the given string contains an occurrence of "xyz" that is not directly preceded by a period (.).
    The function should return True if "xyz" appears without a preceding period, and False otherwise.

    A string containing "xyz" with a period directly before it (e.g., "x.xyz") does not count, while "xyz" at the
    start of the string or after any character other than a period is considered valid (e.g., "xyz.abc" and "abcxyz" count).

    >>> xyz_there('abcxyz')
    True
    >>> xyz_there('abc.xyz')
    False
    >>> xyz_there('xyz.abc')
    True
    >>> xyz_there('xxyz')
    True
    >>> xyz_there('x.xyz')
    False
    >>> xyz_there('xyz')
    True
    """
    pass


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
