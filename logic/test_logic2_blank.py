import unittest
import logic2_blank


class TestFunctions(unittest.TestCase):

    def test_make_bricks(self):
        self.assertTrue(logic2_blank.make_bricks(3, 1, 8))
        self.assertFalse(logic2_blank.make_bricks(3, 1, 9))
        self.assertTrue(logic2_blank.make_bricks(3, 2, 10))
        self.assertTrue(logic2_blank.make_bricks(0, 2, 10))
        self.assertFalse(logic2_blank.make_bricks(5, 1, 11))
        self.assertTrue(logic2_blank.make_bricks(7, 1, 11))

    def test_lone_sum(self):
        self.assertEqual(logic2_blank.lone_sum(1, 2, 3), 6)
        self.assertEqual(logic2_blank.lone_sum(3, 2, 3), 2)
        self.assertEqual(logic2_blank.lone_sum(3, 3, 3), 0)
        self.assertEqual(logic2_blank.lone_sum(1, 1, 2), 2)
        self.assertEqual(logic2_blank.lone_sum(4, 5, 5), 4)
        self.assertEqual(logic2_blank.lone_sum(10, 20, 10), 20)

    def test_lucky_sum(self):
        self.assertEqual(logic2_blank.lucky_sum(1, 2, 3), 6)
        self.assertEqual(logic2_blank.lucky_sum(1, 2, 13), 3)
        self.assertEqual(logic2_blank.lucky_sum(1, 13, 3), 1)
        self.assertEqual(logic2_blank.lucky_sum(13, 2, 3), 0)
        self.assertEqual(logic2_blank.lucky_sum(1, 13, 13), 1)
        self.assertEqual(logic2_blank.lucky_sum(2, 3, 5), 10)

    def test_no_teen_sum(self):
        self.assertEqual(logic2_blank.no_teen_sum(1, 2, 3), 6)
        self.assertEqual(logic2_blank.no_teen_sum(2, 13, 1), 3)
        self.assertEqual(logic2_blank.no_teen_sum(2, 1, 14), 3)
        self.assertEqual(logic2_blank.no_teen_sum(15, 16, 17), 31)
        self.assertEqual(logic2_blank.no_teen_sum(19, 19, 19), 0)
        self.assertEqual(logic2_blank.no_teen_sum(10, 12, 13), 22)

    def test_fix_teen(self):
        self.assertEqual(logic2_blank.fix_teen(13), 0)
        self.assertEqual(logic2_blank.fix_teen(15), 15)
        self.assertEqual(logic2_blank.fix_teen(17), 0)
        self.assertEqual(logic2_blank.fix_teen(16), 16)
        self.assertEqual(logic2_blank.fix_teen(10), 10)

    def test_round_sum(self):
        self.assertEqual(logic2_blank.round_sum(16, 17, 18), 60)
        self.assertEqual(logic2_blank.round_sum(12, 13, 14), 30)
        self.assertEqual(logic2_blank.round_sum(6, 4, 4), 10)
        self.assertEqual(logic2_blank.round_sum(15, 25, 35), 80)
        self.assertEqual(logic2_blank.round_sum(0, 5, 10), 20)
        self.assertEqual(logic2_blank.round_sum(11, 21, 31), 60)

    def test_round10(self):
        self.assertEqual(logic2_blank.round10(12), 10)
        self.assertEqual(logic2_blank.round10(15), 20)
        self.assertEqual(logic2_blank.round10(27), 30)
        self.assertEqual(logic2_blank.round10(30), 30)
        self.assertEqual(logic2_blank.round10(44), 40)
        self.assertEqual(logic2_blank.round10(55), 60)

    def test_close_far(self):
        self.assertTrue(logic2_blank.close_far(1, 2, 10))
        self.assertFalse(logic2_blank.close_far(1, 2, 3))
        self.assertTrue(logic2_blank.close_far(4, 1, 3))
        self.assertFalse(logic2_blank.close_far(5, 4, 6))
        self.assertFalse(logic2_blank.close_far(10, 8, 12))
        self.assertTrue(logic2_blank.close_far(0, 1, 3))

    def test_make_chocolate(self):
        self.assertEqual(logic2_blank.make_chocolate(4, 1, 9), 4)
        self.assertEqual(logic2_blank.make_chocolate(4, 1, 10), -1)
        self.assertEqual(logic2_blank.make_chocolate(4, 1, 7), 2)
        self.assertEqual(logic2_blank.make_chocolate(0, 2, 10), 0)
        self.assertEqual(logic2_blank.make_chocolate(3, 2, 8), 3)
        self.assertEqual(logic2_blank.make_chocolate(1, 1, 6), -1)


if __name__ == '__main__':
    unittest.main(exit=True)
