import time
import unittest

from .fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def test_input_one_return_one(self):
        expect = '1'
        actual = fizzbuzz(1)
        time.sleep(1)
        self.assertEqual(actual , expect)

    def test_input_three_return_fizz(self):
        expect = 'fizz'
        actual = fizzbuzz(3)
        time.sleep(1)
        self.assertEqual(actual , expect)

    def test_input_five_return_buzz(self):
        expect = 'buzz'
        time.sleep(1)
        actual = fizzbuzz(5)
        self.assertEqual(actual , expect)

    def test_input_six_return_fizz(self):
        expect = 'fizz'
        time.sleep(1)
        actual = fizzbuzz(6)
        self.assertEqual(actual , expect)

    def test_input_fifthteen_return_fizzbuzz(self):
        expect = 'fizzbuzz'
        time.sleep(1)
        actual = fizzbuzz(15)
        self.assertEqual(actual , expect)

    def test_input_string_should_throw_error(self):
        time.sleep(1)
        fizzbuzz('1')

    def test_failed_test(self):
        expect = 'fizz'
        actual = fizzbuzz(1)
        time.sleep(1)
        self.assertEqual(actual, expect)

    @unittest.skip("demonstrating skipping")
    def test_skipped_naja(self):
        expect = 'something'
        time.sleep(1)
        self.assertEqual(expect, expect)
