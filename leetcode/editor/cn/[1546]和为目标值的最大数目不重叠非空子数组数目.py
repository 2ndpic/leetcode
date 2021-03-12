# 给你一个数组 nums 和一个整数 target 。 
# 
#  请你返回 非空不重叠 子数组的最大数目，且每个子数组中数字和都为 target 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [1,1,1,1,1], target = 2
# 输出：2
# 解释：总共有 2 个不重叠子数组（加粗数字表示） [1,1,1,1,1] ，它们的和为目标值 2 。
#  
# 
#  示例 2： 
# 
#  输入：nums = [-1,3,5,1,4,2,-9], target = 6
# 输出：2
# 解释：总共有 3 个子数组和为 6 。
# ([5,1], [4,2], [3,5,1,4,2,-9]) 但只有前 2 个是不重叠的。 
# 
#  示例 3： 
# 
#  输入：nums = [-2,6,6,3,5,4,1,2,8], target = 10
# 输出：3
#  
# 
#  示例 4： 
# 
#  输入：nums = [0,0,0], target = 0
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10^5 
#  -10^4 <= nums[i] <= 10^4 
#  0 <= target <= 10^6 
#  
#  Related Topics 动态规划 
#  👍 49 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        pre_sum, ans, s = 0, 0, {0}
        for i in nums:
            pre_sum += i
            if pre_sum - target in s:
                ans += 1
                pre_sum = 0
                s = {0}
            else:
                s.add(pre_sum)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
nums = [-2,6,6,3,5,4,1,2,8]
target = 10
# nums = [0,0,1]
# target = 1
print(Solution().maxNonOverlapping(nums, target))