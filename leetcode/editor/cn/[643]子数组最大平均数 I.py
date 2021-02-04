# 给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。 
# 
#  
# 
#  示例： 
# 
#  
# 输入：[1,12,-5,-6,50,3], k = 4
# 输出：12.75
# 解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= n <= 30,000。 
#  所给数据范围 [-10,000，10,000]。 
#  
#  Related Topics 数组 
#  👍 140 👎 0

from typing import List


def s1(nums: List[int], k: int) -> float:
    l, r = 0, 0
    cur, res = 0, float('-inf')
    while r < len(nums):
        cur += nums[r]
        if r - l + 1 > k:
            cur -= nums[l]
            l += 1
        if r - l + 1 == k: res = max(res, cur)
        r += 1
    return res / k
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur = sum(nums[:k])
        res = cur
        for i in range(k, len(nums)):
            cur = cur - nums[i-k] + nums[i]
            res = max(res, cur)
        return res / k


        
# leetcode submit region end(Prohibit modification and deletion)
nums = [1,2]
k = 1
print(Solution().findMaxAverage(nums, k))