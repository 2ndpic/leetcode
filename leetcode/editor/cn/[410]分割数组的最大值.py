# 给定一个非负整数数组 nums 和一个整数 m ，你需要将这个数组分成 m 个非空的连续子数组。 
# 
#  设计一个算法使得这 m 个子数组各自和的最大值最小。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [7,2,5,10,8], m = 2
# 输出：18
# 解释：
# 一共有四种方法将 nums 分割为 2 个子数组。 其中最好的方式是将其分为 [7,2,5] 和 [10,8] 。
# 因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3,4,5], m = 2
# 输出：9
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1,4,4], m = 3
# 输出：4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 1000 
#  0 <= nums[i] <= 106 
#  1 <= m <= min(50, nums.length) 
#  
#  Related Topics 二分查找 动态规划 
#  👍 433 👎 0

from typing import List
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        """
        题意是将nums分成m个子数组，找出最小的子数组和最大的值
        即将nums砍m-1刀，切成m段，找出最均匀的一种切割方式，返回最大值

        可知此值搜索范围是[max(nums), sum(nums)]
        用了一个前缀和优化一下
        """
        pre_sum, n = [0], len(nums)
        for i in range(n):
            pre_sum.append(pre_sum[-1] + nums[i])
        lo, hi = max(nums), pre_sum[-1]
        while lo < hi:
            mid = (lo + hi) // 2
            l, groups = 0, 1
            for r in range(n + 1):
                if pre_sum[r] - pre_sum[l] > mid:
                    groups += 1
                    l = r - 1
            if groups > m: lo = mid + 1
            else: hi = mid
        return lo

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        """
        题意是将nums分成m个子数组，找出最小的子数组和最大的值
        即将nums砍m-1刀，切成m段，找出最均匀的一种切割方式，返回最大值

        可知此值搜索范围是[max(nums), sum(nums)],
        """
        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            cur, cnt = 0, 1
            for i in nums:
                cur += i
                if cur > mid:
                    cnt += 1
                    cur = i
            if cnt > m: lo = mid + 1
            else: hi = mid
        return lo
# leetcode submit region end(Prohibit modification and deletion)

# nums = [7,2]
# m = 1
nums = [1,2,3,4,5]
m = 2
print(Solution().splitArray(nums, m))