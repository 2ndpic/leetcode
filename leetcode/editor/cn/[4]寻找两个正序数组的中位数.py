# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。 
# 
#  进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？ 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
#  
# 
#  示例 2： 
# 
#  输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
#  
# 
#  示例 3： 
# 
#  输入：nums1 = [0,0], nums2 = [0,0]
# 输出：0.00000
#  
# 
#  示例 4： 
# 
#  输入：nums1 = [], nums2 = [1]
# 输出：1.00000
#  
# 
#  示例 5： 
# 
#  输入：nums1 = [2], nums2 = []
# 输出：2.00000
#  
# 
#  
# 
#  提示： 
# 
#  
#  nums1.length == m 
#  nums2.length == n 
#  0 <= m <= 1000 
#  0 <= n <= 1000 
#  1 <= m + n <= 2000 
#  -106 <= nums1[i], nums2[i] <= 106 
#  
#  Related Topics 数组 二分查找 分治算法 
#  👍 3705 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        lo, hi = -1, max(len(nums1), len(nums2))
        while lo < hi:
            c1 = (lo + hi) // 2
            c2 = (n + 1) // 2 - c1 - 2
            if c2 >= len(nums2) or (-1 < c2 < len(nums2) and c1 + 1 < len(nums1) and nums2[c2] > nums1[c1 + 1]):
                lo = c1 + 1
            else:
                hi = c1
        c1 = lo
        c2 = (n + 1) // 2 - c1 - 2

        if -1 < c1 < len(nums1) and -1 < c2 < len(nums2): l = max(nums1[c1], nums2[c2])
        elif -1 < c1 < len(nums1): l = nums1[c1]
        else: l =  nums2[c2]
        if n % 2: return l
        if c1 + 1 == len(nums1): r = nums2[c2 + 1]
        elif c2 + 1 == len(nums2): r = nums1[c1 + 1]
        else: r = min(nums1[c1+1], nums2[c2+1])
        return (l + r) / 2

# leetcode submit region end(Prohibit modification and deletion)
# nums1 = [2, 3, 5, 10]
# nums2 = [1, 4, 7, 9]
nums1 = []
nums2 = [2, 3]
print(Solution().findMedianSortedArrays(nums1, nums2))
print(sorted(nums1+nums2))
# print("-----------")
nums1 = [1, 3]
nums2 = [2]
print(Solution().findMedianSortedArrays(nums1, nums2))
print(sorted(nums1+nums2))
# print("-----------")
nums1 = [1, 2]
nums2 = [3, 4]
print(Solution().findMedianSortedArrays(nums1, nums2))
print(sorted(nums1+nums2))
# print("-----------")
nums1 = [0, 0]
nums2 = [0, 0]
print(Solution().findMedianSortedArrays(nums1, nums2))
print(sorted(nums1+nums2))
# print("-----------")
nums1 = []
nums2 = [2]
print(Solution().findMedianSortedArrays(nums1, nums2))
print(sorted(nums1+nums2))
# print("-----------")
nums1 = [1,2]
nums2 = [2,3,3]
print(Solution().findMedianSortedArrays(nums1, nums2))
print(sorted(nums1+nums2))
# print("-----------")