import unittest
import logic1_blank


class TestLogicFunctions(unittest.TestCase):
    def test_cigar_party(self):
        self.assertEqual(logic1_blank.cigar_party(30, False), False)
        self.assertEqual(logic1_blank.cigar_party(50, False), True)
        self.assertEqual(logic1_blank.cigar_party(70, True), True)
        self.assertEqual(logic1_blank.cigar_party(60, True), True)
        self.assertEqual(logic1_blank.cigar_party(40, False), True)
        self.assertEqual(logic1_blank.cigar_party(61, False), False)
        self.assertEqual(logic1_blank.cigar_party(39, True), False)

    def test_date_fashion(self):
        self.assertEqual(logic1_blank.date_fashion(5, 10), 2)
        self.assertEqual(logic1_blank.date_fashion(5, 2), 0)
        self.assertEqual(logic1_blank.date_fashion(5, 5), 1)
        self.assertEqual(logic1_blank.date_fashion(8, 3), 2)
        self.assertEqual(logic1_blank.date_fashion(1, 7), 0)
        self.assertEqual(logic1_blank.date_fashion(10, 10), 2)

    def test_squirrel_play(self):
        self.assertEqual(logic1_blank.squirrel_play(70, False), True)
        self.assertEqual(logic1_blank.squirrel_play(95, False), False)
        self.assertEqual(logic1_blank.squirrel_play(95, True), True)
        self.assertEqual(logic1_blank.squirrel_play(60, False), True)
        self.assertEqual(logic1_blank.squirrel_play(90, False), True)
        self.assertEqual(logic1_blank.squirrel_play(100, True), True)
        self.assertEqual(logic1_blank.squirrel_play(101, True), False)
        self.assertEqual(logic1_blank.squirrel_play(59, False), False)

    def test_caught_speeding(self):
        self.assertEqual(logic1_blank.caught_speeding(60, False), 0)
        self.assertEqual(logic1_blank.caught_speeding(65, False), 1)
        self.assertEqual(logic1_blank.caught_speeding(65, True), 0)
        self.assertEqual(logic1_blank.caught_speeding(80, False), 1)
        self.assertEqual(logic1_blank.caught_speeding(81, False), 2)
        self.assertEqual(logic1_blank.caught_speeding(85, True), 1)
        self.assertEqual(logic1_blank.caught_speeding(90, True), 2)

    def test_sorta_sum(self):
        self.assertEqual(logic1_blank.sorta_sum(3, 4), 7)
        self.assertEqual(logic1_blank.sorta_sum(9, 4), 20)
        self.assertEqual(logic1_blank.sorta_sum(10, 11), 21)
        self.assertEqual(logic1_blank.sorta_sum(5, 5), 20)
        self.assertEqual(logic1_blank.sorta_sum(15, 5), 20)
        self.assertEqual(logic1_blank.sorta_sum(2, 3), 5)

    def test_alarm_clock(self):
        self.assertEqual(logic1_blank.alarm_clock(1, False), '7:00')
        self.assertEqual(logic1_blank.alarm_clock(5, False), '7:00')
        self.assertEqual(logic1_blank.alarm_clock(0, False), '10:00')
        self.assertEqual(logic1_blank.alarm_clock(6, True), 'off')
        self.assertEqual(logic1_blank.alarm_clock(3, True), '10:00')
        self.assertEqual(logic1_blank.alarm_clock(5, True), '10:00')

    def test_love6(self):
        self.assertEqual(logic1_blank.love6(6, 4), True)
        self.assertEqual(logic1_blank.love6(4, 5), False)
        self.assertEqual(logic1_blank.love6(1, 5), True)
        self.assertEqual(logic1_blank.love6(2, 4), False)
        self.assertEqual(logic1_blank.love6(7, -1), True)
        self.assertEqual(logic1_blank.love6(0, 6), True)

    def test_in1to10(self):
        self.assertEqual(logic1_blank.in1to10(5, False), True)
        self.assertEqual(logic1_blank.in1to10(11, False), False)
        self.assertEqual(logic1_blank.in1to10(11, True), True)
        self.assertEqual(logic1_blank.in1to10(0, True), True)
        self.assertEqual(logic1_blank.in1to10(10, True), True)
        self.assertEqual(logic1_blank.in1to10(1, False), True)
        self.assertEqual(logic1_blank.in1to10(1, True), True)

    def test_near_ten(self):
        self.assertEqual(logic1_blank.near_ten(12), True)
        self.assertEqual(logic1_blank.near_ten(17), False)
        self.assertEqual(logic1_blank.near_ten(19), True)
        self.assertEqual(logic1_blank.near_ten(20), True)
        self.assertEqual(logic1_blank.near_ten(22), True)
        self.assertEqual(logic1_blank.near_ten(23), False)
        self.assertEqual(logic1_blank.near_ten(30), True)
        self.assertEqual(logic1_blank.near_ten(31), True)
        self.assertEqual(logic1_blank.near_ten(32), False)


if __name__ == '__main__':
    unittest.main(exit=True)
