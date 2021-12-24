# 给你一个字符串 s ，请你返回满足以下条件且出现次数最大的 任意 子串的出现次数： 
# 
#  
#  子串中不同字母的数目必须小于等于 maxLetters 。 
#  子串的长度必须大于等于 minSize 且小于等于 maxSize 。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
# 输出：2
# 解释：子串 "aab" 在原字符串中出现了 2 次。
# 它满足所有的要求：2 个不同的字母，长度为 3 （在 minSize 和 maxSize 范围内）。
#  
# 
#  示例 2： 
# 
#  输入：s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
# 输出：2
# 解释：子串 "aaa" 在原字符串中出现了 2 次，且它们有重叠部分。
#  
# 
#  示例 3： 
# 
#  输入：s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
# 输出：3
#  
# 
#  示例 4： 
# 
#  输入：s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10^5 
#  1 <= maxLetters <= 26 
#  1 <= minSize <= maxSize <= min(26, s.length) 
#  s 只包含小写英文字母。 
#  
#  Related Topics 哈希表 字符串 滑动窗口 👍 62 👎 0
from collections import defaultdict
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n, mod, ans = len(s), 10 ** 9 + 7, 0
        for size in range(minSize, maxSize + 1):
            seen, ch_dict = defaultdict(int), defaultdict(int)
            curr, aL = 0, pow(26, size, mod)
            for i in range(n):
                curr = (curr * 26 + ord(s[i]) - ord('a')) % mod
                ch_dict[s[i]] += 1
                if i >= size:
                    curr = (curr - aL * (ord(s[i - size]) - ord('a'))) % mod
                    ch_dict[s[i - size]] -= 1
                    if ch_dict[s[i - size]] == 0: ch_dict.pop(s[i - size])
                if i >= size - 1:
                    seen[curr] += 1
                    if len(ch_dict) <= maxLetters:
                        ans = max(ans, seen[curr])
        return ans

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        """
        逐个遍历取一次,计算一次.
        只要考虑最短的就好咯,长的肯定会覆盖短的.
        """
        n, d = len(s), {}
        for i in range(n - minSize + 1):
            cur = s[i:i + minSize]
            if len(set(cur)) <= maxLetters: d[cur] = d.get(cur, 0) + 1
        return max(d.values()) if d else 0  # 如果没有满足的,直接返回最大值(不存在的集)会报错,要返回0.

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        """
        其实完全用不到maxSize窗口，因为maxsize窗口字串出现个数一定包含minsize窗口子串
        """
        n, mod, ans, size = len(s), 10 ** 9 + 7, 0, minSize
        seen, ch_dict = defaultdict(int), defaultdict(int)
        curr, aL = 0, pow(26, minSize, mod)
        arr = [ord(i) - ord('a') for i in s]
        for i in range(n):
            curr = (curr * 26 + arr[i]) % mod
            ch_dict[arr[i]] += 1
            if i >= size:
                curr = (curr - aL * arr[i - size]) % mod
                ch_dict[arr[i - size]] -= 1
                if ch_dict[arr[i - size]] == 0: ch_dict.pop(arr[i - size])
            if i >= size - 1:
                seen[curr] += 1
                if len(ch_dict) <= maxLetters:
                    ans = max(ans, seen[curr])
        return ans
# leetcode submit region end(Prohibit modification and deletion)
s = "aababcaab"
maxLetters = 2
minSize = 3
maxSize = 4

print(Solution().maxFreq(s, maxLetters, minSize, maxSize))