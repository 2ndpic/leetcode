# 给你一个整数数组 nums ，请你返回所有下标对 0 <= i, j < nums.length 的 floor(nums[i] / nums[j]) 结果
# 之和。由于答案可能会很大，请你返回答案对109 + 7 取余 的结果。 
# 
#  函数 floor() 返回输入数字的整数部分。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [2,5,9]
# 输出：10
# 解释：
# floor(2 / 5) = floor(2 / 9) = floor(5 / 9) = 0
# floor(2 / 2) = floor(5 / 5) = floor(9 / 9) = 1
# floor(5 / 2) = 2
# floor(9 / 2) = 4
# floor(9 / 5) = 1
# 我们计算每一个数对商向下取整的结果并求和得到 10 。
#  
# 
#  示例 2： 
# 
#  输入：nums = [7,7,7,7,7,7,7]
# 输出：49
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 105 
#  1 <= nums[i] <= 105 
#  
#  Related Topics 数学 
#  👍 9 👎 0

from typing import List
import collections
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        """
        时间复杂度：O(n + ClogC) 其中C是数组nums最大值
        """
        mod = 10 ** 9 + 7
        lower, upper = min(nums), max(nums)
        cnt = [0] * (upper + 1)
        for i in nums:
            cnt[i] += 1
        pre_sum = [0] * (upper + 1) # 统计频次的前缀和, pre_sum[i] = sum(cnt[1], ..,cnt[i])
        for i in range(1, upper + 1):
            pre_sum[i] = pre_sum[i - 1] + cnt[i]
        ans = 0
        for y in range(lower, upper + 1):
            if cnt[y] == 0: continue
            for d in range(1, upper // y + 1):
                ans += (pre_sum[min((d + 1) * y - 1, upper)] - pre_sum[y * d - 1]) * d * cnt[y]
        return ans % mod
# leetcode submit region end(Prohibit modification and deletion)
nums = [2,5,9]
# nums = [7,7,7,7,7,7,7]
print(Solution().sumOfFlooredPairs(nums))