# 给你一个points 数组，表示 2D 平面上的一些点，其中 points[i] = [xi, yi] 。 
# 
#  连接点 [xi, yi] 和点 [xj, yj] 的费用为它们之间的 曼哈顿距离 ：|xi - xj| + |yi - yj| ，其中 |val| 表示 
# val 的绝对值。 
# 
#  请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有 一条简单路径时，才认为所有点都已连接。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# 输出：20
# 解释：
# 
# 我们可以按照上图所示连接所有点得到最小总费用，总费用为 20 。
# 注意到任意两个点之间只有唯一一条路径互相到达。
#  
# 
#  示例 2： 
# 
#  
# 输入：points = [[3,12],[-2,5],[-4,1]]
# 输出：18
#  
# 
#  示例 3： 
# 
#  
# 输入：points = [[0,0],[1,1],[1,0],[-1,1]]
# 输出：4
#  
# 
#  示例 4： 
# 
#  
# 输入：points = [[-1000000,-1000000],[1000000,1000000]]
# 输出：4000000
#  
# 
#  示例 5： 
# 
#  
# 输入：points = [[0,0]]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= points.length <= 1000 
#  -106 <= xi, yi <= 106 
#  所有点 (xi, yi) 两两不同。 
#  
#  Related Topics 并查集 
#  👍 45 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
def find(u, parents):
    if u == parents[u]:
        return parents[u]
    parents[u] = find(parents[u], parents)
    return parents[u]
def union(u, v, parents, ranks):
    pu, pv = find(u, parents), find(v, parents)
    if pu == pv:
        return False
    if ranks[pu] > ranks[pv]:
        parents[pv] = pu
    elif ranks[pv] > ranks[pu]:
        parents[pu] = pv
    else:
        parents[pv] = pu
        ranks[pu] += 1
    return True

def kruskal(g, n):
    """
    :param g: [[V1, V2, weight], [V3,V4,weight]....]
    :param n: 顶点数
    :return:
    """
    n_edge, res = 0, 0
    parents = [i for i in range(n)]
    ranks = [0 for _ in range(n)]
    g.sort(key=lambda x:x[2])
    for u, v, weight in g:
        if n_edge == n-1:
            break
        if find(u, parents) != find(v, parents):
            union(u, v, parents, ranks)
            res += weight
            n_edge += 1

    if n_edge < n-1:
        res = -1
    return res

def lazy_prim(points):
    from queue import PriorityQueue
    cal_dis = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

    pq = PriorityQueue()
    visit = set(range(len(points)))
    res = 0

    pq.put((0, 0))#(dis, point) Prim算法从任何一个节点出发都是一样的，这里从0点开始
    while visit:
        dis, cur = pq.get()
        if cur not in visit:
            continue
        visit.remove(cur)
        res += dis
        for i in visit:
            pq.put((cal_dis(points[cur], points[i]), i))

    return res

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        return lazy_prim(points)
# leetcode submit region end(Prohibit modification and deletion)

print(Solution().minCostConnectPoints(points = [[0,0],[1,1],[1,0],[-1,1]]))