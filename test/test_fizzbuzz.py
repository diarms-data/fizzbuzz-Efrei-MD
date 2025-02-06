import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
from main import fizzbuzz 


class TestFizzBuzz(unittest.TestCase):
    def test_multiples_of_3(self):
        """Test que les multiples de 3 retournent 'Fizz'"""
        self.assertEqual(fizzbuzz(10)[2], "FizzFizz")   # 3 -> "FizzFizz"
        self.assertEqual(fizzbuzz(10)[5], "Fizz")   # 6 -> "Fizz"

    def test_contains_3(self):
        """Test que les nombres contenant '3' retournent 'Fizz'"""
        self.assertEqual(fizzbuzz(35)[2], "FizzFizz")  # 3 -> "FizzFizz"
        self.assertEqual(fizzbuzz(35)[12], "Fizz")     # 13 -> "Fizz"

    def test_multiples_of_5(self):
        """Test que les multiples de 5 retournent 'Buzz'"""
        self.assertEqual(fizzbuzz(10)[4], "BuzzBuzz")  # 5 -> "BuzzBuzz"
        self.assertEqual(fizzbuzz(10)[9], "Buzz")      # 10 -> "Buzz"

    def test_contains_5(self):
        """Test que les nombres contenant '5' retournent 'Buzz'"""
        self.assertEqual(fizzbuzz(55)[14], "FizzBuzzBuzz")  # 15 -> "FizzBuzzBuzz"
        self.assertEqual(fizzbuzz(55)[49], "BuzzBuzz")      # 50 -> "BuzzBuzz"

    def test_regular_numbers(self):
        """Test que les nombres qui ne sont ni multiples de 3/5 ni contiennent 3/5 restent normaux"""
        self.assertEqual(fizzbuzz(10)[0], 1)  # 1 -> 1
        self.assertEqual(fizzbuzz(10)[1], 2)  # 2 -> 2
        self.assertEqual(fizzbuzz(10)[6], 7)  # 7 -> 7
        self.assertEqual(fizzbuzz(10)[7], 8)  # 8 -> 8

if __name__ == '__main__':
    unittest.main()

