# 给你一个下标从 1 开始的二进制矩阵，其中 0 表示陆地，1 表示水域。同时给你 row 和 col 分别表示矩阵中行和列的数目。 
# 
#  一开始在第 0 天，整个 矩阵都是 陆地 。但每一天都会有一块新陆地被 水 淹没变成水域。给你一个下标从 1 开始的二维数组 cells ，其中 cell
# s[i] = [ri, ci] 表示在第 i 天，第 ri 行 ci 列（下标都是从 1 开始）的陆地会变成 水域 （也就是 0 变成 1 ）。 
# 
#  你想知道从矩阵最 上面 一行走到最 下面 一行，且只经过陆地格子的 最后一天 是哪一天。你可以从最上面一行的 任意 格子出发，到达最下面一行的 任意 格子
# 。你只能沿着 四个 基本方向移动（也就是上下左右）。 
# 
#  请返回只经过陆地格子能从最 上面 一行走到最 下面 一行的 最后一天 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
# 输出：2
# 解释：上图描述了矩阵从第 0 天开始是如何变化的。
# 可以从最上面一行到最下面一行的最后一天是第 2 天。
#  
# 
#  示例 2： 
# 
#  输入：row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
# 输出：1
# 解释：上图描述了矩阵从第 0 天开始是如何变化的。
# 可以从最上面一行到最下面一行的最后一天是第 1 天。
#  
# 
#  示例 3： 
# 
#  输入：row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2]
# ,[3,1]]
# 输出：3
# 解释：上图描述了矩阵从第 0 天开始是如何变化的。
# 可以从最上面一行到最下面一行的最后一天是第 3 天。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= row, col <= 2 * 104 
#  4 <= row * col <= 2 * 104 
#  cells.length == row * col 
#  1 <= ri <= row 
#  1 <= ci <= col 
#  cells 中的所有格子坐标都是 唯一 的。 
#  
#  👍 11 👎 0
from typing import List
from collections import deque
class Solution:
    def latestDayToCross(self, m: int, n: int, cells: List[List[int]]) -> int:
        def check(days):
            grid = [[0] * n for _ in range(m)]
            seen = set()
            for i in range(days):
                x, y = cells[i]
                grid[x - 1][y - 1] = 1
            q = deque()
            for j in range(n):
                if grid[0][j] == 0:
                    q.append((0, j))
                    seen.add((0, j))
            while q:
                x, y = q.popleft()
                for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in seen:
                        if nx == m - 1: return True
                        q.append((nx, ny))
                        seen.add((nx, ny))
            return False
        lo, hi = 1, m * n
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid): lo = mid + 1
            else: hi = mid
        return lo if check(lo) else lo - 1

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv: return False
            if ranks[pu] > ranks[pv]:
                parents[pv] = pu
            elif ranks[pv] > ranks[pu]:
                parents[pu] = pv
            else:
                parents[pv] = pu
                ranks[pu] += 1
            return True
        def find(u):
            if parents[u] == u:
                return u
            parents[u] = find(parents[u])
            return parents[u]

        parents = [i for i in range(row * col + 2)]
        ranks = [0] * (row * col + 2)
        grid = [[1] * col for _ in range(row)]
        start, end = row * col, row * col + 1
        for i in range(len(cells) - 1, -1, -1):
            x, y = cells[i][0] - 1, cells[i][1] - 1
            grid[x][y] = 0
            if x == 0: union(x * col + y, start)
            if x == row - 1: union(x * col + y, end)
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == 0:
                    union(x * col + y, nx * col + ny)
            if find(start) == find(end):
                return i
# leetcode submit region end(Prohibit modification and deletion)
row = 2
col = 2
cells = [[1,1],[2,1],[1,2],[2,2]]
row = 2; col = 2; cells = [[1,1],[1,2],[2,1],[2,2]]
row = 3; col = 3; cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
print(Solution().latestDayToCross(row, col, cells))