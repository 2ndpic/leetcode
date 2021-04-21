# 一条包含字母 A-Z 的消息通过以下映射进行了 编码 ： 
# 
#  
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#  
# 
#  要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为： 
# 
#  
#  "AAJF" ，将消息分组为 (1 1 10 6) 
#  "KJF" ，将消息分组为 (11 10 6) 
#  
# 
#  注意，消息不能分组为 (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。 
# 
#  给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。 
# 
#  题目数据保证答案肯定是一个 32 位 的整数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "12"
# 输出：2
# 解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "226"
# 输出：3
# 解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "0"
# 输出：0
# 解释：没有字符映射到以 0 开头的数字。
# 含有 0 的有效映射是 'J' -> "10" 和 'T'-> "20" 。
# 由于没有字符，因此没有有效的方法对此进行解码，因为所有数字都需要映射。
#  
# 
#  示例 4： 
# 
#  
# 输入：s = "06"
# 输出：0
# 解释："06" 不能映射到 "F" ，因为字符串含有前导 0（"6" 和 "06" 在映射中并不等价）。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 100 
#  s 只包含数字，并且可能包含前导零。 
#  
#  Related Topics 字符串 动态规划 
#  👍 699 👎 0
import functools
class Solution:
    """
    backtracking
    Time Limit Exceeded
    """
    def numDecodings(self, s: str) -> int:
        def backtracking(start):
            if start == len(s):
                ans[0] += 1
                return
            for i in range(start, len(s)):
                if s[start] == "0" or int(s[start:i + 1]) > 26:break
                backtracking(i + 1)

        ans = [0]
        backtracking(0)
        return ans[0]


class Solution:
    def numDecodings(self, s: str) -> int:
        """
        recursion
        f(i) = valid(s[i]) * f(i + 1) + valid(s[i: i + 2]) * f(i + 2)
        """
        def valid(ss):
            if ss[0] == "0": return 0
            if int(ss) > 26: return 0
            return 1
        @functools.lru_cache(None)
        def dfs(i):
            if i == len(s): return 1
            if i == len(s) - 1: return valid(s[i])
            return valid(s[i]) * dfs(i + 1) + valid(s[i:i + 2]) * dfs(i + 2)

        return dfs(0)
class Solution:
    def numDecodings(self, s: str) -> int:
        """
        dynamic process
        dp[i] ==> s[0,..,i-1] can decode ways
        dp[i] = dp[i - 1] * valid(s[i - 1]) + dp[i - 2] * valid(s[i-2:i])
        """
        valid = lambda ss: int(ss[0] != "0" and int(ss) < 27)
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = valid(s[0])
        for i in range(2, len(s) + 1):
            dp[i] = dp[i - 1] * valid(s[i - 1]) + dp[i - 2] * valid(s[i - 2: i])
        return dp[-1]
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numDecodings(self, s: str) -> int:
        """
        dynamic process
        dp[i] ==> s[0,..,i-1] can decode ways
        dp[i] = dp[i - 1] * valid(s[i - 1]) + dp[i - 2] * valid(s[i-2:i])

        space optimazation
        """
        n = len(s)
        s = " " + s
        dp = [0] * 3
        dp[0] = 1
        for i in range(1, n + 1):
            a, b = ord(s[i]) - ord('0'), (ord(s[i - 1]) - ord('0')) * 10 + (ord(s[i]) - ord('0'))
            dp[i % 3] = (dp[(i - 1) % 3] if 0 < a < 10 else 0) + (dp[(i - 2) % 3] if 9 < b < 27 else 0)
        return dp[n % 3]

# leetcode submit region end(Prohibit modification and deletion)
s = "6065812287883668764831544958683283296479682877898293612168136334983851946827579555449329483852397155"
# s = "226"
print(Solution().numDecodings(s))