# 有 n 个网络节点，标记为 1 到 n。 
# 
#  给你一个列表 times，表示信号经过 有向 边的传递时间。 times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点， w
# i 是一个信号从源节点传递到目标节点的时间。 
# 
#  现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# 输出：2
#  
# 
#  示例 2： 
# 
#  
# 输入：times = [[1,2,1]], n = 2, k = 1
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：times = [[1,2,1]], n = 2, k = 2
# 输出：-1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= n <= 100 
#  1 <= times.length <= 6000 
#  times[i].length == 3 
#  1 <= ui, vi <= n 
#  ui != vi 
#  0 <= wi <= 100 
#  所有 (ui, vi) 对都 互不相同（即，不含重复边） 
#  
#  Related Topics 深度优先搜索 广度优先搜索 图 最短路 堆（优先队列） 
#  👍 347 👎 0
from typing import List
import heapq
import collections
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def dijkstra(start):
            # 保存最短路结果
            result = [-1 if i != start else 0 for i in range(n + 1)]
            # 初始化未求出最短路的点，pq存储距离start的距离,seen表示求出最短路的点
            pq, seen = [(0, start)], set()
            while pq:
                d, u = heapq.heappop(pq)
                seen.add(u)
                for v in g[u]:
                    if v not in seen:
                        if result[v] == -1 or d + g[u][v] < result[v]:
                            heapq.heappush(pq, (d + g[u][v], v))
                            result[v] = d + g[u][v]
            return result[1:]

        g = collections.defaultdict(dict)
        for u, v, w in times:
            g[u][v] = w
        result = dijkstra(k)
        return max(result) if -1 not in result else -1
# leetcode submit region end(Prohibit modification and deletion)
times = [[2,1,1],[2,3,1],[3,4,1]]; n = 4; k = 2
times = [[1,2,1]]; n = 2; k = 2
print(Solution().networkDelayTime(times, n, k))