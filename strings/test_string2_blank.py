import unittest
import strings2_blank

class TestStrings2(unittest.TestCase):

    def test_double_char(self):
        self.assertEqual(strings2_blank.double_char('The'), 'TThhee')         # Basic case
        self.assertEqual(strings2_blank.double_char('AAbb'), 'AAAAbbbb')     # Repeated characters
        self.assertEqual(strings2_blank.double_char('Hi-There'), 'HHii--TThheerree') # Mixed characters

    def test_count_hi(self):
        self.assertEqual(strings2_blank.count_hi('abc hi ho'), 1)            # One occurrence
        self.assertEqual(strings2_blank.count_hi('ABChi hi'), 2)             # Two occurrences
        self.assertEqual(strings2_blank.count_hi('hihi'), 2)                 # Two occurrences (overlapping)

    def test_cat_dog(self):
        self.assertTrue(strings2_blank.cat_dog('catdog'))                     # Equal counts
        self.assertFalse(strings2_blank.cat_dog('catcat'))                    # Unequal counts
        self.assertTrue(strings2_blank.cat_dog('1cat1cadodog'))               # Equal counts with numbers

    def test_count_code(self):
        self.assertEqual(strings2_blank.count_code('aaacodebbb'), 1)          # One occurrence
        self.assertEqual(strings2_blank.count_code('codexxcode'), 2)          # Two occurrences
        self.assertEqual(strings2_blank.count_code('cozexxcope'), 2)          # Two occurrences
        self.assertEqual(strings2_blank.count_code('cooexxcope'), 2)          # Two occurrences
        self.assertEqual(strings2_blank.count_code(''), 0)                     # No occurrences

    def test_end_other(self):
        self.assertTrue(strings2_blank.end_other('Hiabc', 'abc'))             # 'abc' at the end of 'Hiabc'
        self.assertTrue(strings2_blank.end_other('AbC', 'HiaBc'))             # Case insensitive match
        self.assertFalse(strings2_blank.end_other('abc', 'abXabc'))           # Not at the end

if __name__ == '__main__':
    unittest.main()


