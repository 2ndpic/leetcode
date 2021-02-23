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
# leetcode submit region begin(Prohibit modification and deletion)
def check(l, r, s, words):
    memo = collections.Counter(words)
    j = 0
    for i in range(l, r + 1):





class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans = []
        l, r = 0, 0
        while r < len(s):
            while not check(l, r, s, words):
                l += 1
            ans.append(l)
            r += 1
        return ans





# leetcode submit region end(Prohibit modification and deletion)
