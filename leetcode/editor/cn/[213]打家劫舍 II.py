# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的
# 房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。 
# 
#  给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,3,2]
# 输出：3
# 解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3,1]
# 输出：4
# 解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
#      偷窃到的最高金额 = 1 + 3 = 4 。 
# 
#  示例 3： 
# 
#  
# 输入：nums = [0]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 100 
#  0 <= nums[i] <= 1000 
#  
#  Related Topics 动态规划 
#  👍 594 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        动态规划
        dp[i]表示偷到第i家(并且偷第i家)，取得的最大金额
        dp[i] = max(dp[1], dp[2], ..., dp[i - 2]) + nums[i]
        偷最后一家的话就不能偷第一家,从第二家开始偷，偷第一家的话就不能偷最后一家
        """
        n = len(nums)
        if n == 1: return nums[0]
        dp = [0] * (n + 1)
        # 偷第一家
        for i in range(1, n):
            dp[i] = nums[i - 1]
            tmp = 0
            for j in range(1, i - 1):
                tmp = max(tmp, dp[j])
            dp[i] += tmp
        ans = max(dp)
        dp = [0] * (n + 1)
        # 偷最后一家
        for i in range(2, n + 1):
            dp[i] = nums[i - 1]
            tmp = 0
            for j in range(2, i - 1):
                tmp = max(tmp, dp[j])
            dp[i] += tmp
        ans = max(ans, max(dp))
        return ans


# leetcode submit region end(Prohibit modification and deletion)
nums = [94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61, 6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397, 52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72]

print(Solution().rob(nums))
