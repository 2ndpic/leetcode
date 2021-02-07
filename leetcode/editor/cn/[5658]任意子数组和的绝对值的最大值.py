# 给你一个整数数组 nums 。一个子数组 [numsl, numsl+1, ..., numsr-1, numsr] 的 和的绝对值 为 abs(numsl
#  + numsl+1 + ... + numsr-1 + numsr) 。 
# 
#  请你找出 nums 中 和的绝对值 最大的任意子数组（可能为空），并返回该 最大值 。 
# 
#  abs(x) 定义如下： 
# 
#  
#  如果 x 是负整数，那么 abs(x) = -x 。 
#  如果 x 是非负整数，那么 abs(x) = x 。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,-3,2,3,-4]
# 输出：5
# 解释：子数组 [2,3] 和的绝对值最大，为 abs(2+3) = abs(5) = 5 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,-5,1,-4,3,-2]
# 输出：8
# 解释：子数组 [-5,1,-4] 和的绝对值最大，为 abs(-5+1-4) = abs(-8) = 8 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 105 
#  -104 <= nums[i] <= 104 
#  
#  Related Topics 贪心算法 
#  👍 2 👎 0
class S1:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        pre_sum = [0]
        for i in nums:
            pre_sum.append(pre_sum[-1] + i)
        return max(pre_sum) - min(pre_sum)

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_sum, max_sum, res =nums[0], nums[0], abs(nums[0])
        for i in nums[1:]:
            if min_sum < 0: min_sum += i
            else: min_sum = i
            if max_sum > 0: max_sum += i
            else: max_sum = i
            res = max(res, abs(max_sum), abs(min_sum))
        return res
# leetcode submit region end(Prohibit modification and deletion)
