# 给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是 名称 (name)，其
# 余元素是 emails 表示该账户的邮箱地址。 
# 
#  现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为
# 人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。 
# 
#  合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是按顺序排列的邮箱地址。账户本身可以以任意顺序返回。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnn
# ybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Ma
# ry", "mary@mail.com"]]
# 输出：
# [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  
# ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
# 解释：
# 第一个和第三个 John 是同一个人，因为他们有共同的邮箱地址 "johnsmith@mail.com"。 
# 第二个 John 和 Mary 是不同的人，因为他们的邮箱地址没有被其他帐户使用。
# 可以以任何顺序返回这些列表，例如答案 [['Mary'，'mary@mail.com']，['John'，'johnnybravo@mail.com']，
# ['John'，'john00@mail.com'，'john_newyork@mail.com'，'johnsmith@mail.com']] 也是正确的
# 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  accounts的长度将在[1，1000]的范围内。 
#  accounts[i]的长度将在[1，10]的范围内。 
#  accounts[i][j]的长度将在[1，30]的范围内。 
#  
#  Related Topics 深度优先搜索 并查集 
#  👍 156 👎 0
# def find(u, parents):
#     if u == parents[u]:
#         return u
#     parents[u] = find(parents[u], parents)
#     return parents[u]
# def union(u, v, parents, ranks):
#     pu, pv = find(u, parents), find(v, parents)
#     ru, rv = ranks[pu], ranks[pv]
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
# class Solution:
#     def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
#         n = len(accounts)
#         parents = [i for i in range(n)]
#         ranks = [0 for _ in range(n)]
#         mail2accidx = {}
#         for i in range(n):
#             for j in range(1, len(accounts[i])):
#                 mail = accounts[i][j]
#                 if mail not in mail2accidx:
#                     mail2accidx[mail] = i
#                 else:
#                     union(i, mail2accidx[mail], parents, ranks)
#         d = {}
#         for key, value in mail2accidx.items():
#             d.setdefault(find(value, parents), []).append(key)
#         res = []
#         for key, value in d.items():
#             name = accounts[key][0]
#             res.append([name] + sorted(value))
#         return res
# from typing import List
from typing import List
import collections
# leetcode submit region begin(Prohibit modification and deletion)
def dfs(g, start, visited, paths):
    if start in visited:
        return
    visited.add(start)
    paths.append(start)
    for neighbor in g[start]:
        dfs(g, neighbor, visited, paths)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        g = collections.defaultdict(list)
        for each_acc in accounts:
            email_0 = each_acc[1]
            for each_email in each_acc[2:]:
                g[email_0].append(each_email)
                g[each_email].append(email_0)
        visited = set()
        res = []
        for each_acc in accounts:
            name = each_acc[0]
            mails = []
            dfs(g, each_acc[1], visited, mails)
            if mails:
                res.append([name]+sorted(mails))
        return res

# leetcode submit region end(Prohibit modification and deletion)
accounts = [["Fern","Fern8@m.co","Fern9@m.co"],
            ["Fern","Fern7@m.co","Fern8@m.co"],
            ["Fern","Fern4@m.co","Fern5@m.co"],
            ["Fern","Fern10@m.co","Fern11@m.co"],
            ["Fern","Fern9@m.co","Fern10@m.co"],
            ["Fern","Fern6@m.co","Fern7@m.co"],
            ["Fern","Fern1@m.co","Fern2@m.co"],
            ["Fern","Fern11@m.co","Fern12@m.co"],
            ["Fern","Fern3@m.co","Fern4@m.co"],
            ["Fern","Fern2@m.co","Fern3@m.co"],
            ["Fern","Fern5@m.co","Fern6@m.co"],
            ["Fern","Fern0@m.co","Fern1@m.co"]]

# 答案：[["Fern","Fern0@m.co","Fern10@m.co","Fern11@m.co","Fern12@m.co","Fern1@m.co","Fern2@m.co","Fern3@m.co","Fern4@m.co","Fern5@m.co","Fern6@m.co","Fern7@m.co","Fern8@m.co","Fern9@m.co"]]

print(Solution().accountsMerge(accounts))