# 在一个 N x N 的坐标方格 grid 中，每一个方格的值 grid[i][j] 表示在位置 (i,j) 的平台高度。 
# 
#  现在开始下雨了。当时间为 t 时，此时雨水导致水池中任意位置的水位为 t 。你可以从一个平台游向四周相邻的任意一个平台，但是前提是此时水位必须同时淹没这两
# 个平台。假定你可以瞬间移动无限距离，也就是默认在方格内部游动是不耗时的。当然，在你游泳的时候你必须待在坐标方格里面。 
# 
#  你从坐标方格的左上平台 (0，0) 出发。最少耗时多久你才能到达坐标方格的右下平台 (N-1, N-1)？ 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: [[0,2],[1,3]]
# 输出: 3
# 解释:
# 时间为0时，你位于坐标方格的位置为 (0, 0)。
# 此时你不能游向任意方向，因为四个相邻方向平台的高度都大于当前时间为 0 时的水位。
# 
# 等时间到达 3 时，你才可以游向平台 (1, 1). 因为此时的水位是 3，坐标方格中的平台没有比水位 3 更高的，所以你可以游向坐标方格中的任意位置
#  
# 
#  示例2: 
# 
#  
# 输入: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6
# ]]
# 输出: 16
# 解释:
#  0  1  2  3  4
# 24 23 22 21  5
# 12 13 14 15 16
# 11 17 18 19 20
# 10  9  8  7  6
# 
# 最终的路线用加粗进行了标记。
# 我们必须等到时间为 16，此时才能保证平台 (0, 0) 和 (4, 4) 是连通的
#  
# 
#  
# 
#  提示: 
# 
#  
#  2 <= N <= 50. 
#  grid[i][j] 是 [0, ..., N*N - 1] 的排列。 
#  
#  Related Topics 堆 深度优先搜索 并查集 二分查找 
#  👍 129 👎 0


from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque
def bfs(t, grid):
    q = deque([(0, 0)]) if grid[0][0] <= t else deque()
    visited = {(0, 0)} if grid[0][0] <= t else set()
    while q:
        x, y = q.popleft()
        for nx, ny in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
            if (0 <= nx < len(grid) and 0 <= ny < len(grid[0])) and (nx, ny) not in visited and t >= grid[nx][ny]:
                q.append((nx, ny))
                visited.add((nx, ny))

    return (len(grid) - 1, len(grid[0]) - 1) in visited
def s1(grid: List[List[int]]) -> int:
    lo, hi = 0, 2500
    while lo < hi:
        mid = (lo + hi) // 2
        if not bfs(mid, grid):
            lo = mid + 1
        else:
            hi = mid
    return lo
def find(u, parents):
    if u != parents[u]:
        parents[u] = find(parents[u], parents)
    return parents[u]
def union(u, v, parents, ranks):
    pu, pv = find(u, parents), find(v, parents)
    if pu == pv: return False
    if ranks[pu] > ranks[pv]:
        parents[pv] = pu
    elif ranks[pv] > ranks[pu]:
        parents[pu] = pv
    else:
        parents[pv] = pu
        ranks[pu] += 1
    return True
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        edges = []
        for i in range(n):
            for j in range(n):
                if i + 1 < n:
                    edges.append((i*n+j, i*n+j+n, max(grid[i][j], grid[i+1][j])))
                if j + 1 < n:
                    edges.append((i*n+j, i*n+j+1, max(grid[i][j],  grid[i][j+1])))
        edges.sort(key=lambda x: x[2])
        parents, ranks = [i for i in range(n*n)], [0 for _ in range(n*n)]
        for u, v, d in edges:
            union(u, v, parents, ranks)
            if find(0, parents) == find(n*n-1, parents):
                return d



# leetcode submit region end(Prohibit modification and deletion)
grid = [[0,2],[1,3]]
print(Solution().swimInWater(grid))