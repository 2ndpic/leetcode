# 给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
# 输出: 4
# 解释: 下雨后，雨水将会被上图蓝色的方块中。总的接雨水量为1+2+1=4。
#  
# 
#  示例 2: 
# 
#  
# 
#  
# 输入: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
# 输出: 10
#  
# 
#  
# 
#  提示: 
# 
#  
#  m == heightMap.length 
#  n == heightMap[i].length 
#  1 <= m, n <= 200 
#  0 <= heightMap[i][j] <= 2 * 10⁴ 
#  
# 
#  
#  Related Topics 广度优先搜索 数组 矩阵 堆（优先队列） 👍 463 👎 0
from typing import List
import heapq
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        vis = [[False] * n for _ in range(m)]
        q = []
        for i in range(n):
            heapq.heappush(q, (0, i, heightMap[0][i]))
            heapq.heappush(q, (m - 1, i, heightMap[m - 1][i]))
            vis[0][i] = vis[m - 1][i] = True

        for i in range(1, m - 1):
            heapq.heappush(q, (i, 0, heightMap[i][0]))
            heapq.heappush(q, (i, n - 1, heightMap[i][n - 1]))
            vis[i][0] = vis[i][n - 1] = True

        ans = 0
        while q:
            x, y, h = heapq.heappop(q)
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not vis[nx][ny]:
                    ans += max(0, h - heightMap[nx][ny])
                    heapq.heappush(q, (nx, ny, max(heightMap[nx][ny], h)))
                    vis[nx][ny] = True
        return ans



# leetcode submit region end(Prohibit modification and deletion)
heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
heightMap = [[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]
print(Solution().trapRainWater(heightMap))