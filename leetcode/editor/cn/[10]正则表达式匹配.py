# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。 
# 
#  
#  '.' 匹配任意单个字符 
#  '*' 匹配零个或多个前面的那一个元素 
#  
# 
#  所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aa" p = "a"
# 输出：false
# 解释："a" 无法匹配 "aa" 整个字符串。
#  
# 
#  示例 2: 
# 
#  
# 输入：s = "aa" p = "a*"
# 输出：true
# 解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "ab" p = ".*"
# 输出：true
# 解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
#  
# 
#  示例 4： 
# 
#  
# 输入：s = "aab" p = "c*a*b"
# 输出：true
# 解释：因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
#  
# 
#  示例 5： 
# 
#  
# 输入：s = "mississippi" p = "mis*is*p*."
# 输出：false 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 20 
#  0 <= p.length <= 30 
#  s 可能为空，且只包含从 a-z 的小写字母。 
#  p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。 
#  保证每次出现字符 * 时，前面都匹配到有效的字符 
#  
#  Related Topics 字符串 动态规划 回溯算法 
#  👍 2173 👎 0
import functools
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        f[i][j]表示s中以第i个字符结尾的子串和p中以第j个字符结尾的子串是否匹配,答案为f[len(s)][len(p)]
        初始化f[0][0] = True
        if p[j-1] 是普通字符: f[i][j] = f[i-1][j-1] & s[i-1] == p[j-1]
        elif p[j-1] == ".": f[i][j] = f[i-1][j-1]
        elif p[j-1] == "*": 读得p[j-2]的字符例如a，然后根据a*实际匹配s中a的个数是0个，1个，2个。。。
            当匹配0个时，f[i][j] = f[i][j-2]
            当匹配1个时，f[i][j] = f[i-1][j-2] and (s[i-1] == p[j-2] or p[j-2] == ".")
            当匹配2个时，f[i][j] = f[i-2][j-2] and (s[i-1] == p[j-2] or p[j-2] == ".")
            ...
            总结f[i][j] = f[i][j-2] or
                         f[i-1][j-2] and (s[i-1] == p[j-2] or p[j-2] == ".") or
                         f[i-2][j-2] and (s[i-1] == p[j-2] or p[j-2] == ".") or ...
             f[i-1][j] = f[i-1][j-2] or
                         f[i-2][j-2] and (s[i-2] == p[j-2] or p[j-2] == ".") or ...
            比较两个等式，f[i][j] = f[i][j-2] or (f[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == "."))
            这样处理就降低一个n的时间复杂度
        """
        n, m = len(s), len(p)
        f = [[False] * (m + 1) for _ in range(n + 1)]
        f[0][0] = True
        for i in range(n + 1):
            for j in range(1, m + 1):
                if i - 1 >= 0 and p[j - 1] != "*":
                    f[i][j] = f[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == ".")
                else:
                    f[i][j] = (j - 2 >= 0 and f[i][j - 2]) or (i - 1 >= 0 and f[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == "."))
        return f[n][m]


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        原问题：f(i,j)表示s[i:]与p[j:]是否匹配，
        s[i:]和p[j:]均分成第一个字符和后面的字符两个部分，
        子问题可能是f(i,j+2)、f(i+1,j)、f(i+1,j+1)，
        对应下面的例子：
        s   p
        ---
        a   c*a （p包含*、*匹配前面的字符0次）
        aa  a*  （p包含*、*匹配前面的字符1次）
        ab  ab  （p不包含*）
        """
        @functools.lru_cache(None)
        def f(i, j):
            # *匹配0次的情况，可能是p[i:]为空、p末尾为*。即i结束时，j未结束
            if j == m: return i == n
            # 第一个字符是否匹配
            fst = i < n and (p[j] == s[i] or p[j] == ".")

            # *匹配0次或1次
            if j + 1 < m and p[j + 1] == "*":
                return f(i, j + 2) or fst and f(i + 1, j)

            return fst and f(i + 1, j + 1)

        n, m = len(s), len(p)
        return f(0, 0)
# leetcode submit region end(Prohibit modification and deletion)
