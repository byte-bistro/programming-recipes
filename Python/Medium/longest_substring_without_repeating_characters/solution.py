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
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Returns the length of the longest substring without repeating characters 
        in the given input string.

        Time Complexity = O(n) ... (Runtime: 61ms - Beats 74.36%)
        Space Complexity = O(1) ... (Memory: 14.1mb - Beats 38.77%)
        """

        # If the input string is empty, return 0
        if len(s) == 0:
            return 0

        # Set the length of the longest substring to 1 and the starting index of the substring to 0
        longest_substring_length = 1
        start_idx = 0

        # Iterate through the string s
        for i in range(1, len(s)):
            # If the current character is already in the substring, update the starting index of the substring
            if s[i] in s[start_idx : i]:
                start_idx = s[start_idx:i].index(s[i]) + start_idx + 1

            # Update the length of the longest substring
            longest_substring_length = max(longest_substring_length, i - start_idx + 1)

        # Return the length of the longest substring
        return longest_substring_length
