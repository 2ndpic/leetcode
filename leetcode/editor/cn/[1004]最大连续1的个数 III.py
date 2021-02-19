# 给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。 
# 
#  返回仅包含 1 的最长（连续）子数组的长度。 
# 
#  
# 
#  示例 1： 
# 
#  输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# 输出：6
# 解释： 
# [1,1,1,0,0,1,1,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 6。 
# 
#  示例 2： 
# 
#  输入：A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# 输出：10
# 解释：
# [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 10。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 20000 
#  0 <= K <= A.length 
#  A[i] 为 0 或 1 
#  
#  Related Topics 双指针 Sliding Window 
#  👍 163 👎 0

from typing import List
import bisect
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        l, r, cur, res = 0, 0, 0, 0
        while r < len(A):
            if A[r] == 0:
                cur += 1
            while cur > K:
                if A[l] == 0:
                    cur -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        l, cur, res = 0, 0, 0
        for r in range(len(A)):
            cur += A[r] ^ 1
            if cur > K:
                cur -= A[l] ^ 1
                l += 1
            res = max(res, r - l + 1)
        return res
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        """
        p作为前缀和数组，p[k]表示A数组中前k个数里面0的个数，显然p是个递增数组
        我们只用遍历所有合法右边界，找到最远的左边界，使得p[right] - p[left] <= K, 即p[right] - p[left - 1] > k
        """
        p = [0]
        for i in A:
            p.append(p[-1] + (i ^ 1))
        ans = 0
        for i in range(len(p)):
            lo, hi = 0, i
            while lo < hi:
                mid = (lo + hi) // 2
                if p[i] - p[mid] > K: lo = mid + 1
                else: hi = mid
            ans = max(ans, i - lo)
        return ans
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        p, ans = [0], 0
        for i in A:
            p.append(p[-1] + (i ^ 1))
        for i in range(len(p)):
            ans = max(ans, i - bisect.bisect_left(p, p[i] - K))
            # p[8]=5代表A前8个元素0的个数为5,k=2, 找到p中>=3的下界，p[5] = 3,则找到p[5]即5这个位置。10010 10010001 p = [0,0,1,2,2,3,4,5,5]
        return ans
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        p, ans = [0], 0
        for i in A:
            p.append(p[-1] + (i ^ 1))
        for i in range(len(p)):
            ans = max(ans, i - bisect.bisect_left(p, p[i] - K))
            # p[8]=5代表A前8个元素0的个数为5,k=2, 找到p中>=3的下界，p[5] = 3,则找到p[5]即5这个位置。10010 10010001 p = [0,0,1,2,2,3,4,5,5]
        return ans
# leetcode submit region end(Prohibit modification and deletion)
A = [1,1,1,0,0,0,1,1,1,1,1]
K = 3
A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
K = 3
A = [1,0,0,1,0,0,0,1]
K = 2
print(Solution().longestOnes(A, K))