# 你准备参加一场远足活动。给你一个二维 rows x columns 的地图 heights ，其中 heights[row][col] 表示格子 (row,
#  col) 的高度。一开始你在最左上角的格子 (0, 0) ，且你希望去最右下角的格子 (rows-1, columns-1) （注意下标从 0 开始编号）。你
# 每次可以往 上，下，左，右 四个方向之一移动，你想要找到耗费 体力 最小的一条路径。 
# 
#  一条路径耗费的 体力值 是路径上相邻格子之间 高度差绝对值 的 最大值 决定的。 
# 
#  请你返回从左上角走到右下角的最小 体力消耗值 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：heights = [[1,2,2],[3,8,2],[5,3,5]]
# 输出：2
# 解释：路径 [1,3,5,3,5] 连续格子的差值绝对值最大为 2 。
# 这条路径比路径 [1,2,2,2,5] 更优，因为另一条路径差值最大值为 3 。
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：heights = [[1,2,3],[3,8,4],[5,3,5]]
# 输出：1
# 解释：路径 [1,2,3,4,5] 的相邻格子差值绝对值最大为 1 ，比路径 [1,3,5,3,5] 更优。
#  
# 
#  示例 3： 
# 
#  
# 输入：heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# 输出：0
# 解释：上图所示路径不需要消耗任何体力。
#  
# 
#  
# 
#  提示： 
# 
#  
#  rows == heights.length 
#  columns == heights[i].length 
#  1 <= rows, columns <= 100 
#  1 <= heights[i][j] <= 106 
#  
#  Related Topics 深度优先搜索 并查集 图 二分查找 
#  👍 80 👎 0

from typing import List
import collections
# leetcode submit region begin(Prohibit modification and deletion)
def find(u, parents):
    if u != parents[u]:
        parents[u] = find(parents[u], parents)
    return parents[u]
def union(u, v, parents, ranks):
    pu, pv = find(u, parents), find(v, parents)
    if pu == pv: return False
    if ranks[pu] > ranks[pv]: parents[pv] = pu
    elif ranks[pv] > ranks[pu]: parents[pu] = pv
    else: parents[pv], ranks[pu] = pu, ranks[pu] + 1
    return True
def s1(heights: List[List[int]]) -> int:
    rows, cols, edges = len(heights), len(heights[0]), []
    parents, ranks = [i for i in range(rows*cols)], [0 for _ in range(rows*cols)]
    for i in range(rows):
        for j in range(cols):
            if i + 1 < rows:
                edges.append((i*cols+j,
                              i*cols+j+cols,
                              abs(heights[i][j]-heights[i+1][j])))
            if j + 1 < cols:
                edges.append((i*cols+j,
                              i*cols+j+1,
                              abs(heights[i][j]-heights[i][j+1])))
    edges.sort(key=lambda x :x[2])
    for u, v, d in edges:
        union(u, v, parents, ranks)
        if find(0, parents) == find(rows * cols - 1, parents):
            return d
    return 0

def bfs(heights, mid, m, n):
    q, visited = collections.deque([(0, 0)]), {(0,0)}
    while q:
        x, y = q.popleft()
        for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if (0 <= nx < m and 0 <= ny < n) and (nx, ny) not in visited and abs(
                    heights[x][y] - heights[nx][ny]) <= mid:
                visited.add((nx, ny))
                q.append((nx, ny))
    return (m-1, n-1) in visited

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        lo, hi, m, n = 0, 10**6, len(heights), len(heights[0])
        while lo < hi:
            mid = (lo + hi) // 2
            if not bfs(heights, mid, m, n): lo = mid + 1
            else: hi = mid
        return lo

# leetcode submit region end(Prohibit modification and deletion)
heights = [[3]]
print(Solution().minimumEffortPath(heights))