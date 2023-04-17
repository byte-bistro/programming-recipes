# Group Anagrams
**Difficulty**: Easy | **Data Structures**: Array, Hash Table, String | **Link**: [leetcode.com/problems/keyboard-row](https://leetcode.com/problems/keyboard-row)

### **:page_facing_up: Description**:

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### **:bulb: Example**:

<pre>
<strong>Example 1:</strong>
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

<strong>Example 2:</strong>
Input: strs = [""]
Output: [[""]]

<strong>Example 3:</strong>
Input: strs = ["a"]
Output: [["a"]]
</pre>

### **:lock: Constraints**:

- 1 <= strs.length <= 104
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.
