class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = list(magazine)
        for x in ransomNote:
            if x not in mag:
                return False
            mag.remove(x)
        return True


