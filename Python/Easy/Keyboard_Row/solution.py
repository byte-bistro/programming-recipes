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
    def findWords(self, words: List[str]) -> List[str]:
        """
        This function works by looping through each word in the input list,
        checking if it can be typed using only one row of a QWERTY keyboard.
        If the word can be typed using only one row of the keyboard, it is
        added to an output list.

        Time Complexity = O(n*m) ... (Runtime: 27ms - Beats 88.49%)
        Space Complexity = O(1) ... (Memory: 13.9mb - Beats 08.21%)
        """

        # Define three strings that represent the three rows of letters on a QWERTY keyboard
        first_row, second_row, third_row = "qwertyuiop", "asdfghjkl", "zxcvbnm"

        # Create an empty list to hold the output
        output_list = []

        # Loop through each word in the input list
        for word in words:
            # Initialize a boolean variable to keep track of whether the word can be typed using one row of the keyboard
            flag = True
            # Get the first letter of the word and convert it to lowercase
            first_letter = word[0].lower()

            # Determine which row of the keyboard the first letter belongs to
            if first_letter in first_row:
                expected_row = first_row
            elif first_letter in second_row:
                expected_row = second_row
            else:
                expected_row = third_row

            # Loop through each character in the word
            for character in word:
                # Check if the character can be typed using the expected row of the keyboard (where the first letter belongs)
                if character.lower() not in expected_row:
                    # If not, set the flag to False and break out of the loop
                    flag = False
                    break

            # If the flag is still True, the entire word can be typed using one row of the keyboard, so add it to the output list
            if flag == True:
                output_list.append(word)

        # Return the list of words that can be typed using one row of the keyboard
        return output_list
