# 给你两个字符串 s 和 t ，请你找出 s 中的非空子串的数目，这些子串满足替换 一个不同字符 以后，是 t 串的子串。换言之，请你找到 s 和 t 串中 
# 恰好 只有一个字符不同的子字符串对的数目。 
# 
#  比方说， "computer" 和 "computation" 加粗部分只有一个字符不同： 'e'/'a' ，所以这一对子字符串会给答案加 1 。 
# 
#  请你返回满足上述条件的不同子字符串对数目。 
# 
#  一个 子字符串 是一个字符串中连续的字符。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aba", t = "baba"
# 输出：6
# 解释：以下为只相差 1 个字符的 s 和 t 串的子字符串对：
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# 加粗部分分别表示 s 和 t 串选出来的子字符串。
#  
# 示例 2：
# 
#  
# 输入：s = "ab", t = "bb"
# 输出：3
# 解释：以下为只相差 1 个字符的 s 和 t 串的子字符串对：
# ("ab", "bb")
# ("ab", "bb")
# ("ab", "bb")
# 加粗部分分别表示 s 和 t 串选出来的子字符串。
#  
# 示例 3：
# 
#  
# 输入：s = "a", t = "a"
# 输出：0
#  
# 
#  示例 4： 
# 
#  
# 输入：s = "abe", t = "bbc"
# 输出：10
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length, t.length <= 100 
#  s 和 t 都只包含小写英文字母。 
#  
#  Related Topics 哈希表 字符串 动态规划 👍 36 👎 0
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        m, n, ans = len(s), len(t), 0
        for i in range(m):
            for j in range(n):
                diff, k = 0, 0
                while i + k < m and j + k < n:
                    diff += (s[i + k] != t[j + k])
                    if diff == 1:
                        ans += 1
                    elif diff > 1:
                        break
                    k += 1
        return ans


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        m, n, ans = len(s), len(t), 0
        g = [[0] * (n + 1) for _ in range(m + 1)] # g[i][j]表示以s[i - 1], t[j - 1]结尾的相同子串有多少个
        f = [[0] * (n + 1) for _ in range(m + 1)] # f[i][j]表示以s[i - 1], t[j - 1]结尾的有一个字符不同的其他都相同的子串有多少个
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    g[i][j] = g[i - 1][j - 1] + 1
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = g[i - 1][j - 1] + 1
                ans += f[i][j]
        return ans
# leetcode submit region end(Prohibit modification and deletion)
