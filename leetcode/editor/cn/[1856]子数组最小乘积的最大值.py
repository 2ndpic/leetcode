# 一个数组的 最小乘积 定义为这个数组中 最小值 乘以 数组的 和 。 
# 
#  
#  比方说，数组 [3,2,5] （最小值是 2）的最小乘积为 2 * (3+2+5) = 2 * 10 = 20 。 
#  
# 
#  给你一个正整数数组 nums ，请你返回 nums 任意 非空子数组 的最小乘积 的 最大值 。由于答案可能很大，请你返回答案对 109 + 7 取余 的
# 结果。 
# 
#  请注意，最小乘积的最大值考虑的是取余操作 之前 的结果。题目保证最小乘积的最大值在 不取余 的情况下可以用 64 位有符号整数 保存。 
# 
#  子数组 定义为一个数组的 连续 部分。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3,2]
# 输出：14
# 解释：最小乘积的最大值由子数组 [2,3,2] （最小值是 2）得到。
# 2 * (2+3+2) = 2 * 7 = 14 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,3,3,1,2]
# 输出：18
# 解释：最小乘积的最大值由子数组 [3,3] （最小值是 3）得到。
# 3 * (3+3) = 3 * 6 = 18 。
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [3,1,5,6,4,2]
# 输出：60
# 解释：最小乘积的最大值由子数组 [5,6,4] （最小值是 4）得到。
# 4 * (5+6+4) = 4 * 15 = 60 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 105 
#  1 <= nums[i] <= 107 
#  
#  Related Topics 排序 并查集 队列 二分查找 动态规划 
#  👍 32 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        """
        遍历nums，以nums[i]作为某个子数组的最小值，子数组范围（开区间）为左右第一个小于nums[i]的位置。
        遍历过程中维护最小乘积最大值
        问题转化为：如何在一个无序数组中，找到第一个小于某个值的位置 -> 单调栈

        时间复杂度O(n)
        """
        mod, n = 10 ** 9 + 7, len(nums)
        stack = []
        right_index = [0] * (n + 1) # 开区间
        left_index = [0] * (n + 1) # 闭区间
        pre_sum = [0]
        for i in nums:
            pre_sum.append(pre_sum[-1] + i)
        # 找每个数右边第一个比他小的位置
        for i, v in enumerate(nums + [-1]):
            while stack and v < stack[-1][1]:
                idx, val = stack.pop()
                right_index[idx] = i
            stack.append((i, v))
        # 找每个数左边第一个比他小的位置
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] < stack[-1][1]:
                idx, val = stack.pop()
                left_index[idx] = i + 1
            stack.append((i, nums[i]))

        ans = 0
        for i in range(len(nums)):
            ans = max(ans, nums[i] * (pre_sum[right_index[i]] - pre_sum[left_index[i]]))
        return ans % mod

# leetcode submit region end(Prohibit modification and deletion)
nums = [1,2,3,2]
# nums = [2,3,3,1,2]
nums = [3,1,5,6,4,2]
print(Solution().maxSumMinProduct(nums))