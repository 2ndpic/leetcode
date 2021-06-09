# 给你一个正方形字符数组 board ，你从数组最右下方的字符 'S' 出发。 
# 
#  你的目标是到达数组最左上角的字符 'E' ，数组剩余的部分为数字字符 1, 2, ..., 9 或者障碍 'X'。在每一步移动中，你可以向上、向左或者左上
# 方移动，可以移动的前提是到达的格子没有障碍。 
# 
#  一条路径的 「得分」 定义为：路径上所有数字的和。 
# 
#  请你返回一个列表，包含两个整数：第一个整数是 「得分」 的最大值，第二个整数是得到最大得分的方案数，请把结果对 10^9 + 7 取余。 
# 
#  如果没有任何路径可以到达终点，请返回 [0, 0] 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：board = ["E23","2X2","12S"]
# 输出：[7,1]
#  
# 
#  示例 2： 
# 
#  
# 输入：board = ["E12","1X1","21S"]
# 输出：[4,2]
#  
# 
#  示例 3： 
# 
#  
# 输入：board = ["E11","XXX","11S"]
# 输出：[0,0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= board.length == board[i].length <= 100 
#  
#  Related Topics 动态规划 
#  👍 30 👎 0

from typing import List
import collections
import functools
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        """
        f[idx]表示从S到idx位置时的最大得分,idx = x * n + y,则 x = idx // n, y = idx % n
        f[idx] = max(f[(x + 1, y)], f[(x + 1, y + 1), f[(x, y + 1)]] + board[x][y])
        那么f[0]就是答案最大得分
        对于方案数，用g数组来记录,g[idx]表示从S到idx位置时最大得分的方案数。
        f[(x+1, y)], f[(x + 1, y + 1)], f[(x, y + 1)]的最大得分如果分别为2, 5, 5
        那么g[(x, y)] = g[(x + 1, y + 1)] + g[(x, y + 1)]
        """
        n = len(board)
        f = [-float('inf')] * (n * n)
        f[-1] = 0
        g = [0] * (n * n)
        g[-1] = 1
        for i in range(n * n - 2, -1, -1):
            x, y = i // n, i % n
            val = board[x][y]
            if val == "X":
                continue
            else:
                val = int(val) if val != "E" else 0
            for dx, dy in ((1, 0), (1, 1), (0, 1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    f[i] = max(f[i], f[nx * n + ny] + val)
            for dx, dy in ((1, 0), (1, 1), (0, 1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and f[i] == f[nx * n + ny] + val:
                    g[i] += g[nx * n + ny]
        if f[0] == float('-inf'):
            return [0, 0]
        return [f[0], g[0] % (10 ** 9 + 7)]


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        """
        官解优化版
        dp[i][0]表示S到达i位置的最大得分，dp[i][1]表示最大得分的方案数
        """
        def update(x, y, u, v):
            if u >= n or v >= n or dp[u * n + v][0] == -1:
                return
            i, (score, paths) = x * n + y, dp[u * n + v]
            if dp[i][0] == score: dp[i][1] = (dp[i][1] + paths) % (10 ** 9 + 7)
            elif dp[i][0] < score: dp[i] = [score, paths]

        n = len(board)
        dp = [[-1, 0] for _ in range(n * n)] # dp[i][0]表示
        dp[-1] = [0, 1]
        for i in range(n * n - 2, -1, -1):
            x, y = i // n , i % n
            if board[x][y] != "X":
                update(x, y, x + 1, y)
                update(x, y, x + 1, y + 1)
                update(x, y, x, y + 1)
                if dp[i][0] != -1:
                    dp[i][0] += (int(board[x][y]) if board[x][y] != "E" else 0)
        return dp[0] if dp[0][0] != -1 else [0, 0]

        
# leetcode submit region end(Prohibit modification and deletion)
board = ["E23","2X2","12S"]
board = ["E12","1X1","21S"]
# board = ["E11","XXX","11S"]
board = ["E11345","X452XX","3X43X4","422812","284522","13422S"]
print(Solution().pathsWithMaxScore(board))