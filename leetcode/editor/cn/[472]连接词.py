# 给你一个 不含重复 单词的字符串数组 words ，请你找出并返回 words 中的所有 连接词 。 
# 
#  连接词 定义为：一个完全由给定数组中的至少两个较短单词组成的字符串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses",
# "rat","ratcatdogcat"]
# 输出：["catsdogcats","dogcatsdog","ratcatdogcat"]
# 解释："catsdogcats" 由 "cats", "dog" 和 "cats" 组成; 
#      "dogcatsdog" 由 "dog", "cats" 和 "dog" 组成; 
#      "ratcatdogcat" 由 "rat", "cat", "dog" 和 "cat" 组成。
#  
# 
#  示例 2： 
# 
#  
# 输入：words = ["cat","dog","catdog"]
# 输出：["catdog"] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= words.length <= 10⁴ 
#  0 <= words[i].length <= 1000 
#  words[i] 仅由小写字母组成 
#  0 <= sum(words[i].length) <= 10⁵ 
#  
#  Related Topics 深度优先搜索 字典树 数组 字符串 动态规划 👍 205 👎 0
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word):
        node = self
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.isEnd = True

    def dfs(self, word, start):
        if start == len(word):
            return True
        node = self
        for i in range(start, len(word)):
            node = node.children[ord(word[i]) - ord('a')]
            if node is None: return False
            if node.isEnd and self.dfs(word, i + 1): return True
        return False


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """
        方法一：字典树+深度优先搜索
        要判断一个word是不是连接词，即判断这个单词是不是完全由至少两个数组中的非空单词组成（可以重复）
        判断更短单词是否在给定数组中可以用字典树实现
        为了方便处理，将单词数组按单词长度递增排序，那么当前单词是否是连接词，只用到在他前面的单词的信息
        如果是连接词就加入结果数组，如果不是连接词就加入字典树
        判断是否是连接词，可以用dfs，从该单词的第一个字符开始，在字典树中依次搜索每个字符对应的节点，可能有两种情况：
        - 字符对应的节点是一个更短单词的结尾，则找到了一个更短单词，那么从该字符的下一个字符开始搜索下一个更短单词
        - 如果一个字符对应的节点在字典树中不存在，那么当前搜索失败，回到上一个单词结尾继续往下搜索
        """
        words.sort(key=lambda x: len(x))
        root = Trie()
        ans = []
        for word in words:
            if not word: continue
            if not root.dfs(word, 0): root.insert(word)
            else: ans.append(word)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
