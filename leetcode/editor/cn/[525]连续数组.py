# 给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [0,1]
# 输出: 2
# 说明: [0, 1] 是具有相同数量0和1的最长连续子数组。 
# 
#  示例 2: 
# 
#  
# 输入: nums = [0,1,0]
# 输出: 2
# 说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 105 
#  nums[i] 不是 0 就是 1 
#  
#  Related Topics 哈希表 
#  👍 299 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pre_sum, seen, ans = 0, {0:0}, 0
        for i in range(len(nums)):
            pre_sum += (nums[i] if nums[i] else -1)
            ans = max(ans, i + 1 - seen.setdefault(pre_sum, i + 1))
        return ans
# leetcode submit region end(Prohibit modification and deletion)
nums = [0, 1, 0, 0, 1, 1]
print(Solution().findMaxLength(nums))
