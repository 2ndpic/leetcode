from functools import lru_cache
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minDays(self, n: int) -> int:
        @lru_cache(None)
        def f(i):
            if i <= 1: return i
            return min(i % 2 + 1 + f(i // 2), i % 3 + 1 + f(i // 3))
        return f(n)
# leetcode submit region end(Prohibit modification and deletion)
import heapq
class Solution:
    def minDays(self, n: int) -> int:
        q = [(0, n)]
        vis = set()
        ans = 0
        while True:
            days, rest = heapq.heappop(q)
            if rest in vis:
                continue
            vis.add(rest)
            if rest == 1:
                ans = days + 1
                break
            heapq.heappush(q, (days + rest % 2 + 1, rest // 2))
            heapq.heappush(q, (days + rest % 3 + 1, rest // 3))
        return ans