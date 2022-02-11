# 给你一个下标从 0 开始的整数数组 nums ，它包含 3 * n 个元素。 
# 
#  你可以从 nums 中删除 恰好 n 个元素，剩下的 2 * n 个元素将会被分成两个 相同大小 的部分。 
# 
#  
#  前面 n 个元素属于第一部分，它们的和记为 sumfirst 。 
#  后面 n 个元素属于第二部分，它们的和记为 sumsecond 。 
#  
# 
#  两部分和的 差值 记为 sumfirst - sumsecond 。 
# 
#  
#  比方说，sumfirst = 3 且 sumsecond = 2 ，它们的差值为 1 。 
#  再比方，sumfirst = 2 且 sumsecond = 3 ，它们的差值为 -1 。 
#  
# 
#  请你返回删除 n 个元素之后，剩下两部分和的 差值的最小值 是多少。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [3,1,2]
# 输出：-1
# 解释：nums 有 3 个元素，所以 n = 1 。
# 所以我们需要从 nums 中删除 1 个元素，并将剩下的元素分成两部分。
# - 如果我们删除 nums[0] = 3 ，数组变为 [1,2] 。两部分和的差值为 1 - 2 = -1 。
# - 如果我们删除 nums[1] = 1 ，数组变为 [3,2] 。两部分和的差值为 3 - 2 = 1 。
# - 如果我们删除 nums[2] = 2 ，数组变为 [3,1] 。两部分和的差值为 3 - 1 = 2 。
# 两部分和的最小差值为 min(-1,1,2) = -1 。
#  
# 
#  示例 2： 
# 
#  输入：nums = [7,9,5,8,1,3]
# 输出：1
# 解释：n = 2 。所以我们需要删除 2 个元素，并将剩下元素分为 2 部分。
# 如果我们删除元素 nums[2] = 5 和 nums[3] = 8 ，剩下元素为 [7,9,1,3] 。和的差值为 (7+9) - (1+3) = 12 
# 。
# 为了得到最小差值，我们应该删除 nums[1] = 9 和 nums[4] = 1 ，剩下的元素为 [7,5,8,3] 。和的差值为 (7+5) - (8+
# 3) = 1 。
# 观察可知，最优答案为 1 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  nums.length == 3 * n 
#  1 <= n <= 10⁵ 
#  1 <= nums[i] <= 10⁵ 
#  
#  Related Topics 数组 动态规划 堆（优先队列） 👍 15 👎 0
from typing import List
import heapq

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        left, right = [0] * (n + 1), [0] * (n + 1) # left[i]表示左半段元素个数为n + i时的n个最小和，right[i]表示右半段元素个数为n + i时的最大和
        ql, qr, l, r = [], [], 0, 0
        for i in range(2 * n):
            heapq.heappush(ql, -nums[i])
            heapq.heappush(qr, nums[3 * n - 1 - i])
            l += nums[i]
            r += nums[3 * n - 1 - i]
            if len(ql) > n:
                l += heapq.heappop(ql)
            if len(qr) > n:
                r -= heapq.heappop(qr)
            if i >= n - 1:
                left[i - (n - 1)] = l
                right[i - (n - 1)] = r
        return min(left[i] - right[n - i] for i in range(n + 1))
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        min_pq = nums[2 * n:]
        heapq.heapify(min_pq)
        right_sum = [sum(min_pq)] + [0] * n # right[i]表示右半段元素个数为n + i时的最大和
        for i in range(1, n + 1):
            right_sum[i] = right_sum[i - 1] - heapq.heappushpop(min_pq, nums[2 * n - i]) + nums[2 * n - i]
        max_pq = [-nums[i] for i in range(n)]
        heapq.heapify(max_pq)
        pre_min = -sum(max_pq)
        ans = pre_min - right_sum[n]
        for i in range(n, 2 * n):
            pre_min += nums[i] + heapq.heappushpop(max_pq, -nums[i])
            ans = min(ans, pre_min - right_sum[2 * n - i - 1])
        return ans
# leetcode submit region end(Prohibit modification and deletion)
