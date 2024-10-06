import unittest
from functions.tdd import sum_of_even, calculate_median, find_missing_number, remove_duplicates, first_non_repeating_char


class TestTDDApp(unittest.TestCase):
    def test_sum_of_even(self):
        # Test with a mix of even and odd numbers
        self.assertEqual(sum_of_even([1, 2, 3, 4, 5, 6]), 12)
        # Test with only even numbers
        self.assertEqual(sum_of_even([2, 4, 6]), 12)
        # Test with only odd numbers
        self.assertEqual(sum_of_even([1, 3, 5]), 0)
        # Test with an empty list
        self.assertEqual(sum_of_even([]), 0)

    def test_calculate_median(self):
        # Test with an odd-length list
        self.assertEqual(calculate_median([1, 2, 3]), 2)
        # Test with an even-length list
        self.assertEqual(calculate_median([1, 2, 3, 4]), 2.5)
        # Test with an unsorted list
        self.assertEqual(calculate_median([4, 1, 3, 2]), 2.5)
        # Test with None
        self.assertEqual(calculate_median(None), -1)

    def test_find_missing_number(self):
        # Test when there is a missing number
        self.assertTrue(find_missing_number([1, 2, 4, 5]), 3)
        # Test when no number is missing
        self.assertEqual(find_missing_number([1, 2, 3, 4, 5]), 'none')

    def test_remove_duplicates(self):
        # Test with a string containing duplicates
        self.assertEqual(remove_duplicates("aabbcc"), "abc")
        # Test with a string with no duplicates
        self.assertEqual(remove_duplicates("abc"), "abc")
        # Test with an empty string
        self.assertEqual(remove_duplicates(""), "")

    def test_first_non_repeating_char(self):
        # Test with a string with a non-repeating character
        self.assertEqual(first_non_repeating_char("swiss"), "w")
        # Test with all repeating characters
        self.assertIsNone(first_non_repeating_char("aabbcc"))
        # Test with an empty string
        self.assertIsNone(first_non_repeating_char(""))


if __name__ == '__main__':
    unittest.main()
