# 给你两个 非递增 的整数数组 nums1 和 nums2 ，数组下标均 从 0 开始 计数。 
# 
#  下标对 (i, j) 中 0 <= i < nums1.length 且 0 <= j < nums2.length 。如果该下标对同时满足 i <= j
#  且 nums1[i] <= nums2[j] ，则称之为 有效 下标对，该下标对的 距离 为 j - i 。 
# 
#  返回所有 有效 下标对 (i, j) 中的 最大距离 。如果不存在有效下标对，返回 0 。 
# 
#  一个数组 arr ，如果每个 1 <= i < arr.length 均有 arr[i-1] >= arr[i] 成立，那么该数组是一个 非递增 数组。 
# 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
# 输出：2
# 解释：有效下标对是 (0,0), (2,2), (2,3), (2,4), (3,3), (3,4) 和 (4,4) 。
# 最大距离是 2 ，对应下标对 (2,4) 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums1 = [2,2,2], nums2 = [10,10,1]
# 输出：1
# 解释：有效下标对是 (0,0), (0,1) 和 (1,1) 。
# 最大距离是 1 ，对应下标对 (0,1) 。 
# 
#  示例 3： 
# 
#  
# 输入：nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]
# 输出：2
# 解释：有效下标对是 (2,2), (2,3), (2,4), (3,3) 和 (3,4) 。
# 最大距离是 2 ，对应下标对 (2,4) 。
#  
# 
#  示例 4： 
# 
#  
# 输入：nums1 = [5,4], nums2 = [3,2]
# 输出：0
# 解释：不存在有效下标对，所以返回 0 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums1.length <= 105 
#  1 <= nums2.length <= 105 
#  1 <= nums1[i], nums2[j] <= 105 
#  nums1 和 nums2 都是 非递增 数组 
#  
#  Related Topics 贪心算法 双指针 二分查找 
#  👍 10 👎 0

from typing import List
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        stack = [i for i in nums1[:len(nums2)]]
        ans = 0
        for i in range(len(nums2) - 1, -1 , -1):
            while stack and nums2[i] >= stack[-1]:
                stack.pop()
                ans = max(ans, i - len(stack))
        return ans
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        for i in range(len(nums1)):
            lo, hi = i, len(nums2)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums2[mid] < nums1[i]: hi = mid
                else: lo = mid + 1
            ans = max(ans, lo - i - 1)
        return ans
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        """
        双指针
        """
        l, r, ans = 0, 0, 0
        while r < len(nums2):
            while l < len(nums1) and nums1[l] > nums2[r]:
                l += 1
            if l < len(nums1):
                ans = max(ans, r - l)
            r += 1
        return ans
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        """
        双指针
        """
        l, r = 0, 0
        while l < len(nums1) and r < len(nums2):
            if nums1[l] > nums2[r]:
                l += 1
            r += 1
        return max(0, r - l - 1)

# leetcode submit region end(Prohibit modification and deletion)
# nums1 = [55,30,5,4,2];nums2 = [100,20,10,10,5]
nums1 = [2,2,2]; nums2 = [10,10,1]
nums1 = [30,29,19,5];nums2 = [25,25,25,25,25]
nums1 = [5,4];nums2 = [3,2]
# nums1 = [5,4,3];nums2 = [7, 6, 5, 4]
print(Solution().maxDistance(nums1, nums2))