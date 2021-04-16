# 使用下面描述的算法可以扰乱字符串 s 得到字符串 t ：
#  
#  如果字符串的长度为 1 ，算法停止 
#  如果字符串的长度 > 1 ，执行下述步骤：
#  
#  在一个随机下标处将字符串分割成两个非空的子字符串。即，如果已知字符串 s ，则可以将其分成两个子字符串 x 和 y ，且满足 s = x + y 。 
#  随机 决定是要「交换两个子字符串」还是要「保持这两个子字符串的顺序不变」。即，在执行这一步骤之后，s 可能是 s = x + y 或者 s = y + x
#  。 
#  在 x 和 y 这两个子字符串上继续从步骤 1 开始递归执行此算法。 
#  
#  
#  
# 
#  给你两个 长度相等 的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。如果是，返回 true ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s1 = "great", s2 = "rgeat"
# 输出：true
# 解释：s1 上可能发生的一种情形是：
# "great" --> "gr/eat" // 在一个随机下标处分割得到两个子字符串
# "gr/eat" --> "gr/eat" // 随机决定：「保持这两个子字符串的顺序不变」
# "gr/eat" --> "g/r / e/at" // 在子字符串上递归执行此算法。两个子字符串分别在随机下标处进行一轮分割
# "g/r / e/at" --> "r/g / e/at" // 随机决定：第一组「交换两个子字符串」，第二组「保持这两个子字符串的顺序不变」
# "r/g / e/at" --> "r/g / e/ a/t" // 继续递归执行此算法，将 "at" 分割得到 "a/t"
# "r/g / e/ a/t" --> "r/g / e/ a/t" // 随机决定：「保持这两个子字符串的顺序不变」
# 算法终止，结果字符串和 s2 相同，都是 "rgeat"
# 这是一种能够扰乱 s1 得到 s2 的情形，可以认为 s2 是 s1 的扰乱字符串，返回 true
#  
# 
#  示例 2： 
# 
#  
# 输入：s1 = "abcde", s2 = "caebd"
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 输入：s1 = "a", s2 = "a"
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  s1.length == s2.length 
#  1 <= s1.length <= 30 
#  s1 和 s2 由小写英文字母组成 
#  
#  Related Topics 字符串 动态规划 
#  👍 249 👎 0
"""
如果s1通过扰乱能得到s2，则s2通过扰乱必能得到s1,称这种关系是【和谐】的。和谐 => 必定长度相等,字符个数相等
若一种分割将s1分割成了l(s1), r(s1)
若不交换，则我们需要在s2中分割得到l(s2)与l(s1)是和谐的，并且r(s2)与r(s1)是和谐的
若交换，则需要在s2分割得到l(s1)与r(s2)是和谐的，并且r(s1)与l(s1)是和谐的
我们就把原本需要解决的问题划分成了两个本质相同，但规模更小的子问题，因此可以考虑使用动态规划解决
设f(s1, s2)表示s1，s2是否和谐，那么显而易见的两个情况是：
f(s1, s2) = True if s1 == s2 ; False if count(s1) != count(s2)
其他情况就需要枚举分割点，
不交换：f(s1, s2) = any(f(s1[0:i], s2[0:i]) and f(s1[i:], s2[i:])) i = [1, n - 1]
交换: f(s1, s2) = any(f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]))   i = [1, n - 1]

"""
import collections
import functools
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        """
        超时
        """
        @functools.lru_cache()
        def dfs(ss1, ss2):
            if ss1 == ss2:
                return True
            elif not count(ss1, ss2):
                return False
            for i in range(1, len(ss1)):
                if (dfs(ss1[:i], ss2[:i]) and dfs(ss1[i:], ss2[i:])) or (dfs(ss1[:i], ss2[-i:]) and dfs(ss1[i:], ss2[:-i])):
                    return True
            return False
        count = lambda x, y: collections.Counter(x) == collections.Counter(y)
        return dfs(s1, s2)
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @functools.lru_cache(None)
        def dfs(s1_start, s2_start, length):
            if s1[s1_start:s1_start+length] == s2[s2_start:s2_start+length]:
                return True
            elif collections.Counter(s1[s1_start:s1_start+length]) != collections.Counter(s2[s2_start:s2_start+length]):
                return False
            for i in range(1, length):
                if dfs(s1_start, s2_start, i) and dfs(s1_start + i, s2_start + i, length - i):
                    return True
                if dfs(s1_start, s2_start + length - i, i) and dfs(s1_start + i, s2_start, length - i):
                    return True
            return False
        ans = dfs(0, 0, len(s1))
        dfs.cache_clear()
        return ans

# leetcode submit region end(Prohibit modification and deletion)
# s1 = "abcde"
# s2 = "caebd"
# s1 = "great"
# s2 = "rgeat"
# s1 = "a"
# s2 = "a"
# s1 = "abcdbdacbdac"
# s2 = "bdacabcdbdac"
s1 = "eebaacbcbcadaaedceaaacadccd"
s2 = "eadcaacabaddaceacbceaabeccd"
print(Solution().isScramble(s1, s2))