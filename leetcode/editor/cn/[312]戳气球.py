# 有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。 
# 
#  现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 这里的 i -
#  1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。 
# 
#  求所能获得硬币的最大数量。 
# 
#  
# 示例 1：
# 
#  
# 输入：nums = [3,1,5,8]
# 输出：167
# 解释：
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,5]
# 输出：10
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == nums.length 
#  1 <= n <= 500 
#  0 <= nums[i] <= 100 
#  
#  Related Topics 数组 动态规划 
#  👍 762 👎 0
from typing import List
from functools import lru_cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        因为每次戳掉一个气球使得不相邻气球变得相邻使得后续操作难以处理。倒过来看这些操作，全过程就变成每次添加一个气球。
        为了方便处理，对nums开始和末尾添加1。定义方法solve,令solve(i,j)表示将开区间(i,j)全部填满气球最大得分。那么这个区间开端的气球就是val[i], val[j]
        - 当i >= j - 1时，开区间没有气球，即没有得分，solve(i, j) = 0
        - 当i < j - 1时，枚举开区间所有位置mid，令其为该区间第一个添加的气球，该操作得到的硬币数为val[i]*val[mid]*val[j],同时递归solve(i, mid)和solve(mid, j)
        """
        @lru_cache(None)
        def dfs(i, j):
            if i >= j - 1: return 0
            ans = 0
            for mid in range(i + 1, j - 1):
                cur = val[i] * val[mid] * val[j]
                ans = max(ans, cur + dfs(i, mid) + dfs(mid, j))
            return ans

        val = [1] + nums + [1]
        return dfs(0, len(val) - 1)

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        可以把记忆化搜索改造成自底向上的动态规划
        dp[i][j]表示填满开区间能得到的最多硬币数，边界条件时i>=j-1时，dp[i][j]=0
        当i < j时，dp[i][j] = max(dp[i][mid] + dp[mid][j] + val[i] * val[mid] * val[j]) (i + 1 <= mid <= j - 1)
        画个图注意遍历顺序
        """
        val = [1] + nums + [1]
        n = len(val)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                for mid in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][mid] + val[i] * val[mid] * val[j] + dp[mid][j])
        return dp[0][n-1]
# leetcode submit region end(Prohibit modification and deletion)
nums = [i for i in range(1, 101)]
# nums = [1,5]
print(Solution().maxCoins(nums))