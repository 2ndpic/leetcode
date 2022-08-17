from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
N = 1010
f2 = [0] * N
f5 = [0] * N
for i in range(2, N):
    if i % 2 == 0:
        f2[i] = f2[i // 2] + 1
    if i % 5 == 0:
        f5[i] = f5[i // 5] + 1
class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        """
        四条拐角路径：左上，左下，右上，右下
        创建四个二维前缀和数组，分别代表grid[i][j]左边2，5因子个数和上班的2，5因子个数
        例如r2[i][j]表示grid[i - 1][j - 1]左边的2因子总个数
        """
        m, n = len(grid), len(grid[0])
        r2, r5, c2, c5 = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(4)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                num = grid[i - 1][j - 1]
                r2[i][j] = r2[i][j - 1] + f2[num]
                r5[i][j] = r5[i][j - 1] + f5[num]
                c2[i][j] = c2[i - 1][j] + f2[num]
                c5[i][j] = c5[i - 1][j] + f5[num]
        ans = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 以grid[i - 1][j - 1]作为拐弯，计算4个路线的最大值，值由每条路线的2和5因子的最小值决定

                # 左上
                res1 = min(r2[i][j] + c2[i - 1][j], r5[i][j] + c5[i - 1][j])

                # 左下
                res2 = min(r2[i][j] + c2[m][j] - c2[i][j], r5[i][j] + c5[m][j] - c5[i][j])

                # 右上
                res3 = min(r2[i][n] - r2[i][j] + c2[i][j], r5[i][n] - r5[i][j] + c5[i][j])

                # 右下
                res4 = min(r2[i][n] - r2[i][j - 1] + c2[m][j] - c2[i][j], r5[i][n] - r5[i][j - 1] + c5[m][j] - c5[i][j])

                ans = max(ans, res1, res2, res3, res4)
        return ans







# leetcode submit region end(Prohibit modification and deletion)