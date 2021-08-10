# 如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。 
# 
#  
#  例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。 
#  
# 
#  
#  
#  给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。 
# 
#  子数组 是数组中的一个连续序列。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3,4]
# 输出：3
# 解释：nums 中有三个子等差数组：[1, 2, 3]、[2, 3, 4] 和 [1,2,3,4] 自身。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 5000 
#  -1000 <= nums[i] <= 1000 
#  
#  
#  
#  Related Topics 数组 动态规划 
#  👍 301 👎 0
from typing import List
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        长度为3的等差数列子数组有1个
        长度为4的等差数列子数组有2 + 1个
        长度为5的等差数列子数组有3 + 2 + 1个
        问题转化为找出nums等差数列及其对应长度
        """
        ans = 0
        n, i = len(nums), 0
        while i < n - 2:
            d = nums[i + 1] - nums[i]
            for j in range(i + 2, n + 1):
                if j == n or nums[j] - nums[j - 1] != d:
                    ans += (j - i - 1) * (j - i - 2) // 2
                    i = j - 1
                    break
        return ans
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        官解
        """
        n = len(nums)
        if n == 1: return 0
        d, t, ans = nums[0] - nums[1], 0, 0
        for i in range(2, n):
            if nums[i - 1] - nums[i] == d:
                t += 1
            else:
                d = nums[i - 1] - nums[i]
                t = 0
            ans += t
        return ans
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        dp[i]表示考虑nums[0,..,i]且以nums[i]结尾的等差数列子数组数量
        如果nums[i-2], nums[i-1], nums[i]等差，dp[i] = dp[i - 1] + 1
            因为nums[i]可以接在以nums[i-1]结尾的每一个子数组后面，还多了一个i-2,i-2,i的序列
        否则dp[i] = 0
        """
        dp = [0] * len(nums)
        for i in range(2, len(nums)):
            dp[i] = dp[i - 1] + 1 if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2] else 0
        return sum(dp)

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        因为只与上一状态相关，空间优化
        """
        t, ans = 0, 0
        for i in range(2, len(nums)):
            t = t + 1 if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2] else 0
            ans += t
        return ans


# leetcode submit region end(Prohibit modification and deletion)
nums = [1,2,3,4]
print(Solution().numberOfArithmeticSlices(nums))