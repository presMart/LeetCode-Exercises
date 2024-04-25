class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_iter = enumerate(nums)
        i = 1
        while i <= len(nums):
            x_i, x_val = next(n_iter)
            y_i = x_i + 1
            for z in range(y_i, len(nums)):
                if x_val + nums[z] == target:
                    return [x_i, z]
            i += 1
        return []
