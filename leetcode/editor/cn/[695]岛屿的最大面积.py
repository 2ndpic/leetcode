# 给定一个包含了一些 0 和 1 的非空二维数组 grid 。 
# 
#  一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被 
# 0（代表水）包围着。 
# 
#  找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。) 
# 
#  
# 
#  示例 1: 
# 
#  [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
#  
# 
#  对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。 
# 
#  示例 2: 
# 
#  [[0,0,0,0,0,0,0,0]] 
# 
#  对于上面这个给定的矩阵, 返回 0。 
# 
#  
# 
#  注意: 给定的矩阵grid 的长度和宽度都不超过 50。 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 
#  👍 527 👎 0

from typing import List
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        BFS
        """
        ans, m, n = 0, len(grid), len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    grid[i][j] = 0
                    q = deque([(i, j)])
                    tmp = 0
                    while q:
                        x, y = q.popleft()
                        tmp += 1
                        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny]:
                                grid[nx][ny] = 0
                                q.append((nx, ny))
                    ans = max(ans, tmp)
        return ans
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        dfs
        """
        def dfs(x, y):
            if not (0 <= x < m and 0 <= y < n and grid[x][y]):
                return 0
            grid[x][y] = 0
            ret = 1
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx, ny = x + dx, y + dy
                ret += dfs(nx, ny)
            return ret

        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ans = max(ans, dfs(i, j))
        return ans
# leetcode submit region end(Prohibit modification and deletion)
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
print(Solution().maxAreaOfIsland(grid))