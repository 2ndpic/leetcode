# 给你一个字符串 s ，考虑其所有 重复子串 ：即，s 的连续子串，在 s 中出现 2 次或更多次。这些出现之间可能存在重叠。 
# 
#  返回 任意一个 可能具有最长长度的重复子串。如果 s 不含重复子串，那么答案为 "" 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "banana"
# 输出："ana"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "abcd"
# 输出：""
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= s.length <= 3 * 10⁴ 
#  s 由小写英文字母组成 
#  
#  Related Topics 字符串 二分查找 后缀数组 滑动窗口 哈希函数 滚动哈希 👍 251 👎 0
import random

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        # 生成两个进制和摸来避免hash碰撞
        a1, a2 = random.randint(26, 100), random.randint(26, 100)
        mod1, mod2 = random.randint(10 ** 9 + 7, 2 ** 31 - 1), random.randint(10 ** 9 + 7, 2 ** 31 - 1)
        # 对每个字符进行编码
        arr = [ord(i) - ord('a') for i in s]
        # 二分搜索
        start, length = -1, 0
        lo, hi = 1, len(s)  # 最长重复子串的长度[1...n-1]，左闭右开搜索
        while lo < hi:
            mid = (lo + hi) // 2
            idx = self.check(arr, mid, a1, a2, mod1, mod2)
            if idx != -1:
                start = idx
                length = mid
                lo = mid + 1
            else: hi = mid
        return s[start:start + length] if start != -1 else ""

    def check(self, arr, m, a1, a2, mod1, mod2):
        aL1, aL2 = pow(a1, m, mod1), pow(a2, m, mod2)
        h1, h2 = 0, 0
        for i in range(m):
            h1 = ((h1 * a1) + arr[i]) % mod1
            h2 = ((h2 * a2) + arr[i]) % mod2
        seen = {(h1, h2)}
        for start in range(1, len(arr) - m + 1):
            h1 = (h1 * a1 - arr[start - 1] * aL1 + arr[start + m - 1]) % mod1
            h2 = (h2 * a2 - arr[start - 1] * aL2 + arr[start + m - 1]) % mod2
            if (h1, h2) in seen:
                return start
            seen.add((h1, h2))
        return -1
# leetcode submit region end(Prohibit modification and deletion)
