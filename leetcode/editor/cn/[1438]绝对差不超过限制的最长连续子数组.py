# 给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 limi
# t 。 
# 
#  如果不存在满足条件的子数组，则返回 0 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [8,2,4,7], limit = 4
# 输出：2 
# 解释：所有子数组如下：
# [8] 最大绝对差 |8-8| = 0 <= 4.
# [8,2] 最大绝对差 |8-2| = 6 > 4. 
# [8,2,4] 最大绝对差 |8-2| = 6 > 4.
# [8,2,4,7] 最大绝对差 |8-2| = 6 > 4.
# [2] 最大绝对差 |2-2| = 0 <= 4.
# [2,4] 最大绝对差 |2-4| = 2 <= 4.
# [2,4,7] 最大绝对差 |2-7| = 5 > 4.
# [4] 最大绝对差 |4-4| = 0 <= 4.
# [4,7] 最大绝对差 |4-7| = 3 <= 4.
# [7] 最大绝对差 |7-7| = 0 <= 4. 
# 因此，满足题意的最长子数组的长度为 2 。
#  
# 
#  示例 2： 
# 
#  输入：nums = [10,1,2,4,7,2], limit = 5
# 输出：4 
# 解释：满足题意的最长子数组是 [2,4,7,2]，其最大绝对差 |2-7| = 5 <= 5 。
#  
# 
#  示例 3： 
# 
#  输入：nums = [4,2,2,2,4,4,2,2], limit = 0
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10^5 
#  1 <= nums[i] <= 10^9 
#  0 <= limit <= 10^9 
#  
#  Related Topics 数组 Sliding Window 
#  👍 153 👎 0
import collections
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l, r = 0, 0
        max_q = []
        min_q = []
        res = 0
        min_item = collections.defaultdict(int)
        max_item = collections.defaultdict(int)
        while r < len(nums):
            heapq.heappush(max_q, -nums[r])
            heapq.heappush(min_q, nums[r])
            while -max_q[0] - min_q[0] > limit:
                min_item[nums[l]] += 1
                max_item[nums[l]] += 1
                while max_item[-max_q[0]]:
                    max_item[-max_q[0]] -= 1
                    heapq.heappop(max_q)
                while min_item[min_q[0]]:
                    min_item[min_q[0]] -= 1
                    heapq.heappop(min_q)
                l += 1

            res = max(res, r - l + 1)
            r += 1
        return res

# leetcode submit region begin(Prohibit modification and deletion)
from heapq import heappop, heappush
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_ = []
        min_ = []
        res = 0
        l = 0
        for r, num in enumerate(nums):
            heappush(max_, [-num, r])
            heappush(min_, [num, r])
            # l 为左指针位置
            while -max_[0][0] - min_[0][0] > limit:
                # 条件判断需要max,min[0][0]存的索引不在 l 左侧
                # 删除不在 l 右侧的元素
                while min_[0][1] <= l:
                    heappop(min_)
                while max_[0][1] <= l:
                    heappop(max_)
                # 移动 l
                l += 1
            # 找到最长的符合要求的窗口长度
            res = max(res, r - l + 1)
        return res

# leetcode submit region end(Prohibit modification and deletion)
