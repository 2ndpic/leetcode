# 升序排列的整数数组 nums 在预先未知的某个点上进行了旋转（例如， [0,1,2,4,5,6,7] 经旋转后可能变为 [4,5,6,7,0,1,2] ）。
#  
# 
#  请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1 
# 
#  示例 3： 
# 
#  
# 输入：nums = [1], target = 0
# 输出：-1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 5000 
#  -10^4 <= nums[i] <= 10^4 
#  nums 中的每个值都 独一无二 
#  nums 肯定会在某个点上旋转 
#  -10^4 <= target <= 10^4 
#  
#  Related Topics 数组 二分查找 
#  👍 1152 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
def bin_search(a, x, lo, hi):
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x: lo = mid + 1
        else: hi = mid
    return lo

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        t = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                t = i
                break
        res = bin_search(nums, target, 0, t)
        if res == 0 and res[0] != target: res = bin_search(nums, target, t, len(nums))
        if (res == t and res[t] != target) or res == len(nums):
            return -1
# leetcode submit region end(Prohibit modification and deletion)
