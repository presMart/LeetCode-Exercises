"""
Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).



> Example 1:
Input: s = "abacbc"
Output: true
Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.

> Example 2:
Input: s = "aaabb"
Output: false
Explanation: The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.


> Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""

from collections import defaultdict

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count_dict = defaultdict(int)

        for c in s:
            count_dict[c] += 1

        return min(count_dict.values()) == max(count_dict.values())

    # def areOccurrencesEqualDefault(self, s: str) -> bool:
    #     count_dict = defaultdict(int)
    #
    #     for c in s:
    #         count_dict[c] += 1
    #
    #     frequencies = count_dict.values()
    #     return len(set(frequencies)) == 1



# A oneline example:
# from collections import Counter
#
# class Solution:
#     def areOccurrencesEqual(self, s: str) -> bool:
#         return len(set(Counter(s).values())) == 1

