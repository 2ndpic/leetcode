# Alice 和 Bob 共有一个无向图，其中包含 n 个节点和 3 种类型的边： 
# 
#  
#  类型 1：只能由 Alice 遍历。 
#  类型 2：只能由 Bob 遍历。 
#  类型 3：Alice 和 Bob 都可以遍历。 
#  
# 
#  给你一个数组 edges ，其中 edges[i] = [typei, ui, vi] 表示节点 ui 和 vi 之间存在类型为 typei 的双向边。请
# 你在保证图仍能够被 Alice和 Bob 完全遍历的前提下，找出可以删除的最大边数。如果从任何节点开始，Alice 和 Bob 都可以到达所有其他节点，则认为图
# 是可以完全遍历的。 
# 
#  返回可以删除的最大边数，如果 Alice 和 Bob 无法完全遍历图，则返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
# 输出：2
# 解释：如果删除 [1,1,2] 和 [1,1,3] 这两条边，Alice 和 Bob 仍然可以完全遍历这个图。再删除任何其他的边都无法保证图可以完全遍历。所
# 以可以删除的最大边数是 2 。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
# 输出：0
# 解释：注意，删除任何一条边都会使 Alice 和 Bob 无法完全遍历这个图。
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
# 输出：-1
# 解释：在当前图中，Alice 无法从其他节点到达节点 4 。类似地，Bob 也不能达到节点 1 。因此，图无法完全遍历。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 10^5 
#  1 <= edges.length <= min(10^5, 3 * n * (n-1) / 2) 
#  edges[i].length == 3 
#  1 <= edges[i][0] <= 3 
#  1 <= edges[i][1] < edges[i][2] <= n 
#  所有元组 (typei, ui, vi) 互不相同 
#  
#  Related Topics 并查集 
#  👍 44 👎 0

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
    if ranks[pu] > ranks[pv]: parents[pv] = pu
    elif ranks[pv] > ranks[pu]: parents[pu] = pv
    else:
        parents[pv] = pu
        ranks[pu] += 1
    return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        parents = [[i for i in range(n+1)] for _ in range(2)]
        ranks = [[0 for _ in range(n+1)] for _ in range(2)]
        edges.sort(key=lambda x : -x[0])  # ab,b,a
        res = 0
        for tp, u, v in edges:
            if tp == 3:
                # if union(u, v, parents[0], ranks[0]) == False and union(u, v, parents[1], ranks[1]) == False:
                # if union(u, v, parents[0], ranks[0])==False & union(u, v, parents[1], ranks[1])==False:
                if union(u, v, parents[0], ranks[0]) + union(u, v, parents[1], ranks[1]) == 0:
                    res += 1
            elif not union(u, v, parents[tp - 1], ranks[tp - 1]):
                res += 1

        a, b = find(1, parents[0]), find(1, parents[1])
        for i in range(2, n+1):
            if find(i, parents[0]) != a: return -1
            if find(i, parents[1]) != b: return -1

        return res

# leetcode submit region end(Prohibit modification and deletion)
n = 13
edges = [[1,1,2],[2,1,3],[3,2,4],[3,2,5],[1,2,6],[3,6,7],[3,7,8],[3,6,9],[3,4,10],[2,3,11],[1,5,12],[3,3,13],[2,1,10],[2,6,11],[3,5,13],[1,9,12],[1,6,8],[3,6,13],[2,1,4],[1,1,13],[2,9,10],[2,1,6],[2,10,13],[2,2,9],[3,4,12],[2,4,7],[1,1,10],[1,3,7],[1,7,11],[3,3,12],[2,4,8],[3,8,9],[1,9,13],[2,4,10],[1,6,9],[3,10,13],[1,7,10],[1,1,11],[2,4,9],[3,5,11],[3,2,6],[2,1,5],[2,5,11],[2,1,7],[2,3,8],[2,8,9],[3,4,13],[3,3,8],[3,3,11],[2,9,11],[3,1,8],[2,1,8],[3,8,13],[2,10,11],[3,1,5],[1,10,11],[1,7,12],[2,3,5],[3,1,13],[2,4,11],[2,3,9],[2,6,9],[2,1,13],[3,1,12],[2,7,8],[2,5,6],[3,1,9],[1,5,10],[3,2,13],[2,3,6],[2,2,10],[3,4,11],[1,4,13],[3,5,10],[1,4,10],[1,1,8],[3,3,4],[2,4,6],[2,7,11],[2,7,10],[2,3,12],[3,7,11],[3,9,10],[2,11,13],[1,1,12],[2,10,12],[1,7,13],[1,4,11],[2,4,5],[1,3,10],[2,12,13],[3,3,10],[1,6,12],[3,6,10],[1,3,4],[2,7,9],[1,3,11],[2,2,8],[1,2,8],[1,11,13],[1,2,13],[2,2,6],[1,4,6],[1,6,11],[3,1,2],[1,1,3],[2,11,12],[3,2,11],[1,9,10],[2,6,12],[3,1,7],[1,4,9],[1,10,12],[2,6,13],[2,2,12],[2,1,11],[2,5,9],[1,3,8],[1,7,8],[1,2,12],[1,5,11],[2,7,12],[3,1,11],[3,9,12],[3,2,9],[3,10,11]]
print(Solution().maxNumEdgesToRemove(n, edges))  #114