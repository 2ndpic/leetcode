# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# 
#  ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。 
# 
#  请找出其中最小的元素。 
# 
#  注意数组中可能存在重复的元素。 
# 
#  示例 1： 
# 
#  输入: [1,3,5]
# 输出: 1 
# 
#  示例 2： 
# 
#  输入: [2,2,2,0,1]
# 输出: 0 
# 
#  说明： 
# 
#  
#  这道题是 寻找旋转排序数组中的最小值 的延伸题目。 
#  允许重复会影响算法的时间复杂度吗？会如何影响，为什么？ 
#  
#  Related Topics 数组 二分查找 
#  👍 226 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi)// 2
            if nums[mid] < nums[hi]:
                hi = mid
            elif nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[mid] == nums[hi]:
                hi -= 1
        return nums[lo]


# leetcode submit region end(Prohibit modification and deletion)
nums = [4,5,1,2,3,4]
print(Solution().findMin(nums))