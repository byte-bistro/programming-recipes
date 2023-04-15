# Keyboard Row
**Difficulty**: Easy | **Data Structures**: Array, Hash Table, String | **Link**: [leetcode.com/problems/keyboard-row](https://leetcode.com/problems/keyboard-row)

### **:page_facing_up: Description**:

Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:
- the first row consists of the characters "qwertyuiop",
- the second row consists of the characters "asdfghjkl", and
- the third row consists of the characters "zxcvbnm".

<hr>

### **:bulb: Example**:

<table border="0">
 <tr>
    <td><b style="font-size:30px">Example 1</b></td>
    <td><b style="font-size:30px">Example 2</b></td>
    <td><b style="font-size:30px">Example 3</b></td>
 </tr>
 <tr>
    <td>
      Input: words = ["Hello","Alaska","Dad","Peace"]
      <br>Output: ["Alaska","Dad"]
    </td>
    <td>
      Input: words = ["omk"]
      <br>Output: []
    </td>
    <td>
      Input: words = ["adsdf","sfd"]
      <br>Output: ["adsdf","sfd"]
    </td>
 </tr>
</table>

<hr>

### **:lock: Constraints**:

- 1 <= words.length <= 20
- 1 <= words[i].length <= 100
- words[i] consists of English letters (both lowercase and uppercase). 
