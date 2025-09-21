import unittest
from io import StringIO
import sys

def fizz_buzz(n: int):
    for i in range(1, n + 1):
        num_str = str(i)
        if '6' in num_str:
            print("Buzz-Fizz")
        elif i % 3 == 0 and i % 5 == 0:
            print("Fizz-Buzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


class TestFizzBuzzModified(unittest.TestCase):
    def test_small_range(self):
        # Capture output
        captured_output = StringIO()
        sys.stdout = captured_output

        fizz_buzz(36)

        # Reset stdout
        sys.stdout = sys.__stdout__

        # Split printed lines
        result = captured_output.getvalue().strip().split("\n")

        expected = [
            "1", "2", "Fizz", "4", "Buzz", "Buzz-Fizz", "7", "8", 
            "Fizz", "Buzz", "11", "Fizz", "13", "14", 
            "Fizz-Buzz", "Buzz-Fizz", "17", "Fizz", "19", "Buzz", 
            "Fizz", "22", "23", "Fizz", "Buzz", "Buzz-Fizz", 
            "Fizz", "28", "29", "Fizz-Buzz", "31", "32", 
            "Fizz", "34", "Buzz", "Buzz-Fizz"
        ]

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
