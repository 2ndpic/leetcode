# 给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。 
# 
#  两个相邻元素间的距离为 1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：mat = [[0,0,0],[0,1,0],[0,0,0]]
# 输出：[[0,0,0],[0,1,0],[0,0,0]]
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：mat = [[0,0,0],[0,1,0],[1,1,1]]
# 输出：[[0,0,0],[0,1,0],[1,2,1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == mat.length 
#  n == mat[i].length 
#  1 <= m, n <= 104 
#  1 <= m * n <= 104 
#  mat[i][j] is either 0 or 1. 
#  mat 中至少有一个 0 
#  
#  Related Topics 广度优先搜索 数组 动态规划 矩阵 
#  👍 464 👎 0
from typing import List
from collections import deque
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ans = [[-1] * n for _ in range(m)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    ans[i][j] = 0
        while q:
            x, y, d = q.popleft()
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and mat[nx][ny] == 1 and ans[nx][ny] == -1:
                    q.append((nx, ny, d + 1))
                    ans[nx][ny] = d + 1
        return ans

# leetcode submit region end(Prohibit modification and deletion)
mat = [[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0]]
print(Solution().updateMatrix(mat))