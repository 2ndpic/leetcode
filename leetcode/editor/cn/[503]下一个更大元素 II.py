# 给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第
# 一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。 
# 
#  示例 1: 
# 
#  
# 输入: [1,2,1]
# 输出: [2,-1,2]
# 解释: 第一个 1 的下一个更大的数是 2；
# 数字 2 找不到下一个更大的数； 
# 第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
#  
# 
#  注意: 输入数组的长度不会超过 10000。 
#  Related Topics 栈 
#  👍 391 👎 0

from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []
        for idx, v in enumerate(nums + nums):
            while stack and v > stack[-1][1]:
                ans[stack.pop()[0]] = v
            stack.append((idx%n, v))
        return ans
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        上面写法的程序，信息其实是冗余的，因为可以通过下标求出对应的元素值
        所有我们的stack可以只存元素的下标值
        """
        n = len(nums)
        ans = [-1] * n
        stack = []
        for idx in range(2 * n):
            v = nums[idx%n]
            while stack and v > nums[stack[-1]]:
                ans[stack.pop()] = v
            stack.append(idx%n)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
nums = [1, 2, 3]
print(Solution().nextGreaterElements(nums))