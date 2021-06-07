# 给你一个整数数组 nums 和一个整数 target 。 
# 
#  向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ： 
# 
#  
#  例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。 
#  
# 
#  返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,1,1,1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1], target = 1
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 20 
#  0 <= nums[i] <= 1000 
#  0 <= sum(nums[i]) <= 1000 
#  -1000 <= target <= 100 
#  
#  Related Topics 深度优先搜索 动态规划 
#  👍 726 👎 0

from typing import List
import functools
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        f[i][j]表示考虑前i个数字，值为j-1000的表达式数目
        f[i][j] = f[i-1][j - 1000 - nums[i - 1]] + f[i-1][j + nums[i - 1]]
        """
        f = [[0] * 4000 for _ in range(len(nums) + 1)]
        f[0][1000] = 1 # 考虑0个数字，值为0的表达式数目为1
        for i in range(1, len(nums) + 1):
            for j in range(2010):
                f[i][j] = f[i - 1][j - nums[i - 1]] + f[i - 1][j + nums[i - 1]]
        return f[len(nums)][target + 1000]

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @functools.lru_cache(None)
        def dfs(i, t):
            if i < 0:
                return t == 0
            return dfs(i - 1, t - nums[i]) + dfs(i - 1, t + nums[i])
        return dfs(len(nums) - 1, target)
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        target是由nums中负数和整数加起来的，令负值部分的绝对和为m，s = sum(nums)
        (s-m) + (-m) = target, 则 m = (s - target) / 2
        问题转换为01背包问题，对nums每个数考虑选不选，
        f[i][j]表示考虑前i个数，其绝对值和为j的方案数，初始化f[0][0] = 1
        f[i][j] = f[i-1][j] + f[i-1][j-nums[i-1]]
        """
        s = sum(nums)
        m = (s - target) // 2
        if m < 0 or 2 * m < s - target: return 0
        f = [[0] * (m + 1) for _ in range(2)]
        f[0][0] = 1
        for i in range(1, len(nums) + 1):
            for j in range(m + 1):
                f[i&1][j] = f[(i - 1)&1][j] + (f[(i - 1)&1][j - nums[i - 1]] if j - nums[i - 1] >= 0 else 0)
        return f[len(nums)&1][m]
# leetcode submit region end(Prohibit modification and deletion)
# nums = [1,0]
# target = 1
nums = [38,21,23,36,1,36,18,3,37,27,29,29,35,47,16,0,2,42,46,6]
target = 14
print(Solution().findTargetSumWays(nums, target))