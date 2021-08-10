# 你正在设计一个动态数组。给你一个下标从 0 开始的整数数组 nums ，其中 nums[i] 是 i 时刻数组中的元素数目。除此以外，你还有一个整数 k ，
# 表示你可以 调整 数组大小的 最多 次数（每次都可以调整成 任意 大小）。 
# 
#  t 时刻数组的大小 sizet 必须大于等于 nums[t] ，因为数组需要有足够的空间容纳所有元素。t 时刻 浪费的空间 为 sizet - nums[
# t] ，总 浪费空间为满足 0 <= t < nums.length 的每一个时刻 t 浪费的空间 之和 。 
# 
#  在调整数组大小不超过 k 次的前提下，请你返回 最小总浪费空间 。 
# 
#  注意：数组最开始时可以为 任意大小 ，且 不计入 调整大小的操作次数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [10,20], k = 0
# 输出：10
# 解释：size = [20,20].
# 我们可以让数组初始大小为 20 。
# 总浪费空间为 (20 - 10) + (20 - 20) = 10 。
#  
# 
#  示例 2： 
# 
#  输入：nums = [10,20,30], k = 1
# 输出：10
# 解释：size = [20,20,30].
# 我们可以让数组初始大小为 20 ，然后时刻 2 调整大小为 30 。
# 总浪费空间为 (20 - 10) + (20 - 20) + (30 - 30) = 10 。
#  
# 
#  示例 3： 
# 
#  输入：nums = [10,20,15,30,20], k = 2
# 输出：15
# 解释：size = [10,20,20,30,30].
# 我们可以让数组初始大小为 10 ，时刻 1 调整大小为 20 ，时刻 3 调整大小为 30 。
# 总浪费空间为 (10 - 10) + (20 - 20) + (20 - 15) + (30 - 30) + (30 - 20) = 15 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 200 
#  1 <= nums[i] <= 106 
#  0 <= k <= nums.length - 1 
#  
#  👍 9 👎 0
from typing import List
import functools
class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        """
        题目等价于：把数组完整分成k+1段连续的子数组，每一段权值是[这一段最大值乘以长度-这一段元素和]，最小化总权值
        f[i][j]表示将nums[0,..,i]分成j段的最小总权值。枚举最后一段推状态转移方程
        f[i][j] = min(f[x-1][j-1] + g[x][i]) 0 <= x <= i
        g[x][i]表示nums[x,...,i]这一段区间的权值
        最终答案为f[n-1][k+1]
        细节：
        当x=0时,f[-1][j-1]不是合法状态，考虑f[-1][...]表示的意义：
        对于一段空数组，希望将他分成若干段，由于每一段至少要有一个元素，那么空数组只能分成0段即f[-1][0]=0
        而不能分成任意正整数段，即f[-1][^0]=inf(因为求最小总权值，不合法的标记为极大值)
        然而本题有一个很好的性质当x1<x2时，分成x1段的最小总权值一定不会小于分成k2段的最小总权值，因此将所有的f[-1][...]都置为0也不会影响最终答案
        """
        n = len(nums)
        g = [[0] * n for _ in range(n)]
        for i in range(n):
            best, total = 0, 0
            for j in range(i, n):
                best = max(best, nums[j])
                total += nums[j]
                g[i][j] = best * (j - i + 1) - total
        f = [[float('inf')] * (k + 2) for _ in range(n)]

        for i in range(n):
            for j in range(1, k + 2):
                for x in range(i + 1):
                    f[i][j] = min(f[i][j], (0 if x == 0 else f[x - 1][j - 1]) + g[x][i])
        return f[n-1][k+1]


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        @functools.lru_cache(None)
        def dfs(start, left):
            if left == 1: return g[start][n-1]
            ans = float('inf')
            for i in range(start, n - left + 1):
                ans = min(ans, dfs(i + 1, left - 1) + g[start][i])
            return ans

        dfs.cache_clear()
        n = len(nums)
        g = [[0] * n for _ in range(n)]
        for i in range(n):
            best, total = 0, 0
            for j in range(i, n):
                best = max(best, nums[j])
                total += nums[j]
                g[i][j] = best * (j - i + 1) - total
        return dfs(0, k + 1)
# leetcode submit region end(Prohibit modification and deletion)
nums = [10,20,15,30,20]; k = 4
print(Solution().minSpaceWastedKResizing(nums, k))