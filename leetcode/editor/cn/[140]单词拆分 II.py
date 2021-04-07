# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的
# 句子。 
# 
#  说明： 
# 
#  
#  分隔时可以重复使用字典中的单词。 
#  你可以假设字典中没有重复的单词。 
#  
# 
#  示例 1： 
# 
#  输入:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# 输出:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
#  
# 
#  示例 2： 
# 
#  输入:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# 输出:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# 解释: 注意你可以重复使用字典中的单词。
#  
# 
#  示例 3： 
# 
#  输入:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出:
# []
#  
#  Related Topics 动态规划 回溯算法 
#  👍 438 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def backtracking(start, path):
            if start == len(s):
                ans.append(" ".join(path))
                return
            for i in range(start, len(s)):
                w = s[start:i + 1]
                if w in wordDict:
                    backtracking(i + 1, path + [w])
        wordDict = set(wordDict)
        ans = []
        backtracking(0, [])
        return ans

# leetcode submit region end(Prohibit modification and deletion)
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
print(Solution().wordBreak(s, wordDict))