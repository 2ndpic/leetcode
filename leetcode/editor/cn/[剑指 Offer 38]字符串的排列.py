# 输入一个字符串，打印出该字符串中字符的所有排列。 
# 
#  
# 
#  你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。 
# 
#  
# 
#  示例: 
# 
#  输入：s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]
#  
# 
#  
# 
#  限制： 
# 
#  1 <= s 的长度 <= 8 
#  Related Topics 回溯算法 
#  👍 336 👎 0

from typing import List
class Solution:
    def permutation(self, s: str) -> List[str]:
        """
        集合去重
        """
        def backtracking(word):
            if len(word) == len(s):
                ans.add(word)
                return
            for i in range(len(s)):
                if not visited[i]:
                    visited[i] = True
                    backtracking(word + s[i])
                    visited[i] = False

        ans = set()
        visited = [False] * len(s)
        backtracking("")
        return list(ans)

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permutation(self, s: str) -> List[str]:
        """
        排序去重
        """
        def backtracking(word):
            if len(word) == len(s):
                ans.append(word)
                return
            for i in range(len(s)):
                if i > 0 and s[i] == s[i - 1] and visited[i - 1] is False:
                    continue
                if not visited[i]:
                    visited[i] = True
                    backtracking(word + s[i])
                    visited[i] = False
        ans = []
        s = "".join(sorted(list(s)))
        visited = [False] * len(s)
        backtracking("")
        return ans
# leetcode submit region end(Prohibit modification and deletion)
s = "abc"
print(Solution().permutation(s))