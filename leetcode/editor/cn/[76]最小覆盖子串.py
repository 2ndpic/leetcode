# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。 
# 
#  
# 
#  注意： 
# 
#  
#  对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。 
#  如果 s 中存在这样的子串，我们保证它是唯一的答案。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a", t = "a"
# 输出："a"
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length, t.length <= 10⁵ 
#  s 和 t 由英文字母组成 
#  
# 
#  
# 进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？ Related Topics 哈希表 字符串 滑动窗口 👍 1592 👎 0
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ori = defaultdict(int)
        cnt = defaultdict(int)
        for ch in t:
            ori[ch] += 1
        l, length, ansL = 0, float('inf'), -1
        for r in range(len(s)):
            cnt[s[r]] += 1
            while all(cnt[k] >= v for k, v in ori.items()):
                if r - l + 1 < length:
                    length = r - l + 1
                    ansL = l
                cnt[s[l]] -= 1
                l += 1
        return s[ansL: ansL + length] if ansL != -1 else ""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        memo = defaultdict(int)
        for ch in t:
            memo[ch] -= 1
        l, cnt, length, ansL = 0, 0, float('inf'), -1
        for r, ch in enumerate(s):
            memo[ch] += 1
            if memo[ch] <= 0: cnt += 1
            while cnt == len(t) and memo[s[l]] > 0:
                memo[s[l]] -= 1
                l += 1
            if cnt == len(t):
                if length > r - l + 1:
                    length = r - l + 1
                    ansL = l
        return s[ansL: ansL + length] if ansL != -1 else ""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ori = defaultdict(int)
        cnt = defaultdict(int)
        s_arr = []
        for ch in t:
            ori[ch] += 1
        for i, ch in enumerate(s):
            if ch in ori:
                s_arr.append((ch, i))

        l, length, ansL = 0, float('inf'), -1
        for r in range(len(s_arr)):
            ch, idx = s_arr[r]
            cnt[ch] += 1
            while all(cnt[k] >= v for k, v in ori.items()):
                if idx - s_arr[l][1] + 1 < length:
                    length = idx - s_arr[l][1] + 1
                    ansL = s_arr[l][1]
                cnt[s_arr[l][0]] -= 1
                l += 1
        return s[ansL: ansL + length] if ansL != -1 else ""
# leetcode submit region end(Prohibit modification and deletion)
s = "ADOBECODEBANC"
t = "ABC"
print(Solution().minWindow(s, t))