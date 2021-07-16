# 给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。 
# 
#  示例 1: 
# 
#  
# 输入: "abab"
# 
# 输出: True
# 
# 解释: 可由子字符串 "ab" 重复两次构成。
#  
# 
#  示例 2: 
# 
#  
# 输入: "aba"
# 
# 输出: False
#  
# 
#  示例 3: 
# 
#  
# 输入: "abcabcabcabc"
# 
# 输出: True
# 
# 解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)
#  
#  Related Topics 字符串 字符串匹配 
#  👍 509 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(n // 2, 0, -1):
            if n % i == 0:
                tmp = s[:i]
                for j in range(0, n, i):
                    if tmp != s[j:j+i]:
                        break
                else:
                    return True
        return False
# leetcode submit region end(Prohibit modification and deletion)
