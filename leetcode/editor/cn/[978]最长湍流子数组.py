# 当 A 的子数组 A[i], A[i+1], ..., A[j] 满足下列条件时，我们称其为湍流子数组： 
# 
#  
#  若 i <= k < j，当 k 为奇数时， A[k] > A[k+1]，且当 k 为偶数时，A[k] < A[k+1]； 
#  或 若 i <= k < j，当 k 为偶数时，A[k] > A[k+1] ，且当 k 为奇数时， A[k] < A[k+1]。 
#  
# 
#  也就是说，如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组。 
# 
#  返回 A 的最大湍流子数组的长度。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[9,4,2,10,7,8,8,1,9]
# 输出：5
# 解释：(A[1] > A[2] < A[3] > A[4] < A[5])
#  
# 
#  示例 2： 
# 
#  输入：[4,8,12,16]
# 输出：2
#  
# 
#  示例 3： 
# 
#  输入：[100]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 40000 
#  0 <= A[i] <= 10^9 
#  
#  Related Topics 数组 动态规划 Sliding Window 
#  👍 91 👎 0

from typing import List
class WoLiu:
    def __init__(self):
        self.l, self.r, self.state = None, None, None
        self.length = 0
        self.res = -1
    def add(self, num):
        if self.l is None:
            self.l = num
        elif self.r is None:
            self.r = num
        else:
            self.l, self.r = self.r, num
        self.check()
        self.res = max(self.res, self.length)
    def check(self):
        if self.r is None:
            self.length = 1
        elif self.l == self.r:
            self.r = None
            self.state = None
            self.length = 1
        elif self.l < self.r:
            if self.state in [-1, None]: self.length = 2
            else: self.length += 1
            self.state = -1
        else:
            if self.state in [1, None]: self.length = 2
            else: self.length += 1
            self.state = 1

class S1:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        woliu = WoLiu()
        for i in arr:
            woliu.add(i)
        return woliu.res
def maxTurbulenceSize(self, arr: List[int]) -> int:
    """
    dp[i][0]表示以第i个元素结尾且i位于于下降状态的最长连续子数组长度
    dp[i][1]表示以第i个元素结尾且i位于上升状态的最长连续子数组长度

    dp[i][0] = dp[i-1][1] + 1 if arr[i-1] > arr[i] else 1
    dp[i][1] = dp[i-1][0] + 1 if arr[i-1] < arr[i] else 1
    初始化：dp[0][0] = 1, dp[0][1] = 1

    又因为每次只用到dp[i-1]的信息，所以可以优化空间
    """
    dp = [[1, 1] for i in range(len(arr))]
    res = 1
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            dp[i][0] = dp[i-1][1] + 1
        elif arr[i-1] < arr[i]:
            dp[i][1] = dp[i-1][0] + 1
        res = max(dp[i][0], dp[i][1], res)
    return res
class S2:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """
        dp[i][0]表示以第i个元素结尾且i位于于下降状态的最长连续子数组长度
        dp[i][1]表示以第i个元素结尾且i位于上升状态的最长连续子数组长度

        dp[i][0] = dp[i-1][1] + 1 if arr[i-1] > arr[i] else 1
        dp[i][1] = dp[i-1][0] + 1 if arr[i-1] < arr[i] else 1
        初始化：dp[0][0] = 1, dp[0][1] = 1

        又因为每次只用到dp[i-1]的信息，所以可以优化空间
        """
        dp = [[1, 1] for i in range(len(arr))]
        res = 1
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                dp[i][0] = dp[i-1][1] + 1
            elif arr[i-1] < arr[i]:
                dp[i][1] = dp[i-1][0] + 1
            res = max(dp[i][0], dp[i][1], res)
        return res
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """
        dp[i][0]表示以第i个元素结尾且i位于于下降状态的最长连续子数组长度
        dp[i][1]表示以第i个元素结尾且i位于上升状态的最长连续子数组长度

        dp[i][0] = dp[i-1][1] + 1 if arr[i-1] > arr[i] else 1
        dp[i][1] = dp[i-1][0] + 1 if arr[i-1] < arr[i] else 1
        初始化：dp[0][0] = 1, dp[0][1] = 1

        又因为每次只用到dp[i-1]的信息，所以可以优化空间
        """
        down, up = 1, 1 # 以此元素结尾的且为谷/峰的最长连续子数组长度
        res = 1
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                down = up + 1
                up = 1
            elif arr[i-1] < arr[i]:
                up = down + 1
                down = 1
            else:
                down, up = 1, 1
            res = max(res, down, up)
        return res

# leetcode submit region end(Prohibit modification and deletion)
arr = [9,4,2,10,7,8,8,1,9]
# arr = [4,8,12,16]
print(Solution().maxTurbulenceSize(arr)) # 7