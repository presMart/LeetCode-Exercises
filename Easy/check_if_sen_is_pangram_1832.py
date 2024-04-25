"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.



Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false


Constraints:

1 <= sentence.length <= 1000
sentence consists of lowercase English letters.
"""


class Solution:
    # Both approaches have time and space complexity of O(n), but the top one is a bit more readable
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26

    def checkIfPangramOriginal(self, sentence: str) -> bool:
        s = set(sentence)
        abc = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
        return abc.issubset(s)

