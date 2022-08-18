from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minDifficulty(self, job: List[int], d: int) -> int:
        """
        f[i][j]表示考虑前i个任务，j天的总难度，答案f[n][d]
        限制i >= j
        f[i][j] = min(f[i - 1][j - 1] + max(j[i - 1]),
                      f[i - 2][j - 1] + max(j[i - 1,..,i - 2]) ...
                      f[i - k][j - 1] + max(j[i - 1,..,i - k])
                    遍历中保证i - k >= j - 1 -> 1 <= k <= i - j + 1
        """
        n = len(job)
        if n <= d: return -1 if n < d else sum(job)
        # g[i][j]表示区间[i..j]的最大值
        g = [[-1] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                g[i][j] = max(g[i][j - 1], job[j])

        f = [[float('inf')] * (d + 1) for _ in range(n + 1)]
        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(i + 1, d + 1)):
                for k in range(1, i - j + 2):
                    f[i][j] = min(f[i][j], f[i - k][j - 1] + g[i - k][i - 1])
        return f[n][d]
# leetcode submit region end(Prohibit modification and deletion)

class Solution:
    def minDifficulty(self, job: List[int], d: int) -> int:
        """
        f[i][j]表示考虑前i个任务，j天的总难度，答案f[n][d]
        限制i >= j
        f[i][j] = min(f[i - 1][j - 1] + max(j[i - 1]),
                      f[i - 2][j - 1] + max(j[i - 1,..,i - 2]) ...
                      f[i - k][j - 1] + max(j[i - 1,..,i - k])
                    遍历中保证i - k >= j - 1 -> 1 <= k <= i - j + 1
        """

        @cache
        def f(i, j):
            if j == 1:
                return g[0][i - 1]

            ans = float('inf')
            for k in range(1, i - j + 2):
                ans = min(ans, f(i - k, j - 1) + g[i - k][i - 1])
            return ans

        n = len(job)
        if n < d: return -1
        # g[i][j]表示区间[i..j]的最大值
        g = [[-1] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                g[i][j] = max(g[i][j - 1], job[j])
        return f(n, d)