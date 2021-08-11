# 在给定的网格中，每个单元格可以有以下三个值之一： 
# 
#  
#  值 0 代表空单元格； 
#  值 1 代表新鲜橘子； 
#  值 2 代表腐烂的橘子。 
#  
# 
#  每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。 
# 
#  返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：[[2,1,1],[1,1,0],[0,1,1]]
# 输出：4
#  
# 
#  示例 2： 
# 
#  输入：[[2,1,1],[0,1,1],[1,0,1]]
# 输出：-1
# 解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
#  
# 
#  示例 3： 
# 
#  输入：[[0,2]]
# 输出：0
# 解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= grid.length <= 10 
#  1 <= grid[0].length <= 10 
#  grid[i][j] 仅为 0、1 或 2 
#  
#  Related Topics 广度优先搜索 数组 矩阵 
#  👍 391 👎 0
from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q, m, n, cnt = deque(), len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    cnt += 1
        if cnt == 0: return 0
        ans = -1
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        cnt -= 1
                        q.append((nx, ny))
            ans += 1
        return ans if cnt == 0 else -1

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q, m, n, cnt, t = deque(), len(grid), len(grid[0]), 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, t))
                elif grid[i][j] == 1:
                    cnt += 1
        if cnt == 0: return 0
        while q:
            x, y, t = q.popleft()
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    q.append((nx, ny, t + 1))
                    cnt -= 1
        return -1 if cnt else t

# leetcode submit region end(Prohibit modification and deletion)
grid = [[2,1,1],[1,1,0],[0,1,1]]
grid = [[0,1]]
# grid = [[2,1,1],[0,1,1],[1,0,1]]
print(Solution().orangesRotting(grid))