import unittest
import lists2_blank

class TestLists2(unittest.TestCase):

    def test_count_evens(self):
        self.assertEqual(lists2_blank.count_evens([2, 1, 2, 3, 4]), 3)      # Three evens
        self.assertEqual(lists2_blank.count_evens([2, 2, 0]), 3)            # Three evens
        self.assertEqual(lists2_blank.count_evens([1, 3, 5]), 0)            # No evens
        self.assertEqual(lists2_blank.count_evens([]), 0)                   # Empty list
        self.assertEqual(lists2_blank.count_evens([1, 2, 3, 4, 5, 6]), 3)  # Three evens

    def test_big_diff(self):
        self.assertEqual(lists2_blank.big_diff([10, 3, 5, 6]), 7)           # 10 - 3 = 7
        self.assertEqual(lists2_blank.big_diff([7, 2, 10, 9]), 8)           # 10 - 2 = 8
        self.assertEqual(lists2_blank.big_diff([2, 10, 7, 2]), 8)           # 10 - 2 = 8
        self.assertEqual(lists2_blank.big_diff([1]), 0)                      # Only one element
        self.assertEqual(lists2_blank.big_diff([-1, -2, -3, -4]), 3)        # -1 - (-4) = 3
        self.assertEqual(lists2_blank.big_diff([100, 0, 50, 25]), 100)      # 100 - 0 = 100
        self.assertEqual(lists2_blank.big_diff([0, 0, 0]), 0)                # All zeros

    def test_centered_average(self):
        self.assertEqual(lists2_blank.centered_average([1, 2, 3, 4, 100]), 3)       # Average ignoring 1 and 100
        self.assertEqual(lists2_blank.centered_average([1, 1, 5, 5, 10, 8, 7]), 5)  # Average ignoring 1 and 10
        self.assertEqual(lists2_blank.centered_average([-10, -4, -2, -4, -2, 0]), -3) # Average ignoring -10 and 0
        self.assertEqual(lists2_blank.centered_average([1, 1, 1, 1, 1]), 1)           # All ones
        self.assertEqual(lists2_blank.centered_average([10, 5, 4]), 5)                # Average ignoring 10 and 4

    def test_sum13(self):
        self.assertEqual(lists2_blank.sum13([1, 2, 2, 1]), 6)                  # Sum = 6
        self.assertEqual(lists2_blank.sum13([1, 1]), 2)                        # Sum = 2
        self.assertEqual(lists2_blank.sum13([1, 2, 2, 1, 13]), 6)             # 13 is ignored
        self.assertEqual(lists2_blank.sum13([13, 1, 2, 13, 2]), 2)            # 13 is ignored, sum = 2
        self.assertEqual(lists2_blank.sum13([13, 13, 2, 1]), 1)               # Only 1 is counted
        self.assertEqual(lists2_blank.sum13([]), 0)                            # Empty list
        self.assertEqual(lists2_blank.sum13([13, 13]), 0)                      # All are 13
        self.assertEqual(lists2_blank.sum13([1, 2, 3, 13, 5, 6]), 6)          # Sum = 6

if __name__ == '__main__':
    unittest.main()

