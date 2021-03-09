# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。 
# 
#  子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序
# 列。 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 2500 
#  -104 <= nums[i] <= 104 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  你可以设计时间复杂度为 O(n2) 的解决方案吗？ 
#  你能将算法的时间复杂度降低到 O(n log(n)) 吗? 
#  
#  Related Topics 二分查找 动态规划 
#  👍 1429 👎 0
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        low = []
        for i in range(len(nums)):
            lo, hi = 0, len(low)
            while lo < hi:
                mid = (lo + hi) // 2
                if low[mid] < nums[i]: lo = mid + 1
                else: hi = mid
            if lo == len(low): low.append(nums[i])
            else: low[lo] = nums[i]
        return len(low)

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        如果用dp数组，dp[i] = max(dp[j] + 1, dp[i]) 0<=j<i, nums[j] < nums[i]
        每次都要去找到[0,..,i-1]区间的最大值，时间复杂度O(n^2)
        但是可以用数据结构优化，因为涉及到区间的更新和统计
        为了高效，我们可以利用树状数组，时间复杂度O(nlogn)
        """
        def update(i, value):
            i += 1
            while i <= len(nums):
                T[i] = max(T[i], value)
                i += i & (-i)

        def query(i):
            i += 1
            ans = 0
            while i:
                ans = max(ans, T[i])
                i -= i & (-i)
            return ans
        z = [(i, v) for i, v in enumerate(nums)]
        z.sort(key=lambda x: (x[1], x[0]))
        n = len(z)
        T = [0] * (n + 1)
        ans = 0
        for i in range(n):
            maxx = query(z[i][1]) + 1 # 查询编号小于等于nums[i]的LIS最大长度
            update(z[i][1], maxx)     # 把长度+1，再去更新前面的LIS长度
            ans = max(ans, maxx)
        return ans





# leetcode submit region end(Prohibit modification and deletion)
