import unittest
import addtional_questions

class TestFunctions(unittest.TestCase):

    def test_comp1(self):
        self.assertEqual(addtional_questions.comp1([1, 2, 3]), [1, 8, 27])

    def test_comp2(self):
        self.assertEqual(addtional_questions.comp2([1, 2, 3]), {1: 3, 2: 6, 3: 9})
        self.assertEqual(addtional_questions.comp2([4, 5]), {4: 12, 5: 15})

    def test_comp3(self):
        self.assertEqual(addtional_questions.comp3([1, 2, 3]), {3: 1, 6: 2, 9: 3})
        self.assertEqual(addtional_questions.comp3([4, 5]), {12: 4, 15: 5})

    def test_count_duplicates_v1(self):
        self.assertEqual(addtional_questions.count_duplicates_v1([1, 2, 3, 4]), 0)
        self.assertEqual(addtional_questions.count_duplicates_v1([2, 4, 3, 3, 1, 4]), 2)

    def test_str_compaare(self):
        self.assertFalse(addtional_questions.str_compaare('hello', 'world', 0))
        self.assertTrue(addtional_questions.str_compaare('hello', 'world!', 1))
        self.assertTrue(addtional_questions.str_compaare('hi', 'hello', 3))
        self.assertFalse(addtional_questions.str_compaare('apple', 'banana', 3))

    def test_sum_of_digits(self):
        self.assertEqual(addtional_questions.sum_of_digits('abcl2341'), 10)
        self.assertEqual(addtional_questions.sum_of_digits('hi'), 0)

    def test_smallest_five(self):
        self.assertEqual(addtional_questions.smallest_five([1, 2, 3, 4, 5, 6, 7]), [1, 2, 3, 4, 5])
        self.assertEqual(addtional_questions.smallest_five([6, 2, 11, 12, 7, 12, -3]), [-3, 2, 6, 7, 11])

    def test_is_palindrome(self):
        self.assertTrue(addtional_questions.is_palindrome('noon'))
        self.assertTrue(addtional_questions.is_palindrome('racecar'))
        self.assertFalse(addtional_questions.is_palindrome('dented'))

    def test_prnt_lastname(self):
        with self.assertRaises(ValueError):
            self.assertFalse(addtional_questions.prnt_lastname("ALEX12"))
        # Cannot test print statements, better to refactor to return a list

    def test_calculate_average(self):
        self.assertEqual(addtional_questions.calculate_average([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(addtional_questions.calculate_average([10, 20, 30]), 20.0)

    def test_long_greeting(self):
        self.assertEqual(addtional_questions.long_greeting(['Cat', 'Dog']), 'Hello Cat! Hello Dog! ')

    def test_is_IP_address(self):
        self.assertTrue(addtional_questions.is_IP_address('192.168.1.1'))
        self.assertFalse(addtional_questions.is_IP_address('abc.def.ghi.jkl'))


if __name__ == '__main__':
    unittest.main(exit=True)
