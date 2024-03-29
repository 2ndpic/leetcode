# 存在一个由 n 个节点组成的无向连通图，图中的节点按从 0 到 n - 1 编号。 
# 
#  给你一个数组 graph 表示这个图。其中，graph[i] 是一个列表，由所有与节点 i 直接相连的节点组成。 
# 
#  返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：graph = [[1,2,3],[0],[0],[0]]
# 输出：4
# 解释：一种可能的路径为 [1,0,2,0,3] 
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
# 输出：4
# 解释：一种可能的路径为 [0,1,4,2,3]
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == graph.length 
#  1 <= n <= 12 
#  0 <= graph[i].length < n 
#  graph[i] 不包含 i 
#  如果 graph[a] 包含 b ，那么 graph[b] 也包含 a 
#  输入的图总是连通图 
#  
#  Related Topics 位运算 广度优先搜索 图 动态规划 状态压缩 
#  👍 171 👎 0

from typing import List
from collections import deque
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q = deque((i, 1 << i, 0) for i in range(n))
        ans = 0
        seen = {(i, 1 << i) for i in range(n)}
        while q:
            u, mask, dist = q.popleft()
            if mask == (1 << n) - 1:
                ans = dist
                break
            for v in graph[u]:
                mask_v = mask | (1 << v)
                if (v, mask_v) not in seen:
                    q.append((v, mask_v, dist + 1))
                    seen.add((v, mask_v))
        return ans

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        """
        官解
        """
        n = len(graph)
        d = [[n + 1] * n for _ in range(n)]
        for i in range(n):
            for j in graph[i]:
                d[i][j] = 1
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        f = [[float('inf')] * (1 << n) for _ in range(n)]
        for mask in range(1, 1 << n):
            if mask & (mask - 1) == 0:
                u = bin(mask).count("0") - 1
                f[u][mask] = 0
            else:
                for u in range(n):
                    if mask & (1 << u):
                        for v in range(n):
                            if mask & (1 << v) and u != v:
                                f[u][mask] = min(f[u][mask],
                                                 f[v][mask ^ (1 << u)] + d[v][u])
        ans = min(f[i][(1 << n) - 1] for i in range(n))
        return ans
# leetcode submit region end(Prohibit modification and deletion)
graph = [[1,2,3],[0],[0],[0]]
graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
print(Solution().shortestPathLength(graph))