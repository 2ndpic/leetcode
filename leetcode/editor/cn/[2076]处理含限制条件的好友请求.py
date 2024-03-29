# 给你一个整数 n ，表示网络上的用户数目。每个用户按从 0 到 n - 1 进行编号。 
# 
#  给你一个下标从 0 开始的二维整数数组 restrictions ，其中 restrictions[i] = [xi, yi] 意味着用户 xi 和用户 
# yi 不能 成为 朋友 ，不管是 直接 还是通过其他用户 间接 。 
# 
#  最初，用户里没有人是其他用户的朋友。给你一个下标从 0 开始的二维整数数组 requests 表示好友请求的列表，其中 requests[j] = [
# uj, vj] 是用户 uj 和用户 vj 之间的一条好友请求。 
# 
#  如果 uj 和 vj 可以成为 朋友 ，那么好友请求将会 成功 。每个好友请求都会按列表中给出的顺序进行处理（即，requests[j] 会在 
# requests[j + 1] 前）。一旦请求成功，那么对所有未来的好友请求而言， uj 和 vj 将会 成为直接朋友 。 
# 
#  返回一个 布尔数组 result ，其中元素遵循此规则：如果第 j 个好友请求 成功 ，那么 result[j] 就是 true ；否则，为 false 
# 。 
# 
#  注意：如果 uj 和 vj 已经是直接朋友，那么他们之间的请求将仍然 成功 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3, restrictions = [[0,1]], requests = [[0,2],[2,1]]
# 输出：[true,false]
# 解释：
# 请求 0 ：用户 0 和 用户 2 可以成为朋友，所以他们成为直接朋友。 
# 请求 1 ：用户 2 和 用户 1 不能成为朋友，因为这会使 用户 0 和 用户 1 成为间接朋友 (1--2--0) 。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 3, restrictions = [[0,1]], requests = [[1,2],[0,2]]
# 输出：[true,false]
# 解释：
# 请求 0 ：用户 1 和 用户 2 可以成为朋友，所以他们成为直接朋友。 
# 请求 1 ：用户 0 和 用户 2 不能成为朋友，因为这会使 用户 0 和 用户 1 成为间接朋友 (0--2--1) 。
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 5, restrictions = [[0,1],[1,2],[2,3]], requests = [[0,4],[1,2],[3,1],[3
# ,4]]
# 输出：[true,false,true,false]
# 解释：
# 请求 0 ：用户 0 和 用户 4 可以成为朋友，所以他们成为直接朋友。 
# 请求 1 ：用户 1 和 用户 2 不能成为朋友，因为他们之间存在限制。
# 请求 2 ：用户 3 和 用户 1 可以成为朋友，所以他们成为直接朋友。 
# 请求 3 ：用户 3 和 用户 4 不能成为朋友，因为这会使 用户 0 和 用户 1 成为间接朋友 (0--4--3--1) 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= n <= 1000 
#  0 <= restrictions.length <= 1000 
#  restrictions[i].length == 2 
#  0 <= xi, yi <= n - 1 
#  xi != yi 
#  1 <= requests.length <= 1000 
#  requests[j].length == 2 
#  0 <= uj, vj <= n - 1 
#  uj != vj 
#  
#  Related Topics 并查集 图 👍 12 👎 0
from typing import List
class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        def union(u, v, p, r):
            pu, pv = find(u, p), find(v, p)
            if pu == pv: return
            if r[pu] < r[pv]: p[pu] = pv
            elif r[pv] < r[pu]: p[pv] = pu
            else:
                p[pv] = pu
                r[pu] += 1

        def find(u, p):
            if u == p[u]: return u
            p[u] = find(p[u], p)
            return p[u]

        parents = [i for i in range(n)]
        ranks = [0] * n
        ans = []
        for u, v in requests:
            p = parents.copy()
            r = ranks.copy()
            union(u, v, p, r)
            for i, j in restrictions:
                if find(i, p) == find(j, p):
                    ans.append(False)
                    break
            else:
                ans.append(True)
                parents = p
                ranks = r
        return ans

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv: return
            if ranks[pu] < ranks[pv]: parents[pu] = pv
            elif ranks[pv] < ranks[pu]: parents[pv] = pu
            else:
                parents[pv] = pu
                ranks[pu] += 1

        def find(u):
            if u == parents[u]: return u
            parents[u] = find(parents[u])
            return parents[u]

        parents = [i for i in range(n)]
        ranks = [0] * n
        ans = []
        for request in requests:
            x, y = find(request[0]), find(request[1])
            if x != y:
                for restriction in restrictions:
                    u, v = find(restriction[0]), find(restriction[1])
                    if (x, y) == (u, v) or (x, y) == (v, u):
                        ans.append(False)
                        break
                else:
                    union(x, y)
                    ans.append(True)
            else:
                ans.append(True)
        return ans
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv: return
            if ranks[pu] < ranks[pv]: parents[pu] = pv
            elif ranks[pv] < ranks[pu]: parents[pv] = pu
            else:
                parents[pv] = pu
                ranks[pu] += 1

        def find(u):
            if u == parents[u]: return u
            parents[u] = find(parents[u])
            return parents[u]

        parents = [i for i in range(n)]
        ranks = [0] * n
        ans = []
        for request in requests:
            x, y = find(request[0]), find(request[1])
            if x != y:
                for restriction in restrictions:
                    u, v = find(restriction[0]), find(restriction[1])
                    if (x, y) == (u, v) or (x, y) == (v, u):
                        ans.append(False)
                        break
                else:
                    union(x, y)
                    ans.append(True)
            else:
                ans.append(True)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
n = 3
estrictions = [[0,1]]
requests = [[1,2],[0,2]]
print(Solution().friendRequests(n, estrictions, requests))
