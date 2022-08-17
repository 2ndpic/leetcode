from typing import List
from functools import lru_cache
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        """
        f[i][j]表示考虑piles[i,..,n-1]堆，在可拿前1...2*j堆石头的情况下，先手可获得最大的分数
        - i + 2j >= n: 那么先手可一次拿完，f[i][j] = sum(piles[i...n-1])
        - i + 2j  < n: f[i][j] = sum(piles[i...n-1]) - min(f[i + k][max(j, k)] for k in range(1, 2 * j + 1))
                        2j <= n - 1
        """
        n = len(piles)

        f = [[0] * (n + 1) for _ in range(n)]
        suffix_sum = 0
        for i in range(n - 1, -1, -1):
            suffix_sum += piles[i]
            for j in range(1, n + 1):
                if i + 2 * j >= n:
                    backhand = 0
                else:
                    backhand = min(f[i + k][max(j, k)] for k in range(1, 2 * j + 1))
                f[i][j] = suffix_sum - backhand

        return f[0][1]

# leetcode submit region end(Prohibit modification and deletion)
