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
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        """
        This method takes a license plate string and a list of words as input
        and returns the shortest word from the list that contains all the
        characters in the license plate.

        Time Complexity = O(n*m) ... (Runtime: 58ms - Beats 98.18%)
        Space Complexity = O(1) ... (Memory: 14.2mb - Beats 49.27%)
        """
        # Initialize the output variable as an empty string
        completing_words_output = ""

        for word in words:  # Iterate over each word in the "words" list
            flag = True  # Set the flag to True initially
            # Convert the word to lowercase for case-insensitive comparison
            word = word.lower()
            # Convert the license plate to lowercase as well
            licensePlate = licensePlate.lower()

            # Iterate over each character in the license plate
            for char in licensePlate:
                char = char.lower()  # Convert the character to lowercase

                if char in "01234 56789":  # Skip any digits or spaces
                    continue
                # Check if i is in the word and appears at least as many times
                elif (char in word) and (word.count(char) >= licensePlate.count(char)):
                    continue
                # If not in the word or appears fewer times, set flag to False
                else:
                    flag = False
                    break

            # If flag is True & word is shorter than current output, update output
            if flag == True and len(completing_words_output) > len(word):
                completing_words_output = word
            # If flag is True and output is an empty string, update the output
            elif flag == True and completing_words_output == "":
                completing_words_output = word

        return completing_words_output  # Return the output string
