# 给你一个括号字符串 s ，它只包含字符 '(' 和 ')' 。一个括号字符串被称为平衡的当它满足： 
# 
#  
#  任何左括号 '(' 必须对应两个连续的右括号 '))' 。 
#  左括号 '(' 必须在对应的连续两个右括号 '))' 之前。 
#  
# 
#  比方说 "())"， "())(())))" 和 "(())())))" 都是平衡的， ")()"， "()))" 和 "(()))" 都是不平衡的。 
# 
#  你可以在任意位置插入字符 '(' 和 ')' 使字符串平衡。 
# 
#  请你返回让 s 平衡的最少插入次数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "(()))"
# 输出：1
# 解释：第二个左括号有与之匹配的两个右括号，但是第一个左括号只有一个右括号。我们需要在字符串结尾额外增加一个 ')' 使字符串变成平衡字符串 "(())))"
#  。
#  
# 
#  示例 2： 
# 
#  输入：s = "())"
# 输出：0
# 解释：字符串已经平衡了。
#  
# 
#  示例 3： 
# 
#  输入：s = "))())("
# 输出：3
# 解释：添加 '(' 去匹配最开头的 '))' ，然后添加 '))' 去匹配最后一个 '(' 。
#  
# 
#  示例 4： 
# 
#  输入：s = "(((((("
# 输出：12
# 解释：添加 12 个 ')' 得到平衡字符串。
#  
# 
#  示例 5： 
# 
#  输入：s = ")))))))"
# 输出：5
# 解释：在字符串开头添加 4 个 '(' 并在结尾添加 1 个 ')' ，字符串变成平衡字符串 "(((())))))))" 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10^5 
#  s 只包含 '(' 和 ')' 。 
#  
#  Related Topics 栈 字符串 
#  👍 21 👎 0
class Solution:
    def minInsertions(self, s: str) -> int:
        right_need = 0
        ans = 0
        for i in s:
            if i == "(":
                if right_need % 2:      # 需求的右括号一定是偶数，若不是就操作插入一个右括号，需求-1
                    right_need -= 1
                    ans += 1            # 插入右括号
                right_need += 2
            else:
                right_need -= 1
                if right_need == -1:    # 多了一个右括号，插入一个左括号，还需要一个右括号
                    ans += 1
                    right_need = 1
        return ans + right_need

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minInsertions(self, s: str) -> int:
        """
        用left记录左括号个数
        如果遇到一个右括号且后面的一个也是右括号，则可以匹配掉一个之前的左括号，存的左括号个数-1
        若没有左括号了，就需要加上一个左括号，
        如果后面不是右括号，那么就需要添上一个右括号，不管前面是否有左括号，
        先处理完连续右括号的逻辑再去处理匹配左括号的逻辑
        """
        left, ans, i = 0, 0, 0
        while i < len(s):
            if s[i] == "(":
                left += 1
            else:
                if i + 1 < len(s) and s[i + 1] == ")":
                    i += 1
                else:
                    ans += 1        # 不管前面是否有左括号，需要加上一个右括号

                if left > 0:
                    left -= 1
                else:
                    ans += 1        # 没有左括号，加上一个左括号
            i += 1
        return ans + left * 2


# leetcode submit region end(Prohibit modification and deletion)
s = "(()))"
s = "())"
s = "))())("
# s = "(((((("
s = ")))"
print(Solution().minInsertions(s))