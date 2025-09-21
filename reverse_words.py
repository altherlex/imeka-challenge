import unittest
import os

def reverse_words_to_file(input_string: str, output_file: str = "output.txt"):
    """
    Takes an input string, reverses the order of words,
    and writes the result to a text file.
    """
    words = input_string.split()
    reversed_words = " ".join(reversed(words))

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(reversed_words)

    print(f"Reversed string saved to {output_file}")


class TestReverseWords(unittest.TestCase):
    def test_reverse_words(self):
        test_input = "Combining advanced white matter imaging with AI"
        expected_output = "AI with imaging matter white advanced Combining"
        test_file = "test_output.txt"

        # Run the function
        reverse_words_to_file(test_input, test_file)

        # Read file back
        with open(test_file, "r", encoding="utf-8") as f:
            result = f.read()

        # Check content
        self.assertEqual(result, expected_output)

        # Cleanup
        if os.path.exists(test_file):
            os.remove(test_file)

if __name__ == "__main__":
    unittest.main()
