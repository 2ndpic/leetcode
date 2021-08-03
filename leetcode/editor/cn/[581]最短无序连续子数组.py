# 给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。 
# 
#  请你找出符合题意的 最短 子数组，并输出它的长度。 
# 
#  
# 
#  
#  
#  示例 1： 
# 
#  
# 输入：nums = [2,6,4,8,10,9,15]
# 输出：5
# 解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3,4]
# 输出：0
#  
# 
#  示例 3： 
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
#  1 <= nums.length <= 104 
#  -105 <= nums[i] <= 105 
#  
# 
#  
# 
#  进阶：你可以设计一个时间复杂度为 O(n) 的解决方案吗？ 
#  
#  
#  Related Topics 栈 贪心 数组 双指针 排序 单调栈 
#  👍 621 👎 0
from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        start, end = 10 ** 5, -1
        for i, v in enumerate(nums):
            while stack and stack[-1][1] > v:
                start = min(start, stack.pop()[0])
            stack.append((i, v))
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while stack and stack[-1][1] < nums[i]:
                end = max(end, stack.pop()[0])
            stack.append((i, nums[i]))
        return max(end - start + 1, 0)

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_sorted, n = sorted(nums), len(nums)
        l, r = -1, -1
        for i in range(n):
            if l == -1 and nums[i] != nums_sorted[i]:
                l = i
            if r == -1 and nums[n - 1 - i] != nums_sorted[n - 1 - i]:
                r = n - 1 - i
        return r - l + 1 if l != -1 else 0
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n, maxn, r, minn, l = len(nums), float('-inf'), -1, float('inf'), -1
        for i in range(n):
            if nums[n - 1 - i] > minn:
                l = n - 1 - i
            else:
                minn = nums[n - 1 - i]
            if nums[i] < maxn:
                r = i
            else:
                maxn = nums[i]
        return r - l + 1 if r != -1 else 0
# leetcode submit region end(Prohibit modification and deletion)
