"""
# Author: Ashwin Raj <thisisashwinraj@gmail.com>
# License: MIT License
# Discussions-to: github.com/thisisashwinraj/programming-recipes/discussions

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        """
        Given a list of words, define a dictionary to map each alphabet to
        its Morse code and return the number of unique Morse code
        representations of the input words.

        Time Complexity = O(n*m) ... (Runtime: 31ms - Beats 90.35%)
        Space Complexity = O(n*m) ... (Memory: 13.9mb - Beats 59.17%)
        """
        morse_code_dict = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--..",
        }

        # Create an empty set to store the Morse code transformations
        morse_code_transformation_set = set()

        # Loop through each word in the input list
        for word in words:
            # Create an empty string to store the Morse code transformation
            morse_code_word = ""

            # Loop through each character in the current word
            for char in word:
                # Append Morse code of curr char to Morse code of curr word
                morse_code_word += morse_code_dict[char]

            # Add the Morse code of the current word to the set
            morse_code_transformation_set.add(morse_code_word)

        del morse_code_word
        # Return the number of unique Morse code transformations
        return len(morse_code_transformation_set)
