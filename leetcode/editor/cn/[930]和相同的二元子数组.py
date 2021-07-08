# 给你一个二元数组 nums ，和一个整数 goal ，请你统计并返回有多少个和为 goal 的 非空 子数组。 
# 
#  子数组 是数组的一段连续部分。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,0,1,0,1], goal = 2
# 输出：4
# 解释：
# 如下面黑体所示，有 4 个满足题目要求的子数组：
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,0,0,0,0], goal = 0
# 输出：15
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 3 * 104 
#  nums[i] 不是 0 就是 1 
#  0 <= goal <= nums.length 
#  
#  Related Topics 数组 哈希表 前缀和 滑动窗口 
#  👍 105 👎 0

from typing import List
import collections
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cnt = collections.defaultdict(int)
        pre_sum = 0
        ans = 0
        for i in nums:
            cnt[pre_sum] += 1
            pre_sum += i
            ans += cnt[pre_sum - goal]
        return ans
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        双指针
        因为没有负值，确定右边界，若右边界移动那么左边界也必右移，所以可以使用双指针
        确定右边界r,l1, l2，nums[l] + ..+nums[r]=goal (l1 <= l < l2)
        所以对于r,答案有l2-l1个
        """
        l1, l2, pre1, pre2, ans = [0] * 5
        for r in range(len(nums)):
            pre1, pre2 = pre1 + nums[r], pre2 + nums[r]
            while l1 <= r and pre1 > goal:
                pre1 -= nums[l1]
                l1 += 1
            while l2 <= r and pre2 >= goal:
                pre2 -= nums[l2]
                l2 += 1
            ans += (l2 - l1)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
nums = [15]; goal = 15
nums = [0,0,0,0,0]; goal = 0
print(Solution().numSubarraysWithSum(nums, goal))