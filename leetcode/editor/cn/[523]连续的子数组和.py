# 给你一个整数数组 nums 和一个整数 k ，编写一个函数来判断该数组是否含有同时满足下述条件的连续子数组： 
# 
#  
#  子数组大小 至少为 2 ，且 
#  子数组元素总和为 k 的倍数。 
#  
# 
#  如果存在，返回 true ；否则，返回 false 。 
# 
#  如果存在一个整数 n ，令整数 x 符合 x = n * k ，则称 x 是 k 的一个倍数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [23,2,4,6,7], k = 6
# 输出：true
# 解释：[2,4] 是一个大小为 2 的子数组，并且和为 6 。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [23,2,6,4,7], k = 6
# 输出：true
# 解释：[23, 2, 6, 4, 7] 是大小为 5 的子数组，并且和为 42 。 
# 42 是 6 的倍数，因为 42 = 7 * 6 且 7 是一个整数。
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [23,2,6,4,7], k = 13
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 105 
#  0 <= nums[i] <= 109 
#  0 <= sum(nums[i]) <= 231 - 1 
#  1 <= k <= 231 - 1 
#  
#  Related Topics 数学 动态规划 
#  👍 258 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pre_sum = [0]
        seen = {}
        for i in nums:
            pre_sum.append(pre_sum[-1] + i)
        for i in range(1, len(pre_sum)):
            cur = pre_sum[i] % k
            if cur == 0 and i > 1: return True
            if cur in seen and i - seen[cur] > 1: return True
            if cur not in seen: seen[cur] = i
        return False
# leetcode submit region end(Prohibit modification and deletion)
