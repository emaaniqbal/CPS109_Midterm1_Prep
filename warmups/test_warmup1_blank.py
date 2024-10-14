import unittest
import warmup1_blank 

class TestWarmup1(unittest.TestCase):

    def test_sleep_in(self):
        self.assertTrue(warmup1_blank.sleep_in(False, False))  # Not a weekday and not on vacation
        self.assertFalse(warmup1_blank.sleep_in(True, False))  # It is a weekday
        self.assertTrue(warmup1_blank.sleep_in(False, True))   # Not a weekday, but on vacation

    def test_monkey_trouble(self):
        self.assertTrue(warmup1_blank.monkey_trouble(True, True))   # Both monkeys are smiling
        self.assertTrue(warmup1_blank.monkey_trouble(False, False)) # Both monkeys are not smiling
        self.assertFalse(warmup1_blank.monkey_trouble(True, False)) # One monkey is smiling

    def test_sum_double(self):
        self.assertEqual(warmup1_blank.sum_double(1, 2), 3)   # Different numbers
        self.assertEqual(warmup1_blank.sum_double(3, 2), 5)   # Different numbers
        self.assertEqual(warmup1_blank.sum_double(2, 2), 8)   # Same numbers

    def test_diff21(self):
        self.assertEqual(warmup1_blank.diff21(19), 2)   # Below 21
        self.assertEqual(warmup1_blank.diff21(10), 11)  # Below 21
        self.assertEqual(warmup1_blank.diff21(21), 0)   # Exactly 21
        self.assertEqual(warmup1_blank.diff21(22), 2)   # Above 21
        self.assertEqual(warmup1_blank.diff21(40), 38)  # Above 21

    def test_parrot_trouble(self):
        self.assertTrue(warmup1_blank.parrot_trouble(True, 6))   # Talking before 7
        self.assertFalse(warmup1_blank.parrot_trouble(True, 7))  # Talking at 7
        self.assertFalse(warmup1_blank.parrot_trouble(False, 6))  # Not talking

    def test_makes10(self):
        self.assertTrue(warmup1_blank.makes10(9, 10))   # One is 10
        self.assertFalse(warmup1_blank.makes10(9, 9))   # Neither is 10
        self.assertTrue(warmup1_blank.makes10(1, 9))    # Their sum is 10

    def test_near_hundred(self):
        self.assertTrue(warmup1_blank.near_hundred(93))   # Within 10 of 100
        self.assertTrue(warmup1_blank.near_hundred(90))   # Within 10 of 100
        self.assertFalse(warmup1_blank.near_hundred(89))  # Not within 10 of 100

    def test_pos_neg(self):
        self.assertTrue(warmup1_blank.pos_neg(1, -1, False))  # One positive, one negative
        self.assertTrue(warmup1_blank.pos_neg(-1, 1, False))  # One positive, one negative
        self.assertTrue(warmup1_blank.pos_neg(-4, -5, True))  # Both negative
        self.assertFalse(warmup1_blank.pos_neg(-4, 5, False)) # Both not matching conditions

    def test_not_string(self):
        self.assertEqual(warmup1_blank.not_string('candy'), 'not candy')   # Not added
        self.assertEqual(warmup1_blank.not_string('x'), 'not x')           # Not added
        self.assertEqual(warmup1_blank.not_string('not bad'), 'not bad')   # Already has "not"
        self.assertEqual(warmup1_blank.not_string('is not'), 'not is not') # Already has "not"

    def test_missing_char(self):
        self.assertEqual(warmup1_blank.missing_char('kitten', 1), 'ktten')  # Remove 'i'
        self.assertEqual(warmup1_blank.missing_char('kitten', 0), 'itten')  # Remove 'k'
        self.assertEqual(warmup1_blank.missing_char('kitten', 4), 'kittn')  # Remove 'e'

    def test_front_back(self):
        self.assertEqual(warmup1_blank.front_back('code'), 'eodc')   # Swap 'c' and 'e'
        self.assertEqual(warmup1_blank.front_back('a'), 'a')          # Single character
        self.assertEqual(warmup1_blank.front_back('ab'), 'ba')        # Two characters

    def test_front3(self):
        self.assertEqual(warmup1_blank.front3('Java'), 'JavJavJav')       # Normal case
        self.assertEqual(warmup1_blank.front3('Chocolate'), 'ChoChoCho')  # Normal case
        self.assertEqual(warmup1_blank.front3('abc'), 'abcabcabc')        # Less than 3

if __name__ == '__main__':
    unittest.main()
