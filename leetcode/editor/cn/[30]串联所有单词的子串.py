# 给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。 
# 
#  注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。 
# 
#  
# 
#  示例 1： 
# 
#  输入：
#   s = "barfoothefoobarman",
#   words = ["foo","bar"]
# 输出：[0,9]
# 解释：
# 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
# 输出的顺序不重要, [9,0] 也是有效答案。
#  
# 
#  示例 2： 
# 
#  输入：
#   s = "wordgoodgoodgoodbestword",
#   words = ["word","good","best","word"]
# 输出：[]
#  
#  Related Topics 哈希表 双指针 字符串 
#  👍 418 👎 0

from typing import List
import collections
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n, m, k, ans = len(s), sum(len(i) for i in words), len(words[0]), []
        memo = collections.Counter(words)
        for i in range(n - m + 1):
            tmp = []
            for j in range(i, i + m, k):
                tmp.append(s[j:j + k])
            if collections.Counter(tmp) == memo:
                ans.append(i)
        return ans
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n, m, k, ans = len(s), sum(len(i) for i in words), len(words[0]), []
        memo = collections.Counter(words)
        idx2word = collections.defaultdict(int)
        for i in range(n - k + 1):
            idx2word[i] = s[i:i+k]
        for i in range(n - m + 1):
            tmp = []
            for j in range(i, i + m, k):
                tmp.append(idx2word[j])
            if collections.Counter(tmp) == memo:
                ans.append(i)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
s = "barfoothefoobarman"
words = ["foo", "bar"]

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]
print(Solution().findSubstring(s, words))