# 给你一个整数数组 cost  target 。请你返回满足如下规则可以得到的 最大 整数：
# 
#  
#  给当前结果添加一个数位（i + 1）的成本为 cost[i] （cost 数组下标从 0 开始）。 
#  总成本必须恰好等于 target 。 
#  添加的数位中没有数字 0 。 
#  
# 
#  由于答案可能会很大，请你以字符串形式返回。 
# 
#  如果按照上述要求无法得到任何整数，请你返回 "0" 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：cost = [4,3,2,5,6,7,2,5,5], target = 9
# 输出："7772"
# 解释：添加数位 '7' 的成本为 2 ，添加数位 '2' 的成本为 3 。所以 "7772" 的代价为 2*3+ 3*1 = 9 。 "977" 也是满足要
# 求的数字，但 "7772" 是较大的数字。
#  数字     成本
#   1  ->   4
#   2  ->   3
#   3  ->   2
#   4  ->   5
#   5  ->   6
#   6  ->   7
#   7  ->   2
#   8  ->   5
#   9  ->   5
#  
# 
#  示例 2： 
# 
#  
# 输入：cost = [7,6,5,5,5,6,8,7,8], target = 12
# 输出："85"
# 解释：添加数位 '8' 的成本是 7 ，添加数位 '5' 的成本是 5 。"85" 的成本为 7 + 5 = 12 。
#  
# 
#  示例 3： 
# 
#  
# 输入：cost = [2,4,6,2,4,6,4,4,4], target = 5
# 输出："0"
# 解释：总成本是 target 的条件下，无法生成任何整数。
#  
# 
#  示例 4： 
# 
#  
# 输入：cost = [6,10,15,40,40,40,40,40,40], target = 47
# 输出："32211"
#  
# 
#  
# 
#  提示： 
# 
#  
#  cost.length == 9 
#  1 <= cost[i] <= 5000 
#  1 <= target <= 5000 
#  
#  Related Topics 字符串 动态规划 
#  👍 85 👎 0

from typing import List
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        """
        完全背包问题
        f[i][j]表示考虑[i,..,9]成本为恰好j的最大整数
        f[i][j] = max(f[i-1][j], f[i-1][j-cost[i-1]] + "i", f[i-1][j-2*cost[i-1]] + "i" * 2, ..., f[i-1][j-k*cost[i-1]] + "i" * k)
        f[i][j-cost[i-1]] =  max(f[i-1][j-cost[i-1]],       f[i-1][j-2*cost[i-1]] + "i", ...,     f[i-1][j-k*cost[i-1]] + "i" * (k-1))
        f[i][j] = max(f[i-1][j], f[i][j-cost[i-1]] + "i")
        """
        f = [""] * (target + 1)
        for i in range(9, 0, -1):
            for j in range(target + 1):
                if (j - cost[i - 1] > 0 and f[j - cost[i - 1]]) or j - cost[i - 1] == 0:
                    tmp = f[j - cost[i - 1]] + str(i)
                    if len(f[j]) < len(tmp) or (len(f[j]) == len(tmp) and tmp > f[j]):
                        f[j] = tmp
        return f[target] if f[target] else "0"
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        f = [float('-inf')] * (target + 1)
        f[0] = 0
        for i in range(9, 0, -1):
            for j in range(target + 1):
                if j >= cost[i-1]:
                    f[j] = max(f[j], f[j - cost[i - 1]] * 10 + i)
        return str(f[target]) if f[target] != float('-inf') else "0"

# leetcode submit region end(Prohibit modification and deletion)
cost = [4,3,2,5,6,7,2,5,5];target = 9
# cost = [7,6,5,5,5,6,8,7,8]; target = 12
print(Solution().largestNumber(cost, target))