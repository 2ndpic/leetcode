# 城市用一个 双向连通 图表示，图中有 n 个节点，从 1 到 n 编号（包含 1 和 n）。图中的边用一个二维整数数组 edges 表示，其中每个 
# edges[i] = [ui, vi] 表示一条节点 ui 和节点 vi 之间的双向连通边。每组节点对由 最多一条 边连通，顶点不存在连接到自身的边。穿过任意一条边的时
# 间是 time 分钟。 
# 
#  每个节点都有一个交通信号灯，每 change 分钟改变一次，从绿色变成红色，再由红色变成绿色，循环往复。所有信号灯都 同时 改变。你可以在 任何时候 进入
# 某个节点，但是 只能 在节点 信号灯是绿色时 才能离开。如果信号灯是 绿色 ，你 不能 在节点等待，必须离开。 
# 
#  第二小的值 是 严格大于 最小值的所有值中最小的值。 
# 
#  
#  例如，[2, 3, 4] 中第二小的值是 3 ，而 [2, 2, 4] 中第二小的值是 4 。 
#  
# 
#  给你 n、edges、time 和 change ，返回从节点 1 到节点 n 需要的 第二短时间 。 
# 
#  注意： 
# 
#  
#  你可以 任意次 穿过任意顶点，包括 1 和 n 。 
#  你可以假设在 启程时 ，所有信号灯刚刚变成 绿色 。 
#  
# 
#  
# 
#  示例 1： 
# 
#          
# 
#  
# 输入：n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5
# 输出：13
# 解释：
# 上面的左图展现了给出的城市交通图。
# 右图中的蓝色路径是最短时间路径。
# 花费的时间是：
# - 从节点 1 开始，总花费时间=0
# - 1 -> 4：3 分钟，总花费时间=3
# - 4 -> 5：3 分钟，总花费时间=6
# 因此需要的最小时间是 6 分钟。
# 
# 右图中的红色路径是第二短时间路径。
# - 从节点 1 开始，总花费时间=0
# - 1 -> 3：3 分钟，总花费时间=3
# - 3 -> 4：3 分钟，总花费时间=6
# - 在节点 4 等待 4 分钟，总花费时间=10
# - 4 -> 5：3 分钟，总花费时间=13
# 因此第二短时间是 13 分钟。      
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：n = 2, edges = [[1,2]], time = 3, change = 2
# 输出：11
# 解释：
# 最短时间路径是 1 -> 2 ，总花费时间 = 3 分钟
# 最短时间路径是 1 -> 2 -> 1 -> 2 ，总花费时间 = 11 分钟 
# 
#  
# 
#  提示： 
# 
#  
#  2 <= n <= 10⁴ 
#  n - 1 <= edges.length <= min(2 * 10⁴, n * (n - 1) / 2) 
#  edges[i].length == 2 
#  1 <= ui, vi <= n 
#  ui != vi 
#  不含重复边 
#  每个节点都可以从其他节点直接或者间接到达 
#  1 <= time, change <= 10³ 
#  
#  Related Topics 广度优先搜索 图 最短路 👍 84 👎 0
from typing import List
from collections import deque
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        # dist[i][0]表示从1到i的最短路径长度，dist[i][1]表示从i到1的严格次短路径长度
        dist = [[float('inf'), float('inf')] for _ in range(n + 1)]
        dist[1][0] = 0
        q = deque([(1, 0)])
        while dist[n][1] == float('inf'):
            x, xd = q.popleft()
            for y in graph[x]:
                yd = xd + 1
                if yd < dist[y][0]:
                    q.append((y, yd))
                    dist[y][0] = yd
                elif dist[y][0] < yd < dist[y][1]:
                    q.append((y, yd))
                    dist[y][1] = yd
        """
        给出路径长度如何计算时间，假设到达节点i的时间为ti，则到达i+1的时间为：
        ti+1 = ti + twait + time
        因为只能在绿灯出发，所以可能有一个wait的时间来等待当前红灯bianlv
        绿灯的开启时间段在0,2*change, 4*change, ...,(2k) * change
        """
        ans = 0
        for _ in range(dist[n][1]):
            if ans % (2 * change) >= change:
                ans += 2 * change - ans % (change * 2)
            ans += time
        return ans

# leetcode submit region end(Prohibit modification and deletion)
