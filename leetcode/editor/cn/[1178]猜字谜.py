# 外国友人仿照中国字谜设计了一个英文版猜字谜小游戏，请你来猜猜看吧。 
# 
#  字谜的迷面 puzzle 按字符串形式给出，如果一个单词 word 符合下面两个条件，那么它就可以算作谜底： 
# 
#  
#  单词 word 中包含谜面 puzzle 的第一个字母。 
#  单词 word 中的每一个字母都可以在谜面 puzzle 中找到。 
#  例如，如果字谜的谜面是 "abcdefg"，那么可以作为谜底的单词有 "faced", "cabbage", 和 "baggage"；而 "beefed"
# （不含字母 "a"）以及 "based"（其中的 "s" 没有出现在谜面中）。 
#  
# 
#  返回一个答案数组 answer，数组中的每个元素 answer[i] 是在给出的单词列表 words 中可以作为字谜迷面 puzzles[i] 所对应的谜
# 底的单词数目。 
# 
#  
# 
#  示例： 
# 
#  输入：
# words = ["aaaa","asas","able","ability","actt","actor","access"], 
# puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
# 输出：[1,1,3,2,4,0]
# 解释：
# 1 个单词可以作为 "aboveyz" 的谜底 : "aaaa" 
# 1 个单词可以作为 "abrodyz" 的谜底 : "aaaa"
# 3 个单词可以作为 "abslute" 的谜底 : "aaaa", "asas", "able"
# 2 个单词可以作为 "absoryz" 的谜底 : "aaaa", "asas"
# 4 个单词可以作为 "actresz" 的谜底 : "aaaa", "asas", "actt", "access"
# 没有单词可以作为 "gaswxyz" 的谜底，因为列表中的单词都不含字母 'g'。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= words.length <= 10^5 
#  4 <= words[i].length <= 50 
#  1 <= puzzles.length <= 10^4 
#  puzzles[i].length == 7 
#  words[i][j], puzzles[i][j] 都是小写英文字母。 
#  每个 puzzles[i] 所包含的字符都不重复。 
#  
#  Related Topics 位运算 哈希表 
#  👍 77 👎 0
from typing import List
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        """
        超时。O(nm)
        数量级在10^9，计算机单秒计算量在10^7
        """
        n, m = len(puzzles), len(words)
        first_char_puzzles = [ord(i[0]) - ord('a') for i in puzzles]
        words_table = []
        ans = []
        for i in range(m):
            tmp = ["0"] * 26
            for c in words[i]:
                tmp[ord(c) - ord('a')] = "1"
            words_table.append("".join(tmp))
        puzzles_table = []
        for i in range(n):
            tmp = ["0"] * 26
            for c in puzzles[i]:
                tmp[ord(c) - ord('a')] = "1"
            puzzles_table.append(int("".join(tmp), 2))
        for i in range(n):
            count = 0
            for j in range(m):
                if words_table[j][first_char_puzzles[i]] == "1":
                    tmp = int(words_table[j], 2)
                    if puzzles_table[i] & tmp == tmp:
                        count += 1
            ans.append(count)

import collections
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        n = len(puzzles)
        words_table = collections.defaultdict(int)
        for word in words:
            tmp = ["0"] * 26
            for c in word:
                tmp[25 - ord(c) + ord('a')] = "1"
            words_table[int("".join(tmp), 2)] += 1
        ans = [0] * n
        for i in range(n):
            for j in range(1 << 6):
                u = 1 << (ord(puzzles[i][0]) - ord('a'))
                for k in range(1, 7):
                    if j >> (k - 1) & 1:
                        u += 1 << (ord(puzzles[i][k]) - ord('a'))
                ans[i] += words_table[u]
        return ans

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        words_table = collections.defaultdict(int)
        for word in words:
            tmp = 0
            for c in word:
                tmp |= 1 << (ord(c) - ord('a'))
            words_table[tmp] += 1
        ans = []
        for p in puzzles:
            tmp = [1 << (ord(p[0]) - ord('a'))]
            for j in range(1, 7):
                for k in range(len(tmp)):
                    tmp.append(tmp[k] | (1 << (ord(p[j]) - ord('a'))))
            ans.append(sum(words_table[i] for i in tmp))
        return ans

        
# leetcode submit region end(Prohibit modification and deletion)
words = ["apple","pleas","please"]
puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]

words = ["aaaa","asas","able","ability","actt","actor","access"]
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]

print(Solution().findNumOfValidWords(words, puzzles))