# 给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。 
# 
#  一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。 
# 
#  返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# 输出：3
# 解释：有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# 输出：0
# 解释：所有 1 都在边界上或可以到达边界。
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 500 
#  grid[i][j] 的值为 0 或 1 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 146 👎 0
from typing import List
from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        for i in range(m):
            if grid[i][0]:
                q.append((i, 0))
                grid[i][0] = 0
            if grid[i][n - 1]:
                q.append((i, n - 1))
                grid[i][n - 1] = 0

        for j in range(n):
            if grid[0][j]:
                q.append((0, j))
                grid[0][j] = 0
            if grid[m - 1][j]:
                q.append((m - 1, j))
                grid[m - 1][j] = 0

        while q:
            x, y = q.popleft()
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny]:
                    grid[nx][ny] = 0
                    q.append((nx, ny))
        return sum(sum(row) for row in grid)

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0: return
            grid[x][y] = 0
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                dfs(nx, ny)
        m, n = len(grid), len(grid[0])
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        return sum((sum(row)) for row in grid)

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # TO-DO 并查集

# leetcode submit region end(Prohibit modification and deletion)
grid = [[0,0,0,1,1,1,0,1,1,1,1,1,0,0,0],
        [1,1,1,1,0,0,0,1,1,0,0,0,1,1,1],
        [1,1,1,0,0,1,0,1,1,1,0,0,0,1,1],
        [1,1,0,1,0,1,1,0,0,0,1,1,0,1,0],
        [1,1,1,1,0,0,0,1,1,1,0,0,0,1,1],
        [1,0,1,1,0,0,1,1,1,1,1,1,0,0,0],
        [0,1,0,0,1,1,1,1,0,0,1,1,1,0,0],
        [0,0,1,0,0,0,0,1,1,0,0,1,0,0,0],
        [1,0,1,0,0,1,0,0,0,0,0,0,1,0,1],
        [1,1,1,0,1,0,1,0,1,1,1,0,0,1,0]]
print(Solution().numEnclaves(grid))