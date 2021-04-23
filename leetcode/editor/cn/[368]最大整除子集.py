# 给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i], answer[
# j]) 都应当满足：
#  
#  answer[i] % answer[j] == 0 ，或 
#  answer[j] % answer[i] == 0 
#  
# 
#  如果存在多个有效解子集，返回其中任何一个均可。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[1,2]
# 解释：[1,3] 也会被视为正确答案。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,4,8]
# 输出：[1,2,4,8]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 1000 
#  1 <= nums[i] <= 2 * 109 
#  nums 中的所有整数 互不相同 
#  
#  Related Topics 数学 动态规划 
#  👍 275 👎 0

from typing import List
import bisect
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        最长上升子序列变形题 -> 最长倍数子序列
        dp[i]表示考虑数组前i个数且以nums[i-1]结尾的最长上升子序列
        dp[i] = max(dp[j]) + 1; j in [1,..,i-1] and nums[i - 1] % nums[j - 1] == 0
        """
        nums.sort()
        n = len(nums)
        dp = [1] * (n + 1)
        g = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(1, i):
                if nums[i - 1] % nums[j - 1] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        g[i] = j                    # 第i个数由第j个数转移过来
        ans = []
        idx = dp.index(max(dp))
        while len(ans) < max(dp):
            ans.append(nums[idx - 1])
            idx = g[idx]

        return ans[::-1]
# leetcode submit region end(Prohibit modification and deletion)
nums = [9,18,54,90,108,180,360,540,720]
# nums = [1,2,3]
# nums = [1,2,4,8]
# nums = [2, 3, 5, 7]
# nums = [3,4,16,8]
print(Solution().largestDivisibleSubset(nums))