class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = list(str(x))
        y.reverse()
        if y == list(str(x)):
            return True
        return False

    def isPalindromeImproved(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
