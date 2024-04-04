class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_list = []
        for i in nums:
            sum_list.extend([i + sum_list[-1] if sum_list else nums[0]])
        return sum_list
