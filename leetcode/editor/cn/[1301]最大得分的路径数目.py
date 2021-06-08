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
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        @functools.lru_cache(None)
        def dfs1(x, y):
            if x == n - 1 and y == n - 1:
                return [0, True]
            p = int(board[x][y]) if board[x][y] != "E" else 0
            ans = 0
            flag = False
            for dx, dy in ((1, 1), (1, 0), (0, 1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != "X":
                    cur = dfs1(nx, ny)
                    if cur[1]:
                        flag = True
                        ans = max(ans, cur[0] + p)
            return [ans, flag]
        def dfs2(x, y):
            if x == n - 1 and y == n - 1:
                return 0
            p = int(board[x][y]) if board[x][y] != "E" else 0
            paths = 0
            for dx, dy in ((1, 1), (1, 0), (0, 1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != "X":
                    # if dfs2(nx, ny) == 0 and nx != n - 1 and ny != n - 1: continue
                    if dfs1(nx, ny)[0] + p == ans: paths += 1
            return paths
        n = len(board)
        ans, flag = dfs1(0, 0)
        if not flag: return [ans, 0]
        paths = dfs2(0, 0)
        return [ans, paths % (10 ** 9 % 7)]
        
# leetcode submit region end(Prohibit modification and deletion)
board = ["E23","2X2","12S"]
# board = ["E12","1X1","21S"]
# board = ["E11","XXX","11S"]
board = ["E11345","X452XX","3X43X4","422812","284522","13422S"]
print(Solution().pathsWithMaxScore(board))