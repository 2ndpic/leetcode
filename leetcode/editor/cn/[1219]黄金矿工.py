# 你要开发一座金矿，地质勘测学家已经探明了这座金矿中的资源分布，并用大小为 m * n 的网格 grid 进行了标注。每个单元格中的整数就表示这一单元格中的黄
# 金数量；如果该单元格是空的，那么就是 0。 
# 
#  为了使收益最大化，矿工需要按以下规则来开采黄金： 
# 
#  
#  每当矿工进入一个单元，就会收集该单元格中的所有黄金。 
#  矿工每次可以从当前位置向上下左右四个方向走。 
#  每个单元格只能被开采（进入）一次。 
#  不得开采（进入）黄金数目为 0 的单元格。 
#  矿工可以从网格中 任意一个 有黄金的单元格出发或者是停止。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：grid = [[0,6,0],[5,8,7],[0,9,0]]
# 输出：24
# 解释：
# [[0,6,0],
#  [5,8,7],
#  [0,9,0]]
# 一种收集最多黄金的路线是：9 -> 8 -> 7。
#  
# 
#  示例 2： 
# 
#  输入：grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
# 输出：28
# 解释：
# [[1,0,7],
#  [2,0,6],
#  [3,4,5],
#  [0,3,0],
#  [9,0,20]]
# 一种收集最多黄金的路线是：1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= grid.length, grid[i].length <= 15 
#  0 <= grid[i][j] <= 100 
#  最多 25 个单元格中有黄金。 
#  
#  Related Topics 回溯算法 
#  👍 73 👎 0


from typing import List
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def backtracking(x, y):
            if not (0 <= x < m and 0 <= y < n and grid[x][y]):
                return 0
            tmp = grid[x][y]
            grid[x][y] = 0
            nxt_sum = 0
            for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                nxt_sum = max(nxt_sum, backtracking(x + dx, y + dy))
            grid[x][y] = tmp
            return tmp + nxt_sum

        m, n, ans = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, backtracking(i, j))
        return ans
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def can_be_start(x, y):
            if grid[x][y]:
                nums = 0
                for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny]:
                        nums += 1
                if nums <= 2:
                    return True
            return False

        def backtracking(x, y, cur):
            res = cur
            for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny]:
                    t = grid[nx][ny]
                    grid[nx][ny] = 0
                    res = max(res, backtracking(nx, ny, cur + t))
                    grid[nx][ny] = t
            return res

        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if can_be_start(i, j):
                    tmp = grid[i][j]
                    grid[i][j] = 0
                    ans = max(ans, backtracking(i, j, tmp))
                    grid[i][j] = tmp
        return ans


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def backtracking(x, y, gold):
            nonlocal ans
            ans = max(ans, gold)
            tmp, grid[x][y] = grid[x][y], 0
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny]:
                    backtracking(nx, ny, gold + grid[nx][ny])
            grid[x][y] = tmp

        m, n, ans = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    backtracking(i, j, grid[i][j])
        return ans
# leetcode submit region end(Prohibit modification and deletion)
grid = [[0,6,0],[5,8,7],[0,9,0]]
grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
print(Solution().getMaximumGold(grid))