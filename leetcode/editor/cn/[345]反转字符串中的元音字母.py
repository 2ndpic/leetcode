# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。 
# 
#  
# 
#  示例 1： 
# 
#  输入："hello"
# 输出："holle"
#  
# 
#  示例 2： 
# 
#  输入："leetcode"
# 输出："leotcede" 
# 
#  
# 
#  提示： 
# 
#  
#  元音字母不包含字母 "y" 。 
#  
#  Related Topics 双指针 字符串 
#  👍 191 👎 0
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        l, r, vow = 0, len(s) - 1, {"a", "e", "i", "o", "u"}
        while l < r:
            if s[l].lower() in vow and s[r].lower() in vow:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            else:
                if s[l].lower() not in vow: l += 1
                if s[r].lower() not in vow: r -= 1
        return "".join(s)

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        l, r, vow = 0, len(s) - 1, {"a", "e", "i", "o", "u"}
        while l < r:
            while l < len(s) and s[l].lower() not in vow:
                l += 1
            while r > 0 and s[r].lower() not in vow:
                r -= 1
            if l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return "".join(s)

# leetcode submit region end(Prohibit modification and deletion)
