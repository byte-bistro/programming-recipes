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


from collections import defaultdict


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        """
        This function takes two lists of strings as input and returns a list
        of strings as output. It finds the common elements in both lists and
        returns the element(s) with the minimum index sum.

        Time Complexity = O(n) ... (Runtime: 151ms - Beats 83.14%)
        Space Complexity = O(n) ... (Memory: 14.5mb - Beats 27.75%)
        """

        # Create a dictionary to store the indexes of elements in list1
        element_index_dict = defaultdict(int)

        # Iterate over each element in list1 and add its index to the dictionary
        for idx, val in enumerate(list1):
            element_index_dict[val] = idx

        # Initialize variables to track minimum index sum and corresponding elements
        min_index_sum = float("inf")
        restaurant_name_list = []

        # Iterate over each element in list2
        for idx, name in enumerate(list2):
            # Check if the current element exists in the dictionary
            if name in element_index_dict:
                # Calculate the sum of the indexes of the current element in both lists
                indexSum = element_index_dict[name] + idx

                # If the sum is less than the current minimum, update the minimum and clear the restaurant name list
                if indexSum < min_index_sum:
                    min_index_sum = indexSum
                    restaurant_name_list = []
                    restaurant_name_list.append(name)

                # If the sum is equal to the current minimum, add the current element to the restaurant name list
                elif indexSum == min_index_sum:
                    restaurant_name_list.append(name)

        # Return the restaurant name list with the minimum index sum
        return restaurant_name_list
