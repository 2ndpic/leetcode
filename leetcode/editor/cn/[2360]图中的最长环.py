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

# leetcode submit region end(Prohibit modification and deletion)
edges = [3,3,4,2,3]
print(Solution().longestCycle(edges))
