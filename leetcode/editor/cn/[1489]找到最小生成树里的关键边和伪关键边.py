# 给你一个 n 个点的带权无向连通图，节点编号为 0 到 n-1 ，同时还有一个数组 edges ，其中 edges[i] = [fromi, toi, we
# ighti] 表示在 fromi 和 toi 节点之间有一条带权无向边。最小生成树 (MST) 是给定图中边的一个子集，它连接了所有节点且没有环，而且这些边的权
# 值和最小。 
# 
#  请你找到给定图中最小生成树的所有关键边和伪关键边。如果从图中删去某条边，会导致最小生成树的权值和增加，那么我们就说它是一条关键边。伪关键边则是可能会出现在
# 某些最小生成树中但不会出现在所有最小生成树中的边。 
# 
#  请注意，你可以分别以任意顺序返回关键边的下标和伪关键边的下标。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
# 输出：[[0,1],[2,3,4,5]]
# 解释：上图描述了给定图。
# 下图是所有的最小生成树。
# 
# 注意到第 0 条边和第 1 条边出现在了所有最小生成树中，所以它们是关键边，我们将这两个下标作为输出的第一个列表。
# 边 2，3，4 和 5 是所有 MST 的剩余边，所以它们是伪关键边。我们将它们作为输出的第二个列表。
#  
# 
#  示例 2 ： 
# 
#  
# 
#  输入：n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
# 输出：[[],[0,1,2,3]]
# 解释：可以观察到 4 条边都有相同的权值，任选它们中的 3 条可以形成一棵 MST 。所以 4 条边都是伪关键边。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= n <= 100 
#  1 <= edges.length <= min(200, n * (n - 1) / 2) 
#  edges[i].length == 3 
#  0 <= fromi < toi < n 
#  1 <= weighti <= 1000 
#  所有 (fromi, toi) 数对都是互不相同的。 
#  
#  Related Topics 深度优先搜索 并查集 
#  👍 33 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
def find(u, parents):
    if u != parents[u]:
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

def kruskal(g, n, edge=None):
    parents = [i for i in range(n)]
    ranks = [0 for _ in range(n)]
    cost = 0
    n_edges = 0
    w = float('inf')
    if edge:
        union(edge[0], edge[1], parents, ranks)
        cost += edge[2]
        n_edges += 1
        w = edge[2]
    for u, v, weight in g:
        if n_edges == n-1:
            break
        if union(u, v, parents, ranks):
            cost += weight
            n_edges += 1
            w = weight

    return cost if n_edges == n-1 else float('inf'), w
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        arg = sorted(range(len(edges)), key=lambda x: edges[x][2])
        g = [edges[x] for x in arg]

        cost, w = kruskal(g, n)
        res = [[], []]
        for i in range(len(g)):
            if g[i][2] > w:
                break
            g_temp = g[:i] + g[i+1:]
            if kruskal(g_temp, n)[0] > cost:          # 判断关键边
                res[0].append(arg[i])
            elif kruskal(g_temp, n, g[i])[0] == cost: # 判断伪关键边
                res[1].append(arg[i])
        return res

# leetcode submit region end(Prohibit modification and deletion)
n = 14
edges = [[0,1,13],[0,2,6],[2,3,13],[3,4,4],[0,5,11],[4,6,14],[4,7,8],[2,8,6],[4,9,6],[7,10,4],[5,11,3],[6,12,7],
         [12,13,9],[7,13,2],[5,13,10],[0,6,4],[2,7,3],[0,7,8],[1,12,9],[10,12,11],[1,2,7],[1,3,10],[3,10,6],
         [6,10,4],[4,8,5],[1,13,4],[11,13,8],[2,12,10],[5,8,1],[3,7,6],[7,12,12],[1,7,9],[5,9,1],[2,13,10],
         [10,11,4],[3,5,10],[6,11,14],[5,12,3],[0,8,13],[8,9,1],[3,6,8],[0,3,4],[2,9,6],[0,11,4],[2,5,14],
         [4,11,2],[7,11,11],[1,11,6],[2,10,12],[0,13,4],[3,9,9],[4,12,3],[6,7,10],[6,8,13],[9,11,3],[1,6,2],
         [2,4,12],[0,10,3],[3,12,1],[3,8,12],[1,8,6],[8,13,2],[10,13,12],[9,13,11],[2,11,14],[5,10,9],[5,6,10],
         [2,6,9],[4,10,7],[3,13,10],[4,13,3],[3,11,9],[7,9,14],[6,9,5],[1,5,12],[4,5,3],[11,12,3],[0,4,8],[5,7,8],
         [9,12,13],[8,12,12],[1,10,6],[1,9,9],[7,8,9],[9,10,13],[8,11,3],[6,13,7],[0,12,10],[1,4,8],[8,10,2]]
# [[3],[0,1,2,4,5,6]]
print(Solution().findCriticalAndPseudoCriticalEdges(n, edges))
print([[13,16,45,55,57,58,61,89],[10,15,23,25,28,32,37,39,51,54,70,75,76,85]])