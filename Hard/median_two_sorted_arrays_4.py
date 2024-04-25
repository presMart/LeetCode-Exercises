"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

> Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

> Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6

"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Most efficient - Time == O(m+n) Space == O(m+n)
        # Uses the Two Pointer method, allowing us to iterate over BOTH lists in one loop
        i = j = 0
        nums3 = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1

        if i <= len(nums1) - 1:
            nums3.extend(nums1[i:])
        elif j <= len(nums2) - 1:
            nums3.extend(nums2[j:])

        mid = (len(nums3) - 1) // 2
        return (nums3[mid] + nums3[mid + 1]) / 2 if (len(nums3) - 1) % 2 != 0 else float(nums3[mid])

    # The functions below represent my 1st attempt (and a tweak of it), which helped me pick apart the issues of
    # time and space complexity

    def findMedianSortedArraysFirstIdea(self, nums1: List[int], nums2: List[int]) -> float:
        # Less efficient - Time == O((m+n) log(m+n))  Space == O(m+n)
        nums3 = sorted(nums1 + nums2)
        len_nums = len(nums3) - 1
        mid = len_nums // 2
        return (nums3[mid] + nums3[mid + 1]) / 2 if len_nums % 2 != 0 else float(nums3[mid])

    def findMedianSortedArraysAltIdea(self, nums1: List[int], nums2: List[int]) -> float:
        # Time == O(n log n)  Space == O(n)
        nums1.extend(nums2)
        nums1.sort()
        mid = (len(nums1) - 1) // 2
        return (nums1[mid] + nums1[mid + 1]) / 2 if (len(nums1) - 1) % 2 != 0 else float(nums1[mid])



