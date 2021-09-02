# 你将会得到一份单词表 words，一个字母表 letters （可能会有重复字母），以及每个字母对应的得分情况表 score。 
# 
#  请你帮忙计算玩家在单词拼写游戏中所能获得的「最高得分」：能够由 letters 里的字母拼写出的 任意 属于 words 单词子集中，分数最高的单词集合的
# 得分。 
# 
#  单词拼写游戏的规则概述如下： 
# 
#  
#  玩家需要用字母表 letters 里的字母来拼写单词表 words 中的单词。 
#  可以只使用字母表 letters 中的部分字母，但是每个字母最多被使用一次。 
#  单词表 words 中每个单词只能计分（使用）一次。 
#  根据字母得分情况表score，字母 'a', 'b', 'c', ... , 'z' 对应的得分分别为 score[0], score[1], ..., 
# score[25]。 
#  本场游戏的「得分」是指：玩家所拼写出的单词集合里包含的所有字母的得分之和。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d",
# "g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
# 输出：23
# 解释：
# 字母得分为  a=1, c=9, d=5, g=3, o=2
# 使用给定的字母表 letters，我们可以拼写单词 "dad" (5+1+5)和 "good" (3+2+2+5)，得分为 23 。
# 而单词 "dad" 和 "dog" 只能得到 21 分。 
# 
#  示例 2： 
# 
#  输入：words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], 
# score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
# 输出：27
# 解释：
# 字母得分为  a=4, b=4, c=4, x=5, z=10
# 使用给定的字母表 letters，我们可以组成单词 "ax" (4+5)， "bx" (4+5) 和 "cx" (4+5) ，总得分为 27 。
# 单词 "xxxz" 的得分仅为 25 。 
# 
#  示例 3： 
# 
#  输入：words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,
# 1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
# 输出：0
# 解释：
# 字母 "e" 在字母表 letters 中只出现了一次，所以无法组成单词表 words 中的单词。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= words.length <= 14 
#  1 <= words[i].length <= 15 
#  1 <= letters.length <= 100 
#  letters[i].length == 1 
#  score.length == 26 
#  0 <= score[i] <= 10 
#  words[i] 和 letters[i] 只包含小写的英文字母。 
#  
#  Related Topics 位运算 数组 字符串 动态规划 回溯 状态压缩 👍 35 👎 0

from typing import List
from collections import Counter, defaultdict
from copy import copy
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        """
        f[mask]表示选择单词状态为mask状态下，最高分数和当前剩余字母数量
        """
        n = len(words)
        cal = lambda w: sum(score[ord(ch) - ord('a')] for ch in w)
        words_score = [cal(word) for word in words]
        words_memo = [Counter(word) for word in words]
        ans = 0
        f = [[defaultdict(int), 0] for _ in range(1 << n)]
        for c in letters:
            f[0][0][c] += 1
        for mask in range(1, 1 << n):
            for i in range(n):
                if mask & (1 << i):
                    left_letters, cur_score = f[mask ^ (1 << i)]
                    tmp = copy(left_letters)
                    for k, v in words_memo[i].items():
                        if v > tmp[k]: break
                        tmp[k] -= v
                    else:
                        if cur_score + words_score[i] > f[mask][1]:
                            f[mask] = [tmp, cur_score + words_score[i]]
            ans = max(ans, f[mask][1])
        return ans
class Solution:
def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

    def helper(start, curr_sum, counter):
        nonlocal ans
        if start > len(words):
            return
        ans = max(ans, curr_sum)
        if sum(counter.values()) == 0: return
        for j, w_counter in enumerate(words_counter[start:], start):
            if all(counter[k] >= v for k, v in w_counter.items()):
                helper(j + 1, curr_sum + words_score[j], counter - w_counter)
    words_score = [sum(score[ord(c)-ord('a')] for c in word) for word in words]
    words_counter = [Counter(word) for word in words]
    ans = 0
    helper(0, 0, Counter(letters))
    return ans

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        """
        dfs
        https://leetcode-cn.com/problems/maximum-score-words-formed-by-letters/solution/ti-jie-1255-de-fen-zui-gao-de-dan-ci-ji-he-by-zero/
        """
        def dfs(i, cur_letters):
            if i == n or sum(cur_letters.values()) == 0: return 0
            ret = dfs(i + 1, cur_letters)
            if all(cur_letters[k] >= v for k, v in words_memo[i].items()):
                cur_letters -= words_memo[i]
                ret = max(ret, words_score[i] + dfs(i + 1, cur_letters))
                cur_letters += words_memo[i]
            return ret
        n = len(words)
        cal = lambda w: sum(score[ord(ch) - ord('a')] for ch in w)
        words_score = [cal(word) for word in words]
        words_memo = [Counter(word) for word in words]
        return dfs(0, Counter(letters))


# leetcode submit region end(Prohibit modification and deletion)
words = ["dog","cat","dad","good"]; letters = ["a","a","c","d","d","d", "g","o","o"]; score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
words = ["xxxz","ax","bx","cx"];letters = ["z","a","b","c","x","x","x"];score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
print(Solution().maxScoreWords(words, letters, score))