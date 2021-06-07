# 给定一个 m × n 的网格和一个球。球的起始坐标为 (i,j) ，你可以将球移到相邻的单元格内，或者往上、下、左、右四个方向上移动使球穿过网格边界。但是，
# 你最多可以移动 N 次。找出可以将球移出边界的路径数量。答案可能非常大，返回 结果 mod 109 + 7 的值。 
# 
#  
# 
#  示例 1： 
# 
#  输入: m = 2, n = 2, N = 2, i = 0, j = 0
# 输出: 6
# 解释:
# 
#  
# 
#  示例 2： 
# 
#  输入: m = 1, n = 3, N = 3, i = 0, j = 1
# 输出: 12
# 解释:
# 
#  
# 
#  
# 
#  说明: 
# 
#  
#  球一旦出界，就不能再被移动回网格内。 
#  网格的长度和高度在 [1,50] 的范围内。 
#  N 在 [0,50] 的范围内。 
#  Related Topics 深度优先搜索 动态规划 
#  👍 122 👎 0

import functools
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @functools.lru_cache(None)
        def dfs(i, j, cur):
            if cur > maxMove: return 0
            if i < 0 or i == m or j < 0 or j == n: return 1
            ans = 0
            for dx, dy in ((0, -1), (-1, 0), (0, 1), (1, 0)):
                ans += dfs(i + dx, j + dy, cur + 1)
            return ans
        return dfs(startRow, startColumn, 0) % (10 ** 9 + 7)
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """
        f(i, j) 表示在xy位置出发，可用步数不超过j时的路径数量。其中i = x * n + y,x = i // n, y = i % n
        f(g(x, y), j) = f(g(x-1, y), j - 1) + f(g(x, y + 1), j - 1) + f(g(x + 1, y), j - 1) + f(g(x, y - 1), j - 1)
        那么求解答案：f(g(startRow, startColumn), maxMove)
        初始化，对边缘格子进行初始化操作
        """
        def add(x, y):
            idx = x * n + y
            for j in range(1, maxMove + 1):
                f[idx][j] += 1
        mod = 10 ** 9 + 7
        f = [[0] * (maxMove + 1) for _ in range(m * n)]
        for i in range(m):
            for j in range(n):
                if i == 0: add(i, j)
                if j == 0: add(i, j)
                if i == m - 1: add(i, j)
                if j == n - 1: add(i, j)

        for j in range(1, maxMove + 1):
            for i in range(m * n):
                x, y = i // n, i % n
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        f[i][j] += f[nx * n + ny][j - 1]
                        f[i][j] %= mod
        return f[startRow * n + startColumn][maxMove]
# leetcode submit region end(Prohibit modification and deletion)
