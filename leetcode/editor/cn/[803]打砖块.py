# 有一个 m x n 的二元网格，其中 1 表示砖块，0 表示空白。砖块 稳定（不会掉落）的前提是： 
# 
#  
#  一块砖直接连接到网格的顶部，或者 
#  至少有一块相邻（4 个方向之一）砖块 稳定 不会掉落时 
#  
# 
#  给你一个数组 hits ，这是需要依次消除砖块的位置。每当消除 hits[i] = (rowi, coli) 位置上的砖块时，对应位置的砖块（若存在）会消
# 失，然后其他的砖块可能因为这一消除操作而掉落。一旦砖块掉落，它会立即从网格中消失（即，它不会落在其他稳定的砖块上）。 
# 
#  返回一个数组 result ，其中 result[i] 表示第 i 次消除操作对应掉落的砖块数目。 
# 
#  注意，消除可能指向是没有砖块的空白位置，如果发生这种情况，则没有砖块掉落。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
# 输出：[2]
# 解释：
# 网格开始为：
# [[1,0,0,0]，
#  [1,1,1,0]]
# 消除 (1,0) 处加粗的砖块，得到网格：
# [[1,0,0,0]
#  [0,1,1,0]]
# 两个加粗的砖不再稳定，因为它们不再与顶部相连，也不再与另一个稳定的砖相邻，因此它们将掉落。得到网格：
# [[1,0,0,0],
#  [0,0,0,0]]
# 因此，结果为 [2] 。
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]
# 输出：[0,0]
# 解释：
# 网格开始为：
# [[1,0,0,0],
#  [1,1,0,0]]
# 消除 (1,1) 处加粗的砖块，得到网格：
# [[1,0,0,0],
#  [1,0,0,0]]
# 剩下的砖都很稳定，所以不会掉落。网格保持不变：
# [[1,0,0,0], 
#  [1,0,0,0]]
# 接下来消除 (1,0) 处加粗的砖块，得到网格：
# [[1,0,0,0],
#  [0,0,0,0]]
# 剩下的砖块仍然是稳定的，所以不会有砖块掉落。
# 因此，结果为 [0,0] 。 
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 200 
#  grid[i][j] 为 0 或 1 
#  1 <= hits.length <= 4 * 104 
#  hits[i].length == 2 
#  0 <= xi <= m - 1 
#  0 <= yi <= n - 1 
#  所有 (xi, yi) 互不相同 
#  
#  Related Topics 并查集 数组 矩阵 
#  👍 198 👎 0

from typing import List
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        """
        并查集。细节看官解。
        不能使用按秩合并了，要使用按节点个数合并
        """
        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv: return False
            if pu == top:
                parents[pv] = pu
                size[pu] += size[pv]
            else:
                parents[pu] = pv
                size[pv] += size[pu]
            return True

        def find(u):
            if parents[u] == u: return u
            parents[u] = find(parents[u])
            return parents[u]
        m, n = len(grid), len(grid[0])
        tmp = [grid[i][:] for i in range(m)]
        top = m * n
        parents = [i for i in range(m * n + 1)]
        size = [1 if grid[i//n][i%n] else 0 for i in range(m * n)] + [0]
        get_idx = lambda i, j: i * n + j
        ans = []
        for x, y in hits:
            tmp[x][y] = 0
        for x in range(m):
            for y in range(n):
                if not tmp[x][y]: continue
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < m and 0 <= ny < n and tmp[nx][ny] == 1) or nx == -1:
                        union(get_idx(x, y), get_idx(nx, ny) if nx != -1 else top)

        for x, y in hits[::-1]:
            if grid[x][y] == 0:
                ans.append(0)
                continue
            origin = size[top]
            tmp[x][y] = 1
            size[get_idx(x, y)] = 1
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if (0 <= nx < m and 0 <= ny < n and tmp[nx][ny] == 1) or nx == -1:
                    union(get_idx(x, y), get_idx(nx, ny) if nx != -1 else top)
            current = size[top]
            ans.append(max(0, current - origin - 1))
        return ans[::-1]

# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind:
    def __init__(self, n):
        self.f = [i for i in range(n)]
        self.sz = [1] * n
    def find(self, x):
        if self.f[x] == x:
            return x
        self.f[x] = self.find(self.f[x])
        return self.f[x]
    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy: return
        self.f[fx] = fy
        self.sz[fy] += self.sz[fx]
    def size(self, x):
        return self.sz[self.find(x)]

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        h, w = len(grid), len(grid[0])
        uf = UnionFind(h * w + 1)
        status = [grid[i][:] for i in range(h)]
        for i, j in hits:
            status[i][j] = 0
        for i in range(h):
            for j in range(w):
                if status[i][j]:
                    if i == 0:
                        uf.union(h * w, i * w + j)
                    if i > 0 and status[i - 1][j] == 1:
                        uf.union(i * w + j, (i - 1) * w + j)
                    if j > 0 and status[i][j - 1] == 1:
                        uf.union(i * w + j, i * w + j - 1)

        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        ret = [0] * len(hits)
        for i in range(len(hits) - 1, -1, -1):
            r, c = hits[i]
            if grid[r][c] == 0:
                continue
            prev = uf.size(h * w)
            if r == 0:
                uf.union(h * w, c)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < h and 0 <= nc < w and status[nr][nc] == 1:
                    uf.union(r * w + c, nr * w + nc)

            size = uf.size(h * w)
            ret[i] = max(0, size - prev - 1)
            status[r][c] = 1
        return ret

# leetcode submit region end(Prohibit modification and deletion)
grid = [[1,1,1,0,1,1,1,1],[1,0,0,0,0,1,1,1],[1,1,1,0,0,0,1,1],[1,1,0,0,0,0,0,0],[1,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0]]
hits = [[4,6],[3,0],[2,3],[2,6],[4,1],[5,2],[2,1]]
print(Solution().hitBricks(grid, hits))