# 给你一个整数数组 nums 。每一次操作中，你可以将 nums 中 任意 一个元素替换成 任意 整数。 
# 
#  如果 nums 满足以下条件，那么它是 连续的 ： 
# 
#  
#  nums 中所有元素都是 互不相同 的。 
#  nums 中 最大 元素与 最小 元素的差等于 nums.length - 1 。 
#  
# 
#  比方说，nums = [4, 2, 5, 3] 是 连续的 ，但是 nums = [1, 2, 3, 5, 6] 不是连续的 。 
# 
#  请你返回使 nums 连续 的 最少 操作次数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [4,2,5,3]
# 输出：0
# 解释：nums 已经是连续的了。
#  
# 
#  示例 2： 
# 
#  输入：nums = [1,2,3,5,6]
# 输出：1
# 解释：一个可能的解是将最后一个元素变为 4 。
# 结果数组为 [1,2,3,5,4] ，是连续数组。
#  
# 
#  示例 3： 
# 
#  输入：nums = [1,10,100,1000]
# 输出：3
# 解释：一个可能的解是：
# - 将第二个元素变为 2 。
# - 将第三个元素变为 3 。
# - 将第四个元素变为 4 。
# 结果数组为 [1,2,3,4] ，是连续数组。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  1 <= nums[i] <= 10⁹ 
#  
#  👍 4 👎 0
from typing import List
from collections import Counter
import bisect
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        pre_sum = [0]  # 前缀和统计重复元素个数
        for i, v in enumerate(nums):
            if i == 0: pre_sum.append(0)
            elif nums[i] == nums[i - 1]: pre_sum.append(pre_sum[-1] + 1)
            else: pre_sum.append(pre_sum[-1])
        ans = n - 1
        for i, v in enumerate(nums):
            right_end = v + n - 1
            right_end_index = bisect.bisect_left(nums, right_end)
            if right_end_index != n:
                # left_index到right_end_index之间重复的数，这些重复的数会增加操作数
                cur = pre_sum[right_end_index + 1] - pre_sum[i]
                # 检查有边界是否需要改变
                cur += 0 if nums[right_end_index] == right_end else 1
                # 添加其他的操作数
                cur += (n - (right_end_index - i + 1))
            else:
                cur = pre_sum[n] - pre_sum[i]
                cur += n - (n - 1 - i + 1)
            ans = min(ans, cur)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
nums = [8,10,16,18,10,10,16,13,13,16]
print(Solution().minOperations(nums))