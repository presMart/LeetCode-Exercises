"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1) Open brackets must be closed by the same type of brackets.
2) Open brackets must be closed in the correct order.
3) Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(": ")", "[": "]", "{": "}"}

        for c in s:
            if c in pairs:
                stack.append(c)
            else:
                if not stack:
                    return False

                previous_opening = stack.pop()

                if pairs[previous_opening] != c:
                    return False

        return not stack
