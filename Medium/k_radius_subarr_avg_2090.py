"""
You are given a 0-indexed array nums of n integers, and an integer k.

The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.

Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.

The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part.

"""


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        len_nums = len(nums)

        n1 = nums[k:len_nums-k]
        ln1 = len(n1)
        prefix = [n1[0]]
        x = []


        for i in n1:
