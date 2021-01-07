# 
#  
#  有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连
# 。 
# 
#  省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。 
# 
#  给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 
# isConnected[i][j] = 0 表示二者不直接相连。 
# 
#  返回矩阵中 省份 的数量。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# 输出：2
#  
# 
#  示例 2： 
# 
#  
# 输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 200 
#  n == isConnected.length 
#  n == isConnected[i].length 
#  isConnected[i][j] 为 1 或 0 
#  isConnected[i][i] == 1 
#  isConnected[i][j] == isConnected[j][i] 
#  
#  
#  
#  Related Topics 深度优先搜索 并查集 
#  👍 418 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
# def union(u, v, ranks, parents):
#     pu, pv = find(u, parents), find(v, parents)
#     ru, rv = ranks[pu], ranks[pv]
#     # 按秩合并
#     if pu == pv:
#         return False
#     if ru > rv:
#         parents[pv] = pu
#     elif rv > ru:
#         parents[pu] = pv
#     else:
#         parents[pv] = pu
#         ranks[pu] += 1
#     return True
#
# def find(u, parents):
#     # 路径压缩
#     if u == parents[u]:
#         return u
#     parents[u] = find(parents[u], parents)
#     return parents[u]
#
# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         """
#         若以并查集的思路，此题考察的就是一共有多少个没有相连的集合
#         因为isConnected是无向图，所以可以只遍历上半部分
#         """
#         n = len(isConnected)
#         parents = [i for i in range(n)]
#         ranks = [0] * n
#         for i in range(n):
#             for j in range(i+1, n):
#                 if isConnected[i][j] == 1:
#                     union(i, j, ranks, parents)
#         res = set()
#         for i in range(n):
#             res.add(find(i, parents))
#         return len(res)
def dfs(u, g, citys):
    for i in range(len(g)):
        if g[u][i] and i in citys:
            citys.remove(i)
            dfs(i, g, citys)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        以DFS的思路，就会想到isConnected实际上是一个图的邻接矩阵
        那么要解决这个图中省份的数量问题，就转化成要使用多少次DFS才能遍历完这张图
        """
        citys = set(range(len(isConnected)))
        res = 0
        while citys:
            dfs(citys.pop(), isConnected, citys)
            res += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
print(Solution().findCircleNum(isConnected))