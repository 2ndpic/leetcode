# 给你一个大小为 m x n 的整数矩阵 isWater ，它代表了一个由 陆地 和 水域 单元格组成的地图。 
# 
#  
#  如果 isWater[i][j] == 0 ，格子 (i, j) 是一个 陆地 格子。 
#  如果 isWater[i][j] == 1 ，格子 (i, j) 是一个 水域 格子。 
#  
# 
#  你需要按照如下规则给每个单元格安排高度： 
# 
#  
#  每个格子的高度都必须是非负的。 
#  如果一个格子是是 水域 ，那么它的高度必须为 0 。 
#  任意相邻的格子高度差 至多 为 1 。当两个格子在正东、南、西、北方向上相互紧挨着，就称它们为相邻的格子。（也就是说它们有一条公共边） 
#  
# 
#  找到一种安排高度的方案，使得矩阵中的最高高度值 最大 。 
# 
#  请你返回一个大小为 m x n 的整数矩阵 height ，其中 height[i][j] 是格子 (i, j) 的高度。如果有多种解法，请返回 任意一个
#  。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：isWater = [[0,1],[0,0]]
# 输出：[[1,0],[2,1]]
# 解释：上图展示了给各个格子安排的高度。
# 蓝色格子是水域格，绿色格子是陆地格。
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：isWater = [[0,0,1],[1,0,0],[0,0,0]]
# 输出：[[1,1,0],[0,1,1],[1,2,2]]
# 解释：所有安排方案中，最高可行高度为 2 。
# 任意安排方案中，只要最高高度为 2 且符合上述规则的，都为可行方案。
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == isWater.length 
#  n == isWater[i].length 
#  1 <= m, n <= 1000 
#  isWater[i][j] 要么是 0 ，要么是 1 。 
#  至少有 1 个水域格子。 
#  
#  Related Topics 广度优先搜索 数组 矩阵 👍 70 👎 0
from typing import List
from collections import deque
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        ans = [[water - 1 for water in row] for row in isWater]
        q = deque([(i, j) for i, row in enumerate(isWater) for j, water in enumerate(row) if water])
        while q:
            x, y = q.popleft()
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= nx < m and 0 <= ny < n and ans[nx][ny] == -1:
                    ans[nx][ny] = ans[x][y] + 1
                    q.append((nx, ny))
        return ans


# leetcode submit region end(Prohibit modification and deletion)
isWater = [[0,1],[0,0]]
isWater = [[0,0,1],[1,0,0],[0,0,0]]
isWater = [[0,0,0,0,0,0,1,0],[0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0],[0,0,1,0,0,0,0,0]]
print(Solution().highestPeak(isWater))