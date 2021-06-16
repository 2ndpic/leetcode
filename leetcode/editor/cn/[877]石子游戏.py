# 亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 piles[i] 。 
# 
#  游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。 
# 
#  亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。 这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。
#  
# 
#  假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回 true ，当李赢得比赛时返回 false 。 
# 
#  
# 
#  示例： 
# 
#  
# 输入：[5,3,4,5]
# 输出：true
# 解释：
# 亚历克斯先开始，只能拿前 5 颗或后 5 颗石子 。
# 假设他取了前 5 颗，这一行就变成了 [3,4,5] 。
# 如果李拿走前 3 颗，那么剩下的是 [4,5]，亚历克斯拿走后 5 颗赢得 10 分。
# 如果李拿走后 5 颗，那么剩下的是 [3,4]，亚历克斯拿走后 4 颗赢得 9 分。
# 这表明，取前 5 颗石子对亚历克斯来说是一个胜利的举动，所以我们返回 true 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= piles.length <= 500 
#  piles.length 是偶数。 
#  1 <= piles[i] <= 500 
#  sum(piles) 是奇数。 
#  
#  Related Topics 极小化极大 数学 动态规划 
#  👍 284 👎 0

from typing import List
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        """
        dp[i][j]表示考虑[i,...,j]这堆石头，当前玩家（不一定是alice）与另一个玩家的得分之差的最大值
        显然只遍历i <= j的范围，其中i == j，dp[i][j] = piles[i]
        dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
        可以看到永远只用了下一行的状态，所以可以优化到O(n)
        """
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        for i in range(n-2, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(piles[j] - dp[i][j-1], piles[i] - dp[i + 1][j])
        return dp[0][n-1] > 0

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        """
        dp[i][j]表示考虑[i,...,j]这堆石头，当前玩家（不一定是alice）与另一个玩家的得分之差的最大值
        显然只遍历i <= j的范围，其中i == j，dp[i][j] = piles[i]
        dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
        可以看到永远只用了下一行的状态，所以可以空间复杂度可以优化到O(n)
        """
        n = len(piles)
        dp = [0] * n
        for i in range(n):
            dp[i] = piles[i]
        for i in range(n-2, -1, -1):
            for j in range(i + 1, n):
                dp[j] = max(piles[j] - dp[j-1], piles[i] - dp[j])
        return dp[n-1] > 0
# leetcode submit region end(Prohibit modification and deletion)
piles = [5,3,4,5]
print(Solution().stoneGame(piles))