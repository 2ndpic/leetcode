# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。 
# 
#  解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。 
# 
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
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
#  
#  
#  
#  Related Topics 数组 回溯算法 
#  👍 446 👎 0

from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(start, path):
            if start == len(nums):
                ans.append(path)
                return
            for i in range(start, len(nums)):
                if path + [nums[i]] not in ans:
                    helper(start + 1, path + [nums[i]])
                if path not in ans:
                    helper(start + 1, path)

        ans = []
        nums.sort()
        helper(0, [])
        return ans

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtracking(start, path):
            ans.append(path)
            for i in range(start, len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == 0:
                    continue
                used[i] = 1
                backtracking(i + 1, path + [nums[i]])
                used[i] = 0

        nums.sort()
        ans = []
        used = [0] * len(nums)
        backtracking(0, [])
        return ans
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtracking(start, path):
            ans.append(path)
            used = set()
            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue
                used.add(nums[i])
                backtracking(i + 1, path + [nums[i]])

        nums.sort()
        ans = []
        backtracking(0, [])
        return ans
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(start, path):
            ans.append(path)
            for i in range(start, len(nums)):
                if i != start and nums[i] == nums[i - 1]:
                    continue
                helper(i + 1, path + [nums[i]])
        nums.sort()
        ans = []
        helper(0, [])
        return ans
# leetcode submit region end(Prohibit modification and deletion)
nums = [1,2,2]
# nums = [0]
print(Solution().subsetsWithDup(nums))