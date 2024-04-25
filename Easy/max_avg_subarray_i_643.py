"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Constraints:
    n == nums.length
    1 <= k <= n <= 105
    -104 <= nums[i] <= 104
"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = 0.0
        for i in range(k):
            curr += nums[i]

        ans = curr
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            ans = max(ans, curr)

        return ans/k

