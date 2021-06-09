# 集团里有 n 名员工，他们可以完成各种各样的工作创造利润。 
# 
#  第 i 种工作会产生 profit[i] 的利润，它要求 group[i] 名成员共同参与。如果成员参与了其中一项工作，就不能参与另一项工作。 
# 
#  工作的任何至少产生 minProfit 利润的子集称为 盈利计划 。并且工作的成员总数最多为 n 。 
# 
#  有多少种计划可以选择？因为答案很大，所以 返回结果模 10^9 + 7 的值。 
# 
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 5, minProfit = 3, group = [2,2], profit = [2,3]
# 输出：2
# 解释：至少产生 3 的利润，该集团可以完成工作 0 和工作 1 ，或仅完成工作 1 。
# 总的来说，有两种计划。 
# 
#  示例 2： 
# 
#  
# 输入：n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
# 输出：7
# 解释：至少产生 5 的利润，只要完成其中一种工作就行，所以该集团可以完成任何工作。
# 有 7 种可能的计划：(0)，(1)，(2)，(0,1)，(0,2)，(1,2)，以及 (0,1,2) 。 
#  
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 100 
#  0 <= minProfit <= 100 
#  1 <= group.length <= 100 
#  1 <= group[i] <= 100 
#  profit.length == group.length 
#  0 <= profit[i] <= 100 
#  
#  Related Topics 动态规划 
#  👍 148 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        """
        f[i][j][k]为考虑前i个工作最低利润为j员工为k的情况下的计划数, 最终答案f[len(group)][minProfit][n]
        两种选择做第i个工作，或者不做第i个工作
        不做：f[i][j][k] = f[i-1][j][k]
        做：f[i][j][k] = f[i-1][j-profit[i-1]][k-group[i-1]]
        f[i][j][k] = 不做 + 做
        """
        f = [[[0] * (n + 1) for _ in range(minProfit + 1)] for _ in range(len(group) + 1)]
        for k in range(n + 1):
            f[0][0][k] = 1
        for i in range(1, len(group) + 1):
            for j in range(minProfit + 1):
                for k in range(1, n + 1):
                    f[i][j][k] = f[i-1][j][k]
                    if k - group[i - 1] >= 0:
                        f[i][j][k] += f[i-1][max(0, j-profit[i-1])][k-group[i-1]]
                    f[i][j][k] %= (10 ** 9 + 7)
        return f[len(group)][minProfit][n]
# leetcode submit region end(Prohibit modification and deletion)
n = 5; minProfit = 3; group = [2,2]; profit = [2,3]
# n = 10; minProfit = 5; group = [2,3,5]; profit = [6,7,8]
print(Solution().profitableSchemes(n, minProfit, group, profit))