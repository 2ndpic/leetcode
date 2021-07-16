# 统计一个数字在排序数组中出现的次数。 
# 
#  
# 
#  示例 1: 
# 
#  输入: nums = [5,7,7,8,8,10], target = 8
# 输出: 2 
# 
#  示例 2: 
# 
#  输入: nums = [5,7,7,8,8,10], target = 6
# 输出: 0 
# 
#  
# 
#  限制： 
# 
#  0 <= 数组长度 <= 50000 
# 
#  
# 
#  注意：本题与主站 34 题相同（仅返回值不同）：https://leetcode-cn.com/problems/find-first-and-last-
# position-of-element-in-sorted-array/ 
#  Related Topics 数组 二分查找 
#  👍 172 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target: lo = mid + 1
            else: hi = mid
        left, lo, hi = lo, 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target: hi = mid
            else: lo = mid + 1
        return lo - left
# leetcode submit region end(Prohibit modification and deletion)
