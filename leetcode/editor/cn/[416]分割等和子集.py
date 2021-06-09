# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11] 。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3,5]
# 输出：false
# 解释：数组不能分割成两个元素和相等的子集。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 200 
#  1 <= nums[i] <= 100 
#  
#  Related Topics 动态规划 
#  👍 819 👎 0

from typing import List
import functools
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        01背包问题，给sum(nums)//2的背包，背包能装下的最大价值是否到sum(nums)//2
        """
        if sum(nums) & 1: return False
        n = sum(nums) >> 1
        f = [0] * (n + 1)
        for i in range(len(nums)):
            for j in range(n, nums[i] - 1, -1):
                f[j] = max(f[j], f[j - nums[i]] + nums[i])
        return f[n] == n
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        记忆化搜索
        """
        @functools.lru_cache(None)
        def dfs(i, j):
            if i < 0 < j: return False
            if j == 0: return True
            return dfs(i - 1, j) or (dfs(i - 1, j - nums[i]) if j - nums[i] >= 0 else False)
        if sum(nums) & 1: return False
        return dfs(len(nums) - 1, sum(nums) >> 1)
# leetcode submit region end(Prohibit modification and deletion)
nums = [1,5,11,5]
# nums = [1,2,3,5]
print(Solution().canPartition(nums))
