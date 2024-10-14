"""
CPS 109 suggested Programming Exercises
String 1

Instructions 
===============================

This module contians the solutions to all the String 1 coding bat questions 
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

def hello_name(name):
  return "Hello " + name +"!"

def make_abba(a, b):
  """
     Given two strings, a and b, return the result of putting them together 
     in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
    
    >>> make_abba('Hi', 'Bye')
    'HiByeByeHi'
    
    >>> make_abba('Yo', 'Alice')
    'YoAliceAliceYo'
    
    >>> make_abba('What', 'Up')
    'WhatUpUpWhat'
  """ 
  
  pass

def make_tags(tag, word):
  """
  The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic 
  text. In this example, the "i" tag makes <i> and </i> which surround the word 
  "Yay". Given tag and word strings, create the HTML string with tags around the 
  word, e.g. "<i>Yay</i>".
  
  >>> make_tags('i', 'Yay')
  '<i>Yay</i>'
  
  >>> make_tags('i', 'Hello')
  '<i>Hello</i>'
  
  >>> make_tags('cite', 'Yay')
  '<cite>Yay</cite>'
  
  """
  pass

def make_out_word(out, word):
  """
  Given an "out" string length 4, such as "<<>>", and a word, return a new 
  string where the word is in the middle of the out string, e.g. "<<word>>".

  >>> make_out_word('<<>>', 'Yay')
  '<<Yay>>'
  
  >>> make_out_word('<<>>', 'WooHoo')
  '<<WooHoo>>'
  
  >>> make_out_word('[[]]', 'word')
  '[[word]]'
  
  """
  pass

def extra_end(str):
  """
  Given a string, return a new string made of 3 copies of the last 2 chars of 
  the original string. The string length will be at least 2.
  
  >>> extra_end('Hello')
  'lololo'
  
  >>> extra_end('ab')
  'ababab'
  
  >>> extra_end('Hi')
  'HiHiHi'
  """
  pass

def first_two(str):
  """
  Given a string, return the string made of its first two chars, so the String 
  "Hello" yields "He". If the string is shorter than length 2, return whatever 
  there is, so "X" yields "X", and the empty string "" yields the empty 
  string "".

  >>> first_two('Hello')
  'He'
  
  >>> first_two('abcdefg')
  'ab'
  
  >>> first_two('ab')
  'ab'
  
  """
  pass

def first_half(str):
  """
  Given a string of even length, return the first half. So the string "WooHoo" 
  yields "Woo".

  >>> first_half('WooHoo')
  'Woo'
  
  >>> first_half('HelloThere')
  'Hello'
  
  >>> first_half('abcdef')
  'abc'
  """
  pass

def without_end(str):
  """
  Given a string, return a version without the first and last char, so "Hello" 
  yields "ell". The string length will be at least 2.

  >>> without_end('Hello')
  'ell'
  
  >>> without_end('java')
  'av'
  
  >>> without_end('coding')
  'odin'
  
  """
  pass

def combo_string(a, b):
  """
  Given 2 strings, a and b, return a string of the form short+long+short, 
  with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).


  >>> combo_string('Hello', 'hi')
  'hiHellohi'
  
  >>> combo_string('hi', 'Hello')
  'hiHellohi'
  
  >>> combo_string('aaa', 'b')
  'baaab'
  
  """
  pass

def non_start(a, b):
  """
  Given 2 strings, return their concatenation, except omit the first char of 
  each. The strings will be at least length 1.
  
  >>> non_start('Hello', 'There')
  'ellohere'
  
  >>> non_start('java', 'code')
  'avaode'
  
  >>> non_start('shotl', 'java')
  'hotlava'
  """
  pass

def left2(str):
  """
  Given a string, return a "rotated left 2" version where the first 2 chars are 
  moved to the end. The string length will be at least 2.
  
  >>> left2('Hello')
  'lloHe'
  
  >>> left2('java')
  'vaja'
  
  >>> left2('Hi')
  'Hi'
  """
  pass

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)