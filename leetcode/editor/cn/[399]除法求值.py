# 给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 values
# [i] 共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。 
# 
#  另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj =
#  ? 的结果作为答案。 
# 
#  返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。 
# 
#  
# 
#  注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"]
# ,["b","a"],["a","e"],["a","a"],["x","x"]]
# 输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
# 解释：
# 条件：a / b = 2.0, b / c = 3.0
# 问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# 结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]
#  
# 
#  示例 2： 
# 
#  
# 输入：equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], quer
# ies = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# 输出：[3.75000,0.40000,5.00000,0.20000]
#  
# 
#  示例 3： 
# 
#  
# 输入：equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a
# ","c"],["x","y"]]
# 输出：[0.50000,2.00000,-1.00000,-1.00000]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= equations.length <= 20 
#  equations[i].length == 2 
#  1 <= Ai.length, Bi.length <= 5 
#  values.length == equations.length 
#  0.0 < values[i] <= 20.0 
#  1 <= queries.length <= 20 
#  queries[i].length == 2 
#  1 <= Cj.length, Dj.length <= 5 
#  Ai, Bi, Cj, Dj 由小写英文字母与数字组成 
#  
#  Related Topics 并查集 图 
#  👍 319 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)

class Node:
    def __init__(self, name=None):
        self.name = name
        self.parent = self
        self.rank = 0
        self.value = 1
        self.nodes = {self}

def union(u, v, ratio):
    pu = find(u)
    pv = find(v)
    ratio = v.value * ratio / u.value
    if pu == pv:
        return False
    elif pu.rank > pv.rank:
        pv.parent = pu
        for each in pu.nodes:
            each.value *= ratio
        pu.nodes = pu.nodes.union(pv.nodes)
    elif pv.rank > pu.rank:
        pu.parent = pv
        for each in pu.nodes:
            each.value *= ratio
        pv.nodes = pv.nodes.union(pu.nodes)
    else:
        pv.parent = pu
        for each in pu.nodes:
            each.value *= ratio
        pu.nodes = pu.nodes.union(pv.nodes)
        pu.rank += 1
    return True

def find(u):
    if u.parent == u:
        return u
    u.parent = find(u.parent)
    return u.parent

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        all_vars = dict()
        for (u, v) , ratio in zip(equations, values):
            u, v = all_vars.setdefault(u,Node(u)), all_vars.setdefault(v, Node(v))
            union(u, v, ratio)

        res = []
        for u, v in queries:
            u, v = all_vars.get(u, Node()), all_vars.get(v, Node())
            if find(u) != find(v):
                res.append(-1)
            else:
                res.append(u.value/v.value)

        return res
# leetcode submit region end(Prohibit modification and deletion)
