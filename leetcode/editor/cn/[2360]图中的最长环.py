from typing import List
from collections import deque, Counter
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        inDeg = Counter(edges)
        q = deque([i for i in range(n) if inDeg[i] == 0])
        vis = [False] * n
        while q:
            u = q.popleft()
            vis[u] = True
            v = edges[u]
            if v != -1:
                inDeg[v] -= 1
                if inDeg[v] == 0:
                    q.append(v)
        ans = -1
        for i in range(n):
            if not vis[i]:
                u, curr = i, 0
                while not vis[u]:
                    vis[u] = True
                    curr += 1
                    u = edges[u]
                ans = max(ans, curr)
        return ans


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        time = [0] * len(edges)
        clock, ans = 1, -1
        for x, t in enumerate(time):
            if t > 0: continue
            start_time = clock
            while x != -1:
                if time[x]:
                    if time[x] >= start_time:
                        ans = max(ans, clock - time[x])
                    break
                time[x] = clock
                clock += 1
                x = edges[x]
        return ans



# leetcode submit region end(Prohibit modification and deletion)
edges = [3,3,4,2,3]
print(Solution().longestCycle(edges))
