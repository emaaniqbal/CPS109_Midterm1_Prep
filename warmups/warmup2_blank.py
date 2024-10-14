"""
CPS 109 suggested Programming Exercises
Warm Up 2

Instructions 
===============================

This module contians the solutions to all the Warm Up 2 coding bat questions 
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
def string_times(str, n):
  """
  Given a string and a non-negative int n, return a larger string that is n 
  copies of the original string.
  
  >>> string_times('Hi', 2)
  'HiHi'
  >>> string_times('Hi', 3)
  'HiHiHi'
  >>> string_times('Hi', 1)
  'Hi'
  """
  pass

def front_times(str, n):
  """
  Given a string and a non-negative int n, we'll say that the front of the 
  string is the first 3 chars, or whatever is there if the string is less than 
  length 3. Return n copies of the front;

  >>> front_times('Chocolate', 2)
  'ChoCho'
  
  >>> front_times('Chocolate', 3)
  'ChoChoCho'
  
  >>> front_times('Abc', 3)
  'AbcAbcAbc'
  """
  pass 

def string_bits(str):
  """
  Given a string, return a new string made of every other char starting with
  the first, so "Hello" yields "Hlo".

  >>> string_bits('Hello')
  'Hlo'
  >>> string_bits('Hi')
  'H'
  >>> string_bits('Heeololeo')
  'Hello'
  """
  pass

def string_splosion(str):
  """
  Given a non-empty string like "Code" return a string like "CCoCodCode".
  
  >>> string_splosion('Code')
  'CCoCodCode'
  >>> string_splosion('abc')
  'aababc'
  >>> string_splosion('ab')
  'aab'
  """
  pass

def last2(str):
  """
  Given a string, return the count of the number of times that a substring 
  length 2 appears in the string and also as the last 2 chars of the string, 
  so "hixxxhi" yields 1 (we won't count the end substring).

  >>> last2('hixxhi')
  1
  >>> last2('xaxxaxaxx')
  1
  >>> last2('axxxaaxx')
  2
  """
  pass

def array_count9(nums):
  """
  
  Given an array of ints, return the number of 9's in the array.
  
  
  >>> array_count9([1, 2, 9])
  1
  >>> array_count9([1, 9, 9])
  2
  >>> array_count9([1, 9, 9, 3, 9])
  3
  """
  pass

def array_front9(nums):
  """
  Given an array of ints, return True if one of the first 4 elements in the 
  array is a 9. The array length may be less than 4.


  >>> array_front9([1, 2, 9, 3, 4])
  True
  >>> array_front9([1, 2, 3, 4, 9])
  False
  >>> array_front9([1, 2, 3, 4, 5])
  False
  
  """
  pass

def array123(nums):
  """
  Given an array of ints, return True if the sequence of numbers 1, 2, 3 
  appears in the array somewhere.

  >>> array123([1, 1, 2, 3, 1])
  True
  >>> array123([1, 1, 2, 4, 1])
  False
  >>> array123([1, 1, 2, 1, 2, 3])
  True
  """
  pass

def string_match(a, b):
  """
  Given 2 strings, a and b, return the number of the positions where they
  contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, 
  since the "xx", "aa", and "az" substrings appear in the same place in both 
  strings.
  
  
  >>> string_match('xxcaazz', 'xxbaaz')
  3
  >>> string_match('abc', 'abc')
  2
  >>> string_match('abc', 'axc')
  0
  
  """
  pass
    
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
