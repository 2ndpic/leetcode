# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。 
# 
#  解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0]
# 输出：[[],[0]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10 
#  -10 <= nums[i] <= 10 
#  nums 中的所有元素 互不相同 
#  
#  Related Topics 位运算 数组 回溯算法 
#  👍 1012 👎 0

from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            for j in range(len(res)):
                res.append(res[j] + [i])
        return res
# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(start, l):
            res.append(l)
            for i in range(start, len(nums)):
                helper(i + 1, l + [nums[i]])

        res = []
        helper(0, [])
        return res
# leetcode submit region end(Prohibit modification and deletion)
nums = []
print(Solution().subsets(nums))