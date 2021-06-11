# 给定一个非负整数数组，你最初位于数组的第一个位置。 
# 
#  数组中的每个元素代表你在该位置可以跳跃的最大长度。 
# 
#  你的目标是使用最少的跳跃次数到达数组的最后一个位置。 
# 
#  假设你总是可以到达数组的最后一个位置。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
#  
# 
#  示例 2: 
# 
#  
# 输入: [2,3,0,1,4]
# 输出: 2
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= nums.length <= 1000 
#  0 <= nums[i] <= 105 
#  
#  Related Topics 贪心算法 数组 
#  👍 1013 👎 0

from typing import List
import collections
import functools
class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        f[i]表示从i位置跳到最后一个位置的最少跳跃次数,最终答案f[0]，初始化f[n-1]=0
        f[i] = min(f[i + 1], f[i + 2], ...,f[i + nums[i]]) + 1
        """
        n = len(nums)
        f = [float('inf')] * (n - 1) + [0]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, min(n, i + nums[i] + 1)):
                f[i] = min(f[i], f[j] + 1)
        return f[0]

class Solution:
    def jump(self, nums: List[int]) -> int:
        @functools.lru_cache(None)
        def dfs(s):
            if s == len(nums) - 1: return 0
            ans = len(nums)
            for i in range(1, nums[s] + 1):
                if s + i >= len(nums): break
                ans = min(ans, dfs(s + i) + 1)
            return ans
        return dfs(0)
class Solution:
    def jump(self, nums: List[int]) -> int:
        q = set([0])
        ans = 0
        while q:
            q_tmp = set()
            for idx in q:
                if idx == len(nums) - 1: return ans
                for j in range(1, nums[idx] + 1):
                    if idx + j >= len(nums): break
                    if (idx + j) not in q: q_tmp.add(idx + j)
            q = q_tmp.copy()
            ans += 1
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        双指针+贪心+动态规划
        f[i]表示到达第i个点时的最少步数
        f[i] = min(f[i-1], f[i-2], ..., f[i-k]) + 1
        必然有 f[i - 1]<= f[i] <= f[i + 1] <= f[i + 2],可用反证法证明
            - 假设存在f[i] > f[i+1], 则f[i]是由之前的最小值c转移过来的。f[i] = c + 1。f[i+1]由f[i]和c转移，则f[i] <= f[i+1],与假设矛盾
        贪心策略：计算f[i]时，找到能到达i的最远的j位置（j最小）f[i] = f[j] + 1。策略正确性可由反证法证明。
            - 假设存在k位置（k>j）,f[i]那么由f[k]转移过来，那么f[k] > f[j]，根据上个证明f[j] <= f[k]（j < k）矛盾，故不存在k位置
        找j的过程可用双指针来找
        """
        n = len(nums)
        f = [0] * n
        l = 0
        for r in range(1, n):
            while l + nums[l] < r:
                l += 1
            f[r] = f[l] + 1
        return f[n-1]
# leetcode submit region end(Prohibit modification and deletion)
nums = [2,3,1,1,4]
nums = [2,3,0,1,4]
nums = [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]
nums = [5]
print(Solution().jump(nums))