# 给你一个字符串列表 words 和一个目标字符串 target 。words 中所有字符串都 长度相同 。 
# 
#  你的目标是使用给定的 words 字符串列表按照下述规则构造 target ： 
# 
#  
#  从左到右依次构造 target 的每一个字符。 
#  为了得到 target 第 i 个字符（下标从 0 开始），当 target[i] = words[j][k] 时，你可以使用 words 列表中第 j 
# 个字符串的第 k 个字符。 
#  一旦你使用了 words 中第 j 个字符串的第 k 个字符，你不能再使用 words 字符串列表中任意单词的第 x 个字符（x <= k）。也就是说，所
# 有单词下标小于等于 k 的字符都不能再被使用。 
#  请你重复此过程直到得到目标字符串 target 。 
#  
# 
#  请注意， 在构造目标字符串的过程中，你可以按照上述规定使用 words 列表中 同一个字符串 的 多个字符 。 
# 
#  请你返回使用 words 构造 target 的方案数。由于答案可能会很大，请对 10⁹ + 7 取余 后返回。 
# 
#  （译者注：此题目求的是有多少个不同的 k 序列，详情请见示例。） 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：words = ["acca","bbbb","caca"], target = "aba"
# 输出：6
# 解释：总共有 6 种方法构造目标串。
# "aba" -> 下标为 0 ("acca")，下标为 1 ("bbbb")，下标为 3 ("caca")
# "aba" -> 下标为 0 ("acca")，下标为 2 ("bbbb")，下标为 3 ("caca")
# "aba" -> 下标为 0 ("acca")，下标为 1 ("bbbb")，下标为 3 ("acca")
# "aba" -> 下标为 0 ("acca")，下标为 2 ("bbbb")，下标为 3 ("acca")
# "aba" -> 下标为 1 ("caca")，下标为 2 ("bbbb")，下标为 3 ("acca")
# "aba" -> 下标为 1 ("caca")，下标为 2 ("bbbb")，下标为 3 ("caca")
#  
# 
#  示例 2： 
# 
#  
# 输入：words = ["abba","baab"], target = "bab"
# 输出：4
# 解释：总共有 4 种不同形成 target 的方法。
# "bab" -> 下标为 0 ("baab")，下标为 1 ("baab")，下标为 2 ("abba")
# "bab" -> 下标为 0 ("baab")，下标为 1 ("baab")，下标为 3 ("baab")
# "bab" -> 下标为 0 ("baab")，下标为 2 ("baab")，下标为 3 ("baab")
# "bab" -> 下标为 1 ("abba")，下标为 2 ("baab")，下标为 3 ("baab")
#  
# 
#  示例 3： 
# 
#  
# 输入：words = ["abcd"], target = "abcd"
# 输出：1
#  
# 
#  示例 4： 
# 
#  
# 输入：words = ["abab","baba","abba","baab"], target = "abba"
# 输出：16
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= words.length <= 1000 
#  1 <= words[i].length <= 1000 
#  words 中所有单词长度相同。 
#  1 <= target.length <= 1000 
#  words[i] 和 target 都仅包含小写英文字母。 
#  
#  Related Topics 数组 字符串 动态规划 👍 18 👎 0
from functools import lru_cache
from typing import List
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        """
        n, m = len(target), len(words[0])
        f[i][j]表示利用words[j:]个字符构造出target[i:]的方案数，答案为f[0][0] (m - j >= n - i -> j <= m - n + i)
        不用w[j]字符
        f[i][j] = f[i][j + 1]
        用w[j]字符
        f[i][j] = f[i + 1][j + 1] * len(w for w in words if w[j] == target[i])
        两种情况取和
        """
        n, m, mod = len(target), len(words[0]), 10 ** 9 + 7
        cnt = [[0] * 26 for _ in range(m)]
        for w in words:
            for i, ch in enumerate(w):
                cnt[i][ord(ch) - ord('a')] += 1
        f = [[0] * m for _ in range(n)]
        for j in range(m - 1, -1, -1):
            f[n - 1][j] = cnt[j][ord(target[n - 1]) - ord('a')]
            if j + 1 < m: f[n - 1][j] = (f[n - 1][j] + f[n - 1][j + 1]) % mod
        for i in range(n - 2, -1, -1):
            for j in range(m - n + i, -1, -1):
                f[i][j] = (f[i + 1][j + 1] * cnt[j][ord(target[i]) - ord('a')]) % mod
                if j + 1 <= m - n + i: f[i][j] = (f[i][j] + f[i][j + 1]) % mod
        return f[0][0]


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i >= n: return 1  # 先判断i溢出的情况
            if j >= m: return 0
            return (dfs(i, j + 1) + dfs(i + 1, j + 1) * cnt[j][ord(target[i]) - ord('a')]) % mod

        n, m, mod = len(target), len(words[0]), 10 ** 9 + 7
        cnt = [[0] * 26 for _ in range(m)]
        for w in words:
            for i, ch in enumerate(w):
                cnt[i][ord(ch) - ord('a')] += 1
        return dfs(0, 0)

# leetcode submit region end(Prohibit modification and deletion)
words = ["cabbaacaaaccaabbbbaccacbabbbcb","bbcabcbcccbcacbbbaacacaaabbbac","cbabcaacbcaaabbcbaabaababbacbc","aacabbbcaaccaabbaccacabccaacca","bbabbaabcaabccbbabccaaccbabcab","bcaccbbaaccaabcbabbacaccbbcbbb","cbbcbcaaaacacabbbabacbaabbabaa","cbbbbbbcccbabbacacacacccbbccca","bcbccbccacccacaababcbcbbacbbbc","ccacaabaaabbbacacbacbaaacbcaca","bacaaaabaabccbcbbaacacccabbbcb","bcbcbcabbccabacbcbcaccacbcaaab","babbbcccbbbbbaabbbacbbaabaabcc","baaaacaaacbbaacccababbaacccbcb","babbaaabaaccaabacbbbacbcbababa","cbacacbacaaacbaaaabacbbccccaca","bcbcaccaabacaacaaaccaabbcacaaa","cccbabccaabbcbccbbabaaacbacaaa","bbbcabacbbcabcbcaaccbcacacccca","ccccbbaababacbabcaacabaccbabaa","caaabccbcaaccabbcbcaacccbcacba","cccbcaacbabaacbaaabbbbcbbbbcbb","cababbcacbabcbaababcbcabbaabba","aaaacacaaccbacacbbbbccaabcccca","cbcaaaaabacbacaccbcbcbccaabaac","bcbbccbabaccabcccacbbaacbbcbba","cccbabbbcbbabccbbabbbbcaaccaab","acccacccaabbcaccbcaaccbababacc","bcacabaacccbbcbbacabbbbbcaaaab","cacccaacbcbccbabccabbcbabbcacc","aacabbabcaacbaaacaabcabcaccaab","cccacabacbabccbccaaaaabbcacbcc","cabaacacacaaabaacaabababccbaaa","caabaccaacccbaabcacbcbbabccabc","bcbbccbbaaacbaacbccbcbababcacb","bbabbcabcbbcababbbbccabaaccbca","cacbbbccabaaaaccacbcbabaabbcba","ccbcacbabababbbcbcabbcccaccbca","acccabcacbcbbcbccaccaacbabcaab","ccacaabcbbaabaaccbabcbacaaabaa","cbabbbbcabbbbcbccabaabccaccaca","acbbbbbccabacabcbbabcaacbbaacc","baaababbcabcacbbcbabacbcbaaabc","cabbcabcbbacaaaaacbcbbcacaccac"]
target = "acbaccacbbaaabbbabac"
print(Solution().numWays(words, target))