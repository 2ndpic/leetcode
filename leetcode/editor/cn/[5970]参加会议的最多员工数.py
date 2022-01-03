# 一个公司准备组织一场会议，邀请名单上有 n 位员工。公司准备了一张 圆形 的桌子，可以坐下 任意数目 的员工。 
# 
#  员工编号为 0 到 n - 1 。每位员工都有一位 喜欢 的员工，每位员工 当且仅当 他被安排在喜欢员工的旁边，他才会参加会议。每位员工喜欢的员工 不会 
# 是他自己。 
# 
#  给你一个下标从 0 开始的整数数组 favorite ，其中 favorite[i] 表示第 i 位员工喜欢的员工。请你返回参加会议的 最多员工数目 。 
# 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：favorite = [2,2,1,2]
# 输出：3
# 解释：
# 上图展示了公司邀请员工 0，1 和 2 参加会议以及他们在圆桌上的座位。
# 没办法邀请所有员工参与会议，因为员工 2 没办法同时坐在 0，1 和 3 员工的旁边。
# 注意，公司也可以邀请员工 1，2 和 3 参加会议。
# 所以最多参加会议的员工数目为 3 。
#  
# 
#  示例 2： 
# 
#  输入：favorite = [1,2,0]
# 输出：3
# 解释：
# 每个员工都至少是另一个员工喜欢的员工。所以公司邀请他们所有人参加会议的前提是所有人都参加了会议。
# 座位安排同图 1 所示：
# - 员工 0 坐在员工 2 和 1 之间。
# - 员工 1 坐在员工 0 和 2 之间。
# - 员工 2 坐在员工 1 和 0 之间。
# 参与会议的最多员工数目为 3 。
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：favorite = [3,0,1,4,1]
# 输出：4
# 解释：
# 上图展示了公司可以邀请员工 0，1，3 和 4 参加会议以及他们在圆桌上的座位。
# 员工 2 无法参加，因为他喜欢的员工 0 旁边的座位已经被占领了。
# 所以公司只能不邀请员工 2 。
# 参加会议的最多员工数目为 4 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == favorite.length 
#  2 <= n <= 10⁵ 
#  0 <= favorite[i] <= n - 1 
#  favorite[i] != i 
#  
#  👍 33 👎 0
from typing import List
from collections import deque, defaultdict
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        def bfs(node):
            q = deque([i for i in g[node] if i != favorite[node]])
            ans = 1
            while q:
                for _ in range(len(q)):
                    q.extend(g[q.popleft()])
                ans += 1
            return ans

        n = len(favorite)
        g = defaultdict(list)
        deg = [0] * n
        vis = [False] * n
        for u, v in enumerate(favorite):
            # u 喜欢 v
            g[v].append(u)
            deg[v] += 1

        q = deque([i for i, v in enumerate(deg) if v == 0])
        while q:
            u = q.popleft()
            vis[u] = True
            deg[favorite[u]] -= 1
            if deg[favorite[u]] == 0:
                q.append(favorite[u])
        max_ring_size, double_ring_size = 0, 0
        for i in range(n):
            if vis[i]: continue
            ring_size, curr = 1, i
            vis[i] = True
            while favorite[curr] != i:
                curr = favorite[curr]
                vis[curr] = True
                ring_size += 1
            if ring_size > 2:
                max_ring_size = max(max_ring_size, ring_size)
            else:
                double_ring_size += bfs(i) + bfs(favorite[i])
        return max(max_ring_size, double_ring_size)


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        # 官解
        n = len(favorite)
        indeg = [0] * n
        for i in range(n):
            indeg[favorite[i]] += 1
        used = [False] * n
        f = [1] * n # f[i]表示节点i为止的最长「游走」路径经过的节点个数
        q = deque([i for i in range(n) if indeg[i] == 0])
        while q:
            u = q.popleft()
            used[u] = True
            v = favorite[u]
            f[v] = max(f[v], f[u] + 1)
            indeg[v] -= 1
            if indeg[v] == 0: q.append(v)
        # ring 表示最大的环的大小
        # total 表示所有环大小为 2 的「基环内向树」上的最长的「双向游走」路径之和
        ring, total = 0, 0
        for i in range(n):
            if not used[i]:
                j = favorite[i]
                # 环的大小为2
                if favorite[j] == i:
                    total += f[i] + f[j]
                    used[i] = used[j] = True
                else:
                    u = i
                    cnt = 0
                    while True:
                        cnt += 1
                        u = favorite[u]
                        used[u] = True
                        if u == i: break
                    ring = max(ring, cnt)
        return max(ring, total)
# leetcode submit region end(Prohibit modification and deletion)
print(Solution().maximumInvitations([2,2,1,2]))