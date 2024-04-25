class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x: x**2)

        return [x ** 2 for x in nums]
