# 请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。
# 
#  实现词典类 WordDictionary ： 
# 
#  
#  WordDictionary() 初始化词典对象 
#  void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配 
#  bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回 false 。word 中可能包含一些 
# '.' ，每个 . 都可以表示任何一个字母。 
#  
# 
#  
# 
#  示例： 
# 
#  
# 输入：
# ["WordDictionary","addWord","addWord","addWord","search","search","search",
# "search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# 输出：
# [null,null,null,null,false,true,true,true]
# 
# 解释：
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= word.length <= 500 
#  addWord 中的 word 由小写英文字母组成 
#  search 中的 word 由 '.' 或小写英文字母组成 
#  最多调用 50000 次 addWord 和 search 
#  
#  Related Topics 深度优先搜索 设计 字典树 字符串 👍 328 👎 0
from collections import deque
class WordDictionary:

    def __init__(self):
        self.words = {}

    def addWord(self, word: str) -> None:
        cur = self.words
        for w in word:
            if w not in cur: cur[w] = {}
            cur = cur[w]
        cur["END"] = {}

    def search(self, word: str) -> bool:
        if word[0] == ".": q = deque(list(self.words.values()))
        else: q = deque([self.words.get(word[0], {})])
        idx = 1
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if idx == len(word) and "END" in cur: return True
                if idx < len(word):
                    if word[idx] != "." and word[idx] in cur:
                        q.append(cur[word[idx]])
                    elif word[idx] == ".":
                        q.extend(list(cur.values()))
            idx += 1
        return False

# leetcode submit region begin(Prohibit modification and deletion)
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word):
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True

class WordDictionary:

    def __init__(self):
        self.trieRoot = TrieNode()

    def addWord(self, word: str) -> None:
        self.trieRoot.insert(word)

    def search(self, word: str) -> bool:
        def dfs(index, node):
            if index == len(word):
                return node.isEnd
            ch = word[index]
            if ch != ".":
                child = node.children[ord(ch) - ord('a')]
                if child is not None and dfs(index + 1, child): return True
            else:
                for child in node.children:
                    if child is not None and dfs(index + 1, child): return True
            return False
        return dfs(0, self.trieRoot)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# leetcode submit region end(Prohibit modification and deletion)
wd = WordDictionary()
wd.addWord("bad")
wd.addWord("dad")
wd.addWord("mad")
print(wd.search("..."))