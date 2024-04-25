"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort(key=lambda y: y if y != val else 1000)
        val_count = nums.count(val)
        num_len = len(nums)
        if num_len == val_count:
            return 0
        elif val_count == 0:
            return num_len
        elif val_count == 1:
            nums.pop(num_len - 1)
            return num_len - val_count
        for x in range(num_len - val_count, num_len):
            nums[x] = 101
        return num_len - val_count

