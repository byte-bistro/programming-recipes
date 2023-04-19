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
    def romanToInt(self, s: str) -> int:
        """        
        This function takes a string containing a Roman numeral as input and 
        returns an integer value corresponding to the Roman numeral. It uses 
        a dictionary to map each Roman numeral to its integer value, and 
        iterates through the string to determine the appropriate operation 
        (addition or subtraction) for each numeral.
        
        Time Complexity = O(n) ... (Runtime: 44ms - Beats 83.10%)
        Space Complexity = O(1) ... (Memory: 13.8mb - Beats 60.72%)
        """
        
        # Define a dictionary that maps Roman numerals to their integer values
        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        # Initialize a variable called integer_output to 0
        integer_output = 0

        # Loop through the string s up until the second-to-last character
        for i in range(len(s)-1):
            if roman[s[i]] < roman[s[i+1]]:
                # Subtract the value of the current Roman numeral from the integer output
                integer_output = integer_output - roman[s[i]]
            else:
                # Add the value of the current Roman numeral to the integer output
                integer_output = integer_output + roman[s[i]]
        
        # Add the value of the last Roman numeral in the string to the integer output and return it
        return integer_output + roman[s[-1]]
