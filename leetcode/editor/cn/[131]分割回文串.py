# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。 
# 
#  回文串 是正着读和反着读都一样的字符串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a"
# 输出：[["a"]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 16 
#  s 仅由小写英文字母组成 
#  
#  Related Topics 深度优先搜索 动态规划 回溯算法 
#  👍 635 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def helper(i, l):
            # 求以s[i]开头的答案,l保存着之前的答案
            if i == len(s):
                res.append(l)
                return
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    helper(j, l + [s[i:j]])
        res = []
        helper(0, [])
        return res
# leetcode submit region end(Prohibit modification and deletion)
s = "aabbaa"
print(Solution().partition(s))