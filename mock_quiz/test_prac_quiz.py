import unittest
import prac_quiz

class TestQuizzes(unittest.TestCase):

    def test_n_sided_polygon(self):
        """Test the n_sided_polygon function."""
        # Testing various polygons
        self.assertAlmostEqual(prac_quiz.n_sided_polygon(4, 5.0), 25.0)
        self.assertAlmostEqual(prac_quiz.nn_sided_polygon(3, 6), 15.588457268119896)
        self.assertAlmostEqual(prac_quiz.nn_sided_polygon(5, 10), 72.69017017488349)
        self.assertAlmostEqual(prac_quiz.nn_sided_polygon(6, 4), 27.712812921102035)
        self.assertAlmostEqual(prac_quiz.nn_sided_polygon(8, 2), 6.928203230275509)
        self.assertAlmostEqual(prac_quiz.nn_sided_polygon(0, 5), 0.0)

    def test_int_reader(self):
        """Test the int_reader function."""
        self.assertEqual(prac_quiz.nint_reader(12), "The factors of 12 between 2 and 8 are 2, 3, 4, 6.")
        self.assertEqual(prac_quiz.nint_reader(28), "The factors of 28 between 2 and 8 are 4, 7.")
        self.assertIsNone(prac_quiz.nint_reader(15))
        self.assertIsNone(prac_quiz.nint_reader(1))
        self.assertEqual(prac_quiz.nint_reader(64), "The factors of 64 between 2 and 8 are 4, 8.")
        self.assertEqual(prac_quiz.nint_reader(9), "The factors of 9 between 2 and 8 are 3.")

    def test_valid_password(self):
        """Test the valid_password function."""
        self.assertEqual(prac_quiz.nvalid_password("123", "123"), "Password not complex enough")
        self.assertEqual(prac_quiz.nvalid_password("ACVbAY2034", "ACVbAY2034"), "Password changed successfully")
        self.assertEqual(prac_quiz.nvalid_password("123456789", "123456789"), "Password not complex enough")

    def test_bats_bogs(self):
        """Test the bats_bogs function."""
        self.assertEqual(prac_quiz.nbats_bogs(24), [
            1, 2, 3, "Bats", 5, "Bogs", 7, "Bats", 
            9, 10, "Bogs", 11, "Bats", 13, 14, "Bogs", 
            15, "Bats", 17, 18, "Bats", 20, 21, "Bogs", 
            23, "BatsBogs"
        ])
        self.assertEqual(prac_quiz.nbats_bogs(0), "N must be greater than 1")
        self.assertEqual(prac_quiz.nbats_bogs(56), "Too much work, no thanks")
        self.assertEqual(prac_quiz.nbats_bogs(1), "N must be greater than 1")


    if __name__ == '__main__':
        unittest.main(exit=True)


