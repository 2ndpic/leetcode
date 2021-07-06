# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。 
# 
#  
# 
#  示例： 
# 
#  输入：
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# 输出：3
# 解释：
# 长度最长的公共子数组是 [3, 2, 1] 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= len(A), len(B) <= 1000 
#  0 <= A[i], B[i] < 100 
#  
#  Related Topics 数组 二分查找 动态规划 滑动窗口 哈希函数 滚动哈希 
#  👍 481 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
        dp[i][j]表示考虑nums1[i:]和nums2[j:]的最长重复子数组
        dp[i][j] = 1 + dp[i+1][j+1] if nums1[i] == nums2[j] else 0
        """
        m, n = len(nums1), len(nums2)
        dp = [[0] * n for _ in range(m)]
        ans = 0
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 or j == n - 1:
                    dp[i][j] = 1 if nums1[i] == nums2[j] else 0
                else:
                    dp[i][j] = 1 + dp[i + 1][j + 1] if nums1[i] == nums2[j] else 0
                ans = max(ans, dp[i][j])
        return ans
# leetcode submit region end(Prohibit modification and deletion)
