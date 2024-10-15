import unittest
import lists1_blank


class TestLists1(unittest.TestCase):

    def test_first_last6(self):
        self.assertTrue(lists1_blank.first_last6([1, 2, 6]))  # 6 is the last element
        self.assertTrue(lists1_blank.first_last6([6, 1, 2, 3]))  # 6 is the first element
        self.assertFalse(lists1_blank.first_last6([13, 6, 1, 2, 3]))  # 6 is neither first nor last
        self.assertTrue(lists1_blank.first_last6([6]))  # Single element array

    def test_same_first_last(self):
        self.assertFalse(lists1_blank.same_first_last([1, 2, 3]))  # First and last are different
        self.assertTrue(lists1_blank.same_first_last([1, 2, 3, 1]))  # First and last are the same
        self.assertTrue(lists1_blank.same_first_last([1, 2, 1]))  # First and last are the same
        self.assertTrue(lists1_blank.same_first_last([7]))  # Single element array
        self.assertFalse(lists1_blank.same_first_last([]))  # Empty array

    def test_common_end(self):
        self.assertTrue(lists1_blank.common_end([1, 2, 3], [7, 3]))  # Same last element
        self.assertFalse(lists1_blank.common_end([1, 2, 3], [7, 3, 2]))  # Different first and last
        self.assertTrue(lists1_blank.common_end([1, 2, 3], [1, 3]))  # Same first element
        self.assertTrue(lists1_blank.common_end([4], [4]))  # Same first and last element
        self.assertFalse(lists1_blank.common_end([5, 6], [7, 5]))  # Different first and last

    def test_sum3(self):
        self.assertEqual(lists1_blank.sum3([1, 2, 3]), 6)  # Sum is 6
        self.assertEqual(lists1_blank.sum3([5, 11, 2]), 18)  # Sum is 18
        self.assertEqual(lists1_blank.sum3([7, 0, 0]), 7)  # Sum is 7

    def test_rotate_left3(self):
        self.assertEqual(lists1_blank.rotate_left3([1, 2, 3]), [2, 3, 1])  # Rotated left
        self.assertEqual(lists1_blank.rotate_left3([5, 11, 9]), [11, 9, 5])  # Rotated left
        self.assertEqual(lists1_blank.rotate_left3([7, 0, 0]), [0, 0, 7])  # Rotated left

    def test_reverse3(self):
        self.assertEqual(lists1_blank.reverse3([1, 2, 3]), [3, 2, 1])  # Reversed array
        self.assertEqual(lists1_blank.reverse3([5, 11, 9]), [9, 11, 5])  # Reversed array

    def test_max_end3(self):
        self.assertEqual(lists1_blank.max_end3([1, 2, 3]), [3, 3, 3])  # Last element is greater
        self.assertEqual(lists1_blank.max_end3([11, 5, 9]), [11, 11, 11])  # First element is greater
        self.assertEqual(lists1_blank.max_end3([2, 11, 3]), [11, 11, 11])  # First is less than last

    def test_sum2(self):
        self.assertEqual(lists1_blank.sum2([1, 2, 3]), 3)  # Sum of first two
        self.assertEqual(lists1_blank.sum2([1, 1]), 2)  # Sum of two ones
        self.assertEqual(lists1_blank.sum2([1, 1, 1, 1]), 2)  # Sum of first two
        self.assertEqual(lists1_blank.sum2([5]), 5)  # Only one element
        self.assertEqual(lists1_blank.sum2([]), 0)  # Empty array

    def test_middle_way(self):
        self.assertEqual(lists1_blank.middle_way([1, 2, 3], [4, 5, 6]), [2, 5])  # Middle elements
        self.assertEqual(lists1_blank.middle_way([7, 7, 7], [3, 8, 0]), [7, 8])  # Middle elements
        self.assertEqual(lists1_blank.middle_way([5, 2, 9], [1, 4, 5]), [2, 4])  # Middle elements

    def test_make_ends(self):
        self.assertEqual(lists1_blank.make_ends([1, 2, 3]), [1, 3])  # First and last
        self.assertEqual(lists1_blank.make_ends([1, 2, 3, 4]), [1, 4])  # First and last
        self.assertEqual(lists1_blank.make_ends([7, 4, 6, 2]), [7, 2])  # First and last
        self.assertEqual(lists1_blank.make_ends([5]), [5, 5])  # Only one element

    def test_has23(self):
        self.assertTrue(lists1_blank.has23([2, 5]))  # Contains 2
        self.assertTrue(lists1_blank.has23([4, 3]))  # Contains 3
        self.assertFalse(lists1_blank.has23([4, 5]))  # Contains neither

    def test_valid_xyz(self):
        self.assertTrue(lists1_blank.xyz_there('abcxyz'))  # Valid occurrence of "xyz"
        self.assertTrue(lists1_blank.xyz_there('xyz.abc'))  # "xyz" is not preceded by a period
        self.assertTrue(lists1_blank.xyz_there('xyz'))  # "xyz" at the start is valid
        self.assertTrue(lists1_blank.xyz_there('xxyz'))  # "xyz" is valid since it's not preceded by a period

    def test_invalid_xyz(self):
        self.assertFalse(lists1_blank.xyz_there('abc.xyz'))  # "xyz" is preceded by a period
        self.assertFalse(lists1_blank.xyz_there('x.xyz'))  # "xyz" is preceded by a period
        self.assertFalse(lists1_blank.xyz_there('xyz.xyz'))  # First "xyz" is valid but second is preceded by a period

    def test_edge_cases(self):
        self.assertTrue(lists1_blank.xyz_there(''))  # Empty string, no "xyz" at all
        self.assertFalse(lists1_blank.xyz_there('.xyz'))  # "xyz" is preceded by a period
        self.assertFalse(lists1_blank.xyz_there('...xyz'))  # "xyz" is preceded by a period


if __name__ == '__main__':
    unittest.main()
