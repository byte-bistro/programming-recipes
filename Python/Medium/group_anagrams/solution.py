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
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Given a list of strings, groups the anagrams together and returns
        them as a list of lists.

        Time Complexity = O(n*m*log m) ... (Runtime: 98ms - Beats 74.52%)
        Space Complexity = O(n*m) ... (Memory: 17.8mb - Beats 60.90%)
        """
        # Initialize an empty dictionary to store anagrams
        sorted_strs_dict = {}
        # Initialize an empty list to store the groups of anagrams
        anagrams = []

        # Loop through each string in the input list
        for i in strs:
            # Sort the characters in the string and join them together
            temp = "".join(sorted(i))

            # If already present, append original string to value
            if temp in sorted_strs_dict:
                sorted_strs_dict[temp].append(i)
            # Otherwise, create a new key-value pair
            else:
                sorted_strs_dict[temp] = [i]

        # Return the list of anagrams
        return sorted_strs_dict.values()
