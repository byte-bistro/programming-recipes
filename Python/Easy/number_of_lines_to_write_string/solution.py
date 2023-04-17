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


from string import ascii_lowercase as alphabets


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        """
        Returns the number of lines needed to write a given string "s" using
        a given list "widths" of letter widths, assuming that each line can
        hold up to 100 units of width. The function returns a list containing
        the total number of lines used and the width of the last line used.

        Time Complexity = O(n) ... (Runtime: 24ms - Beats 89.94%)
        Space Complexity = O(1) ... (Memory: 13.9mb - Beats 55.97%)
        """
        # Create a dictionary to map each letter to its corresponding width
        english_alphabets = {}
        for i in range(26):
            english_alphabets[alphabets[i]] = widths[i]

        # Initialize the current width and total lines to 0 and 1 respectively
        current_width = 0
        total_lines = 1

        # Loop through each character in the input string s
        for i in s:
            # Add the width of the current character to the current width
            current_width = current_width + english_alphabets[i]

            # If current width exceeds 100, increment total lines and reset current width
            if current_width > 100:
                total_lines = total_lines + 1
                current_width = english_alphabets[i]

        # Return a list containing total lines and width of last line
        return [total_lines, current_width]
