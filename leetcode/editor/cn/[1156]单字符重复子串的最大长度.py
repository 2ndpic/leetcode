# 如果字符串中的所有字符都相同，那么这个字符串是单字符重复的字符串。 
# 
#  给你一个字符串 text，你只能交换其中两个字符一次或者什么都不做，然后得到一些单字符重复的子串。返回其中最长的子串的长度。 
# 
#  
# 
#  示例 1： 
# 
#  输入：text = "ababa"
# 输出：3
#  
# 
#  示例 2： 
# 
#  输入：text = "aaabaaa"
# 输出：6
#  
# 
#  示例 3： 
# 
#  输入：text = "aaabbaaa"
# 输出：4
#  
# 
#  示例 4： 
# 
#  输入：text = "aaaaa"
# 输出：5
#  
# 
#  示例 5： 
# 
#  输入：text = "abcdef"
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= text.length <= 20000 
#  text 仅由小写英文字母组成。 
#  
#  Related Topics 字符串 滑动窗口 👍 79 👎 0
from collections import Counter, defaultdict
from itertools import groupby
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        def check(curr):
            # 不合法返回True
            if len(curr) == 1: return False
            if len(curr) > 2 or min(curr.values()) > 1: return True
            if list(curr.values()) == [1, 1] and all(cnt[k] == v for k, v in curr.items()): return True
            if list(curr.values()) != [1, 1] and all(cnt[k] == v for k, v in curr.items() if v != 1): return True
            return False
        l, n, curr = 0, len(text), defaultdict(int)
        cnt, ans = Counter(text), 0
        for r in range(n):
            curr[text[r]] += 1
            while check(curr):
                curr[text[l]] -= 1
                if curr[text[l]] == 0: curr.pop(text[l])
                l += 1
            ans = max(ans, r - l + 1)
        return ans

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # We get the group's key and length first, e.g. 'aaabaaa' -> [[a , 3], [b, 1], [a, 3]
        A = [[c, len(list(g))] for c, g in groupby(text)]
        # We also generate a count dict for easy look up e.g. 'aaabaaa' -> {a: 6, b: 1}
        count = Counter(text)
        # only extend 1 more, use min here to avoid the case that there's no extra char to extend
        res = max(min(k + 1, count[c]) for c, k in A)
        # merge 2 groups together
        for i in range(1, len(A) - 1):
            # if both sides have the same char and are separated by only 1 char
            if A[i - 1][0] == A[i + 1][0] and A[i][1] == 1:
                # min here serves the same purpose
                res = max(res, min(A[i - 1][1] + A[i + 1][1] + 1, count[A[i + 1][0]]))
        return res
# leetcode submit region end(Prohibit modification and deletion)
print(Solution().maxRepOpt1("ababa"))