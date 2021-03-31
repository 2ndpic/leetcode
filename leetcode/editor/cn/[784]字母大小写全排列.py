# 给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。 
# 
#  
# 
#  示例：
# 输入：S = "a1b2"
# 输出：["a1b2", "a1B2", "A1b2", "A1B2"]
# 
# 输入：S = "3z4"
# 输出：["3z4", "3Z4"]
# 
# 输入：S = "12345"
# 输出：["12345"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  S 的长度不超过12。 
#  S 仅由数字和字母组成。 
#  
#  Related Topics 位运算 回溯算法 
#  👍 257 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def backtracking(start, l):
            ans.append("".join(l))
            for i in range(start, len(l)):
                if l[i].isalpha():
                    if l[i].islower():
                        l[i] = l[i].upper()
                        backtracking(i + 1, l)
                        l[i] = l[i].lower()
                    else:
                        l[i] = l[i].lower()
                        backtracking(i + 1, l)
                        l[i] = l[i].upper()

        ans = []
        backtracking(0, list(S))
        return ans
# leetcode submit region end(Prohibit modification and deletion)
S = "a1b2"
S = "3zZ4"
S = "12345"
print(Solution().letterCasePermutation(S))