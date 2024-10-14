"""
CPS 109 suggested Programming Exercises
lab questions
Instructions 
===============================

This module contians an similar lab questions from cps 109

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

# Source: https://www.geeksforgeeks.org/area-of-a-n-sided-regular-polygon-with-given-side-length/

def n_sided_polygon(n_sides: int, side_len: float):
   """
   Calc and print area of n-sided polygon
   
   >>> n_sided_polygon(4, 5.0)
   The area is 25.0!
   """
   pass

# Source: https://www.programiz.com/python-programming/examples/factor-number
def int_reader(n: int):
   """
   Find and print the factors of the given n(number) between 2-8
   Return the factor of the given value
   If there are no factors, return None
   
   >>> int_reader(12)
   The factors of 12 between 2 and 8 are 2, 3, 4, 6.
   
   >>> int_reader(28)
   The factors of 12 between 2 and 8 are 4,7.
   
   >>> int_reader(15)
   None
   
   >>> int_reader(1)
   None
   
   >>> int_reader(64)
   The factors of 12 between 2 and 8 are 4,8.
    
   >>> int_reader(9)
   The factors of 9 between 2 and 8 are 3.
   """
   pass
   
# Source: https://www.geeksforgeeks.org/python-program-check-validity-password/
def valid_password(pass_new: str, pass_valid: str):
   """
   Check if the new pass word is valif based on these condtions:
       
    - Minimum 8 characters.
    - The alphabet must be between [a-z]
    - At least one alphabet should be of Upper Case [A-Z]
    - At least 1 number or digit between [0-9].
    - At least 1 character from [ _ or @ or $ ].
    
   >>> valid__password("123", "123")
   Password not complex enough
   
   >>> valid__password("ACVbAY2034","ACVbAY2034" )
   Password changed successfully
   
   >>> valid__password("123456789", "123456789")
   Password not complex enough
   """
   pass
   
def bats_bogs(n: int):
    """
    Prints numbers from 1 to n, replacing multiples of 4 with "Bats",
    multiples of 6 with "Bogs", and multiples of both with "BatsBogs".
    
    >>> bats_bogs(24)
    1
    2
    3
    Bats
    5
    Bogs
    7
    Bats
    9
    10
    Bogs
    11
    Bats
    13
    14
    Bogs
    15
    Bats
    17
    18
    Bats
    20
    21
    Bogs
    23
    BatsBogs
    
    >>> bats_bogs(0)
    N must be greater than 1
    
    >>> bats_bogs(56)
    Too much work, no thanks
    
    >>> bats_bogs(1)
    N must be greater than 1
    """
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

