# 给定一个非空且只包含非负数的整数数组 nums，数组的度的定义是指数组里任一元素出现频数的最大值。 
# 
#  你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：[1, 2, 2, 3, 1]
# 输出：2
# 解释：
# 输入数组的度是2，因为元素1和2的出现频数最大，均为2.
# 连续子数组里面拥有相同度的有如下所示:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# 最短连续子数组[2, 2]的长度为2，所以返回2.
#  
# 
#  示例 2： 
# 
#  
# 输入：[1,2,2,3,1,4,2]
# 输出：6
#  
# 
#  
# 
#  提示： 
# 
#  
#  nums.length 在1到 50,000 区间范围内。 
#  nums[i] 是一个在 0 到 49,999 范围内的整数。 
#  
#  Related Topics 数组 
#  👍 225 👎 0

from typing import List
import collections
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d, degree, ans = {}, 0, len(nums)
        for index, value in enumerate(nums):
            d.setdefault(value, [0, index])
            d[value][0] += 1
            if d[value][0] > degree:
                ans = index - d[value][1] + 1
                degree = d[value][0]
            elif d[value][0] == degree:
                ans = min(ans, index - d[value][1] + 1)
        return ans

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        max_degree, ans, N = 0, 50009, 50009
        degree = [0] * N
        first = [N] * N
        for index, value in enumerate(nums):
            first[value] = min(first[value], index)
            degree[value] += 1
            if degree[value] > max_degree:
                ans = index - first[value] + 1
                max_degree = degree[value]
            elif degree[value] == max_degree:
                ans = min(ans, index - first[value] + 1)
        return ans

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d, degree, ans = {}, 0, len(nums)
        for index, value in enumerate(nums):
            d.setdefault(value, [0, index])
            d[value][0] += 1
            if d[value][0] > degree:
                ans = index - d[value][1] + 1
                degree = d[value][0]
            elif d[value][0] == degree:
                ans = min(ans, index - d[value][1] + 1)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
nums = [1,2,2,3,1]
print(Solution().findShortestSubArray(nums))
