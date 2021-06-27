# 给你一个大小为 m x n 的整数矩阵 grid ，其中 m 和 n 都是 偶数 ；另给你一个整数 k 。 
# 
#  矩阵由若干层组成，如下图所示，每种颜色代表一层： 
# 
#  
# 
#  矩阵的循环轮转是通过分别循环轮转矩阵中的每一层完成的。在对某一层进行一次循环旋转操作时，层中的每一个元素将会取代其 逆时针 方向的相邻元素。轮转示例如下：
#  
# 
#  返回执行 k 次循环轮转操作后的矩阵。 
# 
#  
# 
#  示例 1： 
# 
#  输入：grid = [[40,10],[30,20]], k = 1
# 输出：[[10,20],[40,30]]
# 解释：上图展示了矩阵在执行循环轮转操作时每一步的状态。 
# 
#  示例 2： 
#  
# 
#  输入：grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
# 输出：[[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
# 解释：上图展示了矩阵在执行循环轮转操作时每一步的状态。
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  2 <= m, n <= 50 
#  m 和 n 都是 偶数 
#  1 <= grid[i][j] <= 5000 
#  1 <= k <= 109 
#  
#  Related Topics 数组 
#  👍 5 👎 0

from typing import List
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def rotateLayer(i, k):
            length = 2 * (m + n - 4 * i) - 4
            k = k % length
            for _ in range(k):
                start = grid[i][i]
                for y in range(i, n - 1 - i):
                    grid[i][y] = grid[i][y + 1]
                for x in range(i, m - 1 - i):
                    grid[x][n - 1 - i] = grid[x + 1][n - 1 - i]
                for y in range(n - 1 - i, i, -1):
                    grid[m - 1 - i][y] = grid[m - 1 - i][y - 1]
                for x in range(m - 1 - i, i, -1):
                    grid[x][i] = grid[x - 1][i]
                grid[i + 1][i] = start

        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2
        for i in range(layers):
            rotateLayer(i, k)
        return grid
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2
        for layer in range(layers):
            rows, cols, val = [], [], []
            for i in range(layer, m - 1 - layer):  # left
                rows.append(i)
                cols.append(layer)
                val.append(grid[i][layer])
            for j in range(layer, n - 1 - layer):  # bottom
                rows.append(m - 1 - layer)
                cols.append(j)
                val.append(grid[m - 1 - layer][j])
            for i in range(m - 1 - layer, layer, -1):  # right
                rows.append(i)
                cols.append(n - 1 - layer)
                val.append(grid[i][n - 1 - layer])
            for j in range(n - 1 - layer, layer, -1):  # top
                rows.append(layer)
                cols.append(j)
                val.append(grid[layer][j])
            total = len(val)
            kk = k % total
            for i in range(total):
                idx = (total - kk + i) % total
                grid[rows[i]][cols[i]] = val[idx]
        return grid
# leetcode submit region end(Prohibit modification and deletion)
