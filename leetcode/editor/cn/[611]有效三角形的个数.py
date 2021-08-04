# 给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。 
# 
#  示例 1: 
# 
#  
# 输入: [2,2,3,4]
# 输出: 3
# 解释:
# 有效的组合是: 
# 2,3,4 (使用第一个 2)
# 2,3,4 (使用第二个 2)
# 2,2,3
#  
# 
#  注意: 
# 
#  
#  数组长度不超过1000。 
#  数组里整数的范围为 [0, 1000]。 
#  
#  Related Topics 贪心 数组 双指针 二分查找 排序 
#  👍 267 👎 0

from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n, ans = len(nums), 0
        for i in range(2, n):
            c = nums[i]
            for j in range(i):
                a = nums[j]
                lo, hi = j + 1, i
                while lo < hi:
                    mid = (lo + hi) // 2
                    if nums[mid] > c - a: hi = mid
                    else: lo = mid + 1
                ans += (i - lo)
        return ans
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n):
            k = i
            for j in range(i + 1, n):
                while k + 1 < n and nums[k + 1] < nums[i] + nums[j]:
                    k += 1
                ans += max(0, k - j)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
nums = [2,2,3,4]
print(Solution().triangleNumber(nums))