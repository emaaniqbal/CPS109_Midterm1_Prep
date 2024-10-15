import unittest
import list2_blank


class TestLists2(unittest.TestCase):

    def test_count_evens(self):
        self.assertEqual(list2_blank.count_evens([2, 1, 2, 3, 4]), 3)  # Three evens
        self.assertEqual(list2_blank.count_evens([2, 2, 0]), 3)  # Three evens
        self.assertEqual(list2_blank.count_evens([1, 3, 5]), 0)  # No evens
        self.assertEqual(list2_blank.count_evens([]), 0)  # Empty list
        self.assertEqual(list2_blank.count_evens([1, 2, 3, 4, 5, 6]), 3)  # Three evens

    def test_big_diff(self):
        self.assertEqual(list2_blank.big_diff([10, 3, 5, 6]), 7)  # 10 - 3 = 7
        self.assertEqual(list2_blank.big_diff([7, 2, 10, 9]), 8)  # 10 - 2 = 8
        self.assertEqual(list2_blank.big_diff([2, 10, 7, 2]), 8)  # 10 - 2 = 8
        self.assertEqual(list2_blank.big_diff([1]), 0)  # Only one element
        self.assertEqual(list2_blank.big_diff([-1, -2, -3, -4]), 3)  # -1 - (-4) = 3
        self.assertEqual(list2_blank.big_diff([100, 0, 50, 25]), 100)  # 100 - 0 = 100
        self.assertEqual(list2_blank.big_diff([0, 0, 0]), 0)  # All zeros

    def test_centered_average(self):
        self.assertEqual(list2_blank.centered_average([1, 2, 3, 4, 100]), 3)  # Average ignoring 1 and 100
        self.assertEqual(list2_blank.centered_average([1, 1, 5, 5, 10, 8, 7]), 5)  # Average ignoring 1 and 10
        self.assertEqual(list2_blank.centered_average([-10, -4, -2, -4, -2, 0]), -3)  # Average ignoring -10 and 0
        self.assertEqual(list2_blank.centered_average([1, 1, 1, 1, 1]), 1)  # All ones
        self.assertEqual(list2_blank.centered_average([10, 5, 4]), 5)  # Average ignoring 10 and 4

    def test_sum13(self):
        self.assertEqual(list2_blank.sum13([1, 2, 2, 1]), 6)  # Sum = 6
        self.assertEqual(list2_blank.sum13([1, 1]), 2)  # Sum = 2
        self.assertEqual(list2_blank.sum13([1, 2, 2, 1, 13]), 6)  # 13 is ignored
        self.assertEqual(list2_blank.sum13([13, 1, 2, 13, 2]), 2)  # 13 is ignored, sum = 2
        self.assertEqual(list2_blank.sum13([13, 13, 2, 1]), 1)  # Only 1 is counted
        self.assertEqual(list2_blank.sum13([]), 0)  # Empty list
        self.assertEqual(list2_blank.sum13([13, 13]), 0)  # All are 13
        self.assertEqual(list2_blank.sum13([1, 2, 3, 13, 5, 6]), 6)  # Sum = 6

    def test_valid_cases(self):
        self.assertEqual(list2_blank.sum67([1, 2, 2]), 5)  # Simple case
        self.assertEqual(list2_blank.sum67([1, 2, 2, 6, 99, 99, 7]), 5)  # Ignore section starting with 6
        self.assertEqual(list2_blank.sum67([1, 1, 6, 7, 2]), 4)  # Ignore section starting with 6
        self.assertEqual(list2_blank.sum67([6, 1, 2, 3, 7, 4, 5]), 15)  # Ignore 1, 2, 3
        self.assertEqual(list2_blank.sum67([1, 2, 6, 7, 3, 4]), 10)  # Ignore 6 and 7
        self.assertEqual(list2_blank.sum67([6, 7, 1, 2]), 3)  # Ignore 6 and 7

    def test_edge_cases(self):
        self.assertEqual(list2_blank.sum67([]), 0)  # No numbers
        self.assertEqual(list2_blank.sum67([6]), 0)  # Only 6
        self.assertEqual(list2_blank.sum67([7]), 7)  # Only 7
        self.assertEqual(list2_blank.sum67([1, 6, 2, 7]), 1)  # Ignore section starting with 6
        self.assertEqual(list2_blank.sum67([1, 2, 3]), 6)  # All numbers are counted

    def test_has_22(self):
        self.assertTrue(list2_blank.has22([1, 2, 2]))  # True: 2 next to another 2
        self.assertFalse(list2_blank.has22([1, 2, 1, 2]))  # False: No 2s next to each other
        self.assertFalse(list2_blank.has22([2, 1, 2]))  # False: No 2s next to each other
        self.assertTrue(list2_blank.has22([2, 2, 1]))  # True: 2 next to another 2
        self.assertTrue(list2_blank.has22([2, 2]))  # True: 2 next to another 2
        self.assertFalse(list2_blank.has22([]))  # False: Empty list
        self.assertFalse(list2_blank.has22([1, 1, 1, 1]))  # False: No 2s in the list
        self.assertTrue(list2_blank.has22([1, 2, 2, 2, 1]))  # True: 2s next to each other in the list


if __name__ == '__main__':
    unittest.main()
