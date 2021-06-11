# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回
#  -1。 
# 
#  你可以认为每种硬币的数量是无限的。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3 
# 解释：11 = 5 + 5 + 1 
# 
#  示例 2： 
# 
#  
# 输入：coins = [2], amount = 3
# 输出：-1 
# 
#  示例 3： 
# 
#  
# 输入：coins = [1], amount = 0
# 输出：0
#  
# 
#  示例 4： 
# 
#  
# 输入：coins = [1], amount = 1
# 输出：1
#  
# 
#  示例 5： 
# 
#  
# 输入：coins = [1], amount = 2
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= coins.length <= 12 
#  1 <= coins[i] <= 231 - 1 
#  0 <= amount <= 104 
#  
#  Related Topics 动态规划 
#  👍 1309 👎 0

from typing import List
import functools
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        f[i][j]表示用前i种硬币凑到j的最少个数，转化为完全背包问题.f[n][amount]为答案
        f[i][j] = min(f[i-1][j], f[i-1][j-coins[i-1]] + 1, f[i-1][j-2*coins[i-1]] + 2,...)
        f[i][j-conis[i]] = min(  f[i-1][j-coins[i-1]], f[i-1][j-2*coins[i-1]] + 1,...)
        so f[i][j] = min(f[i-1][j], f[i][j-coins[i-1]] + 1)
        """
        n = len(coins)
        f = [float('inf')] * (amount + 1)
        f[0] = 0
        for i in range(1, n + 1):
            for j in range(coins[i-1], amount + 1):
                f[j] = min(f[j], f[j - coins[i-1]] + 1)
        return f[-1] if f[-1] < float('inf') else -1
# leetcode submit region end(Prohibit modification and deletion)
coins = [1, 2, 5]; amount = 11
coins = [1]; amount = 0
print(Solution().coinChange(coins, amount))