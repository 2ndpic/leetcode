# 有 n 个城市通过一些航班连接。给你一个数组 flights ，其中 flights[i] = [fromi, toi, pricei] ，表示该航班都从城
# 市 fromi 开始，以价格 pricei 抵达 toi。 
# 
#  现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到出一条最多经过 k 站中转的路线，使得从 src 到 dst 的 价格最便
# 宜 ，并返回该价格。 如果不存在这样的路线，则输出 -1。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# 输出: 200
# 解释: 
# 城市航班图如下
# 
# 
# 从城市 0 到城市 2 在 1 站中转以内的最便宜价格是 200，如图中红色所示。 
# 
#  示例 2： 
# 
#  
# 输入: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# 输出: 500
# 解释: 
# 城市航班图如下
# 
# 
# 从城市 0 到城市 2 在 0 站中转以内的最便宜价格是 500，如图中蓝色所示。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 100 
#  0 <= flights.length <= (n * (n - 1) / 2) 
#  flights[i].length == 3 
#  0 <= fromi, toi < n 
#  fromi != toi 
#  1 <= pricei <= 10⁴ 
#  航班没有重复，且不存在自环 
#  0 <= src, dst, k < n 
#  src != dst 
#  
#  Related Topics 深度优先搜索 广度优先搜索 图 动态规划 最短路 堆（优先队列） 👍 357 👎 0
from typing import List
from functools import lru_cache
from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        DFS + 记忆化搜索
        """
        @lru_cache(None)
        def dfs(u, stops):
            ans = g[u][dst] if dst in g[u] else float('inf')
            if stops == k:
                return ans
            for v in g[u]:
                ans = min(ans, dfs(v, stops + 1) + g[u][v])
            return ans
        g = defaultdict(dict)
        for u, v, c in flights:
            g[u][v] = c
        res = dfs(src, 0)
        return res if res < float('inf') else -1
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        动态规划
        """
        g = defaultdict(dict)
        for u, v, c in flights:
            g[u][v] = c
        ans = g[src][dst] if dst in g[src] else float('inf')
        f1 = {u:c for u, c in g[src].items()}
        for i in range(1, k + 1):
            f2 = defaultdict(lambda: float('inf'))
            for k, price in f1.items():
                for j in g[k]:
                    f2[j] = min(f2[j], price + g[k][j])
            f1 = f2
            if dst in f1: ans = min(ans, f1[dst])
        return ans if ans < float('inf') else -1
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        f = [[float('inf')] * n for _ in range(k + 2)]
        f[0][src], ans = 0, float('inf')
        for t in range(1, k + 2):
            for j, i, c in flights:
                f[t][i] = min(f[t][i], f[t - 1][j] + c)
            ans = min(ans, f[t][dst])
        return ans if ans < float('inf') else -1
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = defaultdict(dict)
        for u, v, c in flights:
            g[u][v] = c
        pq = [(0, src, 0)]
        costs = [float('inf') if i != src else 0 for i in range(n)]
        stops = [0] * n
        # seen = set()
        while pq:
            cost, vertex, stop = heapq.heappop(pq)
            if vertex == dst: return cost
            if stop >= k + 1: continue
            # seen.add(vertex)
            for u in g[vertex]:
                # if u in seen: continue
                if cost + g[vertex][u] < costs[u]:
                    costs[u] = cost + g[vertex][u]
                    stops[u] = stop + 1
                    heapq.heappush(pq, (costs[u], u, stops[u]))
                elif stop + 1 < stops[u]:
                    heapq.heappush(pq, (cost + g[vertex][u], u, stop + 1))
        return -1

# leetcode submit region end(Prohibit modification and deletion)
n = 11
flights = [[0,3,3],[3,4,3],[4,1,3],[0,5,1],[5,1,100],[0,6,2],[6,1,100],[0,7,1],[7,8,1],[8,9,1],[9,1,1],[1,10,1],[10,2,1],[1,2,100]]
src = 0
dst = 2
k = 4
# n = 4; src = 0; dst = 3; k = 1
# flights = [[0,1,10],[0,2,40],[1,2,20],[2,3,40]]
print(Solution().findCheapestPrice(n, flights, src, dst, k))