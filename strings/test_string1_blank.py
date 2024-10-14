import unittest
import string1_blank

class TestStrings1(unittest.TestCase):

    def test_hello_name(self):
        self.assertEqual(string1_blank.hello_name("Emaan"), "Hello Emaan!")  # Basic case
        self.assertEqual(string1_blank.hello_name("Alice"), "Hello Alice!")  # Basic case
        self.assertEqual(string1_blank.hello_name("Bob"), "Hello Bob!")      # Basic case

    def test_make_abba(self):
        self.assertEqual(string1_blank.make_abba('Hi', 'Bye'), 'HiByeByeHi')     # Basic case
        self.assertEqual(string1_blank.make_abba('Yo', 'Alice'), 'YoAliceAliceYo') # Basic case
        self.assertEqual(string1_blank.make_abba('What', 'Up'), 'WhatUpUpWhat')    # Basic case

    def test_make_tags(self):
        self.assertEqual(string1_blank.make_tags('i', 'Yay'), '<i>Yay</i>')           # Basic case
        self.assertEqual(string1_blank.make_tags('i', 'Hello'), '<i>Hello</i>')       # Basic case
        self.assertEqual(string1_blank.make_tags('cite', 'Yay'), '<cite>Yay</cite>')  # Basic case

    def test_make_out_word(self):
        self.assertEqual(string1_blank.make_out_word('<<>>', 'Yay'), '<<Yay>>')            # Basic case
        self.assertEqual(string1_blank.make_out_word('<<>>', 'WooHoo'), '<<WooHoo>>')      # Basic case
        self.assertEqual(string1_blank.make_out_word('[[]]', 'word'), '[[word]]')          # Basic case

    def test_extra_end(self):
        self.assertEqual(string1_blank.extra_end('Hello'), 'lololo')      # Basic case
        self.assertEqual(string1_blank.extra_end('ab'), 'ababab')          # Basic case
        self.assertEqual(string1_blank.extra_end('Hi'), 'HiHiHi')          # Basic case

    def test_first_two(self):
        self.assertEqual(string1_blank.first_two('Hello'), 'He')           # Basic case
        self.assertEqual(string1_blank.first_two('abcdefg'), 'ab')         # Longer string
        self.assertEqual(string1_blank.first_two('ab'), 'ab')               # Exactly two

    def test_first_half(self):
        self.assertEqual(string1_blank.first_half('WooHoo'), 'Woo')        # Basic case
        self.assertEqual(string1_blank.first_half('HelloThere'), 'Hello')  # Longer string
        self.assertEqual(string1_blank.first_half('abcdef'), 'abc')        # Basic case

    def test_without_end(self):
        self.assertEqual(string1_blank.without_end('Hello'), 'ell')        # Basic case
        self.assertEqual(string1_blank.without_end('java'), 'av')          # Basic case
        self.assertEqual(string1_blank.without_end('coding'), 'odin')      # Basic case

    def test_combo_string(self):
        self.assertEqual(string1_blank.combo_string('Hello', 'hi'), 'hiHellohi')       # Basic case
        self.assertEqual(string1_blank.combo_string('hi', 'Hello'), 'hiHellohi')       # Basic case
        self.assertEqual(string1_blank.combo_string('aaa', 'b'), 'baaab')               # Short and long

    def test_non_start(self):
        self.assertEqual(string1_blank.non_start('Hello', 'There'), 'ellohere')         # Basic case
        self.assertEqual(string1_blank.non_start('java', 'code'), 'avaode')             # Basic case
        self.assertEqual(string1_blank.non_start('shotl', 'java'), 'hotlava')           # Basic case

    def test_left2(self):
        self.assertEqual(string1_blank.left2('Hello'), 'lloHe')          # Basic case
        self.assertEqual(string1_blank.left2('java'), 'vaja')            # Basic case
        self.assertEqual(string1_blank.left2('Hi'), 'Hi')                # Short string

if __name__ == '__main__':
    unittest.main()


