"""
CPS 109 suggested Programming Exercises
Strings 2
Instructions 
===============================

This module contians the solutions to all the Strings 2 coding bat questions 
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

def double_char(str):
    """
    Given a string, return a string where for every char in the original, 
    there are two chars.

    >>> double_char('The')
    'TThhee'
    >>> double_char('AAbb')
    'AAAAbbbb'
    >>> double_char('Hi-There')
    'HHii--TThheerree'
    """
    pass

def count_hi(str):
    """
    Return the number of times that the string "hi" appears anywhere in the given string.

    >>> count_hi('abc hi ho')
    1
    >>> count_hi('ABChi hi')
    2
    >>> count_hi('hihi')
    2
    """
    pass

def cat_dog(str):
    """
    Return True if the string "cat" and "dog" appear the same number of times in the given string.

    >>> cat_dog('catdog')
    True
    
    >>> cat_dog('catcat')
    False
    
    >>> cat_dog('1cat1cadodog')
    True
    """
    pass

def count_code(str):
    """
    Count occurrences of the substring 'co_e' where '_' can be any single character.

    >>> count_code('aaacodebbb')
    1
    >>> count_code('codexxcode')
    2
    >>> count_code('cozexxcope')
    2
    >>> count_code('cooexxcope')
    2
    >>> count_code('')
    0
    """
    pass

def end_other(a, b):
    """
    Return True if either of the strings appears at the very end of the other string,
    ignoring case differences.

    >>> end_other('Hiabc', 'abc')
    True
    >>> end_other('AbC', 'HiaBc')
    True
    >>> end_other('abc', 'abXabc')

    """
    #Use s1.endswith(s2) in hint
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)