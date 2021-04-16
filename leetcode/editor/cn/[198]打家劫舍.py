# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上
# 被小偷闯入，系统会自动报警。 
# 
#  给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[1,2,3,1]
# 输出：4
# 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
#      偷窃到的最高金额 = 1 + 3 = 4 。 
# 
#  示例 2： 
# 
#  输入：[2,7,9,3,1]
# 输出：12
# 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
#      偷窃到的最高金额 = 2 + 9 + 1 = 12 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 100 
#  0 <= nums[i] <= 400 
#  
#  Related Topics 动态规划 
#  👍 1405 👎 0
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        动态规划
        dp[i]表示前i个房子且偷nums[i-1]房子的最大金额
        dp[i] = nums[i + 1] + max(dp[1], dp[2], .., dp[i - 2])
        """
        dp = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            dp[i] = nums[i - 1] + (max(dp[:i - 1]) if i - 1 > 0 else 0)
        return max(dp)
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        动态规划
        f[i][j]表示考虑前i个房子，当前第个i房间现在状态为j的最大价值
        f[i][0]表示不选第i个房间的最大价值，f[i][0] = max(f[i - 1][0], f[i - 1][1])
        f[i][1]表示选第i个房间的最大价值,f[i][1] = f[i - 1][0] + nums[i - 1]
        只与前一个状态相关，用滚动数组优化空间
        """
        f = [[0, 0], [0, 0]]
        for i in range(1, len(nums) + 1):
            f[i%2][0] = max(f[(i - 1)%2])
            f[i%2][1] = f[(i - 1)%2][0] + nums[i - 1]
        return max(f[len(nums)%2])
# leetcode submit region end(Prohibit modification and deletion)
nums = [1,2,3,1]
# nums = [2,7,9,3,1]
print(Solution().rob(nums))