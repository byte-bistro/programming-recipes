# Unique Morse Code Words
**Difficulty**: Easy | **Data Structures**: Array, Hash Table, String | **Link**: [leetcode.com/problems/unique-morse-code-words](https://leetcode.com/problems/unique-morse-code-words)

### **:page_facing_up: Description**:

International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

- 'a' maps to ".-",
- 'b' maps to "-...",
- 'c' maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:
<pre>
[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
</pre>
Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

- For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
Return the number of different transformations among all words we have.

### **:bulb: Example**:

<pre>
<strong>Example 1:</strong>
Input: words = ["gin","zen","gig","msg"]
Output: 2
Explanation: The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations: "--...-." and "--...--.".

<strong>Example 2:</strong>
Input: words = ["a"]
Output: 1
</pre>

### **:lock: Constraints**:

- 1 <= words.length <= 100
- 1 <= words[i].length <= 12
- words[i] consists of lowercase English letters.
