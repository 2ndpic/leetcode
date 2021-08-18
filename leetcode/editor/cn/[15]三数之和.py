# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重
# 复的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [0]
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 3000 
#  -105 <= nums[i] <= 105 
#  
#  Related Topics 数组 双指针 排序 
#  👍 3646 👎 0
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n):
            if nums[i] > 0: break
            if i != 0 and nums[i] == nums[i - 1]: continue
            r, target = n - 1, -nums[i]
            for l in range(i + 1, n):
                if l > i + 1 and nums[l] == nums[l - 1]:
                    continue
                while l < r and nums[l] + nums[r] > target:
                    r -= 1
                if l == r: break
                if nums[l] + nums[r] == target: ans.append([nums[i], nums[l], nums[r]])
        return ans

# leetcode submit region end(Prohibit modification and deletion)
nums = [-1,0,1,2,-1,-4]
nums = [0,0,0,0]
print(Solution().threeSum(nums))