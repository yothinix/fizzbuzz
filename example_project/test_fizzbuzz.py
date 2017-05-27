import unittest

from fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def test_input_one_return_one(self):
        expect = '1'
        actual = fizzbuzz(1)
        self.assertEqual(actual , expect)

    def test_input_three_return_fizz(self):
        expect = 'fizz'
        actual = fizzbuzz(3)
        self.assertEqual(actual , expect)

    def test_input_five_return_buzz(self):
        expect = 'buzz'
        actual = fizzbuzz(5)
        self.assertEqual(actual , expect)

    def test_input_six_return_fizz(self):
        expect = 'fizz'
        actual = fizzbuzz(6)
        self.assertEqual(actual , expect)

    def test_input_fifthteen_return_fizzbuzz(self):
        expect = 'fizzbuzz'
        actual = fizzbuzz(15)
        self.assertEqual(actual , expect)

    def test_input_string_should_throw_error(self):
        fizzbuzz('1')

    def test_failed_test(self):
        expect = 'fizz'
        actual = fizzbuzz(1)
        self.assertEqual(actual, expect)

