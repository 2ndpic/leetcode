# 元素的 频数 是该元素在一个数组中出现的次数。 
# 
#  给你一个整数数组 nums 和一个整数 k 。在一步操作中，你可以选择 nums 的一个下标，并将该下标对应元素的值增加 1 。 
# 
#  执行最多 k 次操作后，返回数组中最高频元素的 最大可能频数 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,4], k = 5
# 输出：3
# 解释：对第一个元素执行 3 次递增操作，对第二个元素执 2 次递增操作，此时 nums = [4,4,4] 。
# 4 是数组中最高频元素，频数是 3 。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,4,8,13], k = 5
# 输出：2
# 解释：存在多种最优解决方案：
# - 对第一个元素执行 3 次递增操作，此时 nums = [4,4,8,13] 。4 是数组中最高频元素，频数是 2 。
# - 对第二个元素执行 4 次递增操作，此时 nums = [1,8,8,13] 。8 是数组中最高频元素，频数是 2 。
# - 对第三个元素执行 5 次递增操作，此时 nums = [1,4,13,13] 。13 是数组中最高频元素，频数是 2 。
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [3,9,6], k = 2
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 105 
#  1 <= nums[i] <= 105 
#  1 <= k <= 105 
#  
#  Related Topics 数组 二分查找 前缀和 滑动窗口 
#  👍 104 👎 0

from typing import List
from itertools import accumulate
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_freq, n = 1, len(nums)
        pre_sum = [0]
        for i in nums:
            pre_sum.append(pre_sum[-1] + i)
        for i in range(1, n + 1):
            lo, hi = 1, i
            while lo < hi:
                mid = (lo + hi) // 2
                if mid * nums[i - 1] - (pre_sum[i] - pre_sum[i - mid]) < k: lo = mid + 1
                else: hi = mid
            if lo * nums[i - 1] - (pre_sum[i] - pre_sum[i - lo]) > k: lo -= 1
            max_freq = max(max_freq, lo)
        return max_freq
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
        另外一种的排序+二分
        """
        def check(t):
            for i in range(t, len(nums) + 1):
                if t * nums[i - 1] - (pre_sum[i] - pre_sum[i - t]) <= k: return True
            else: return False
        nums.sort()
        pre_sum = list(accumulate(nums, initial=0))
        lo, hi = 1, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid): lo = mid + 1
            else: hi = mid
        return lo if check(lo) else lo - 1
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
        滑动窗口
        """
        nums.sort()
        l, total, ans = 0, 0, 1
        for r in range(1, len(nums)):
            total += (nums[r] - nums[r - 1]) * (r - l)
            while total > k:
                total -= (nums[r] - nums[l])
                l += 1
            ans = max(ans, r - l + 1)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
nums = [8,8,8,1];k = 5
# nums = [1,2,4];k = 5
print(Solution().maxFrequency(nums, k))
