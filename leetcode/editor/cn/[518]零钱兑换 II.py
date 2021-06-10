# 给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 
# 
#  
# 
#  
#  
# 
#  示例 1: 
# 
#  输入: amount = 5, coins = [1, 2, 5]
# 输出: 4
# 解释: 有四种方式可以凑成总金额:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
#  
# 
#  示例 2: 
# 
#  输入: amount = 3, coins = [2]
# 输出: 0
# 解释: 只用面额2的硬币不能凑成总金额3。
#  
# 
#  示例 3: 
# 
#  输入: amount = 10, coins = [10] 
# 输出: 1
#  
# 
#  
# 
#  注意: 
# 
#  你可以假设： 
# 
#  
#  0 <= amount (总金额) <= 5000 
#  1 <= coin (硬币面额) <= 5000 
#  硬币种类不超过 500 种 
#  结果符合 32 位符号整数 
#  
#  👍 435 👎 0

from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        f[i][j]表示前i个coins凑到金额j的方案数
        f[i][j] = f[i-1][j] + f[i-1][j-coins[i-1]] + f[i-1][j-coins[i-1]*2] + ...
        """
        f = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        for i in range(len(coins) + 1):
            f[i][0] = 1
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                for k in range(j//coins[i-1] + 1):
                    f[i][j] += f[i-1][j-coins[i-1]*k]
        return f[len(coins)][amount]

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        f[i][j]表示前i个coins凑到金额j的方案数
        f[i][j] = f[i-1][j] + f[i-1][j-coins[i-1]] + f[i-1][j-coins[i-1]*2] + ...
        f[i][j-coins[i-1]] = f[i-1][j-coins[i-1]] + f[i-1][j-coins[i-1]*2] + ...
        """
        f = [1] + [0] * amount
        for i in range(1, len(coins) + 1):
            for j in range(coins[i-1], amount + 1):
                f[j] = f[j] + f[j - coins[i-1]]
        return f[-1]
# leetcode submit region end(Prohibit modification and deletion)
# amount = 5; coins = [1, 2, 5]
amount = 3; coins = [2]
amount = 10; coins = [10]
print(Solution().change(amount, coins))