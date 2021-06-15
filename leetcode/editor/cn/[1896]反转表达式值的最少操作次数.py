# 给你一个 有效的 布尔表达式，用字符串 expression 表示。这个字符串包含字符 '1'，'0'，'&'（按位 与 运算），'|'（按位 或 运算），
# '(' 和 ')' 。 
# 
#  
#  比方说，"()1|1" 和 "(1)&()" 不是有效 布尔表达式。而 "1"， "(((1))|(0))" 和 "1|(0&(1))" 是 有效 布尔表
# 达式。 
#  
# 
#  你的目标是将布尔表达式的 值 反转 （也就是将 0 变为 1 ，或者将 1 变为 0），请你返回达成目标需要的 最少操作 次数。 
# 
#  
#  比方说，如果表达式 expression = "1|1|(0&0)&1" ，它的 值 为 1|1|(0&0)&1 = 1|1|0&1 = 1|0&1 = 
# 1&1 = 1 。我们想要执行操作将 新的 表达式的值变成 0 。 
#  
# 
#  可执行的 操作 如下： 
# 
#  
#  将一个 '1' 变成一个 '0' 。 
#  将一个 '0' 变成一个 '1' 。 
#  将一个 '&' 变成一个 '|' 。 
#  将一个 '|' 变成一个 '&' 。 
#  
# 
#  注意：'&' 的 运算优先级 与 '|' 相同 。计算表达式时，括号优先级 最高 ，然后按照 从左到右 的顺序运算。 
# 
#  
# 
#  示例 1： 
# 
#  输入：expression = "1&(0|1)"
# 输出：1
# 解释：我们可以将 "1&(0|1)" 变成 "1&(0&1)" ，执行的操作为将一个 '|' 变成一个 '&' ，执行了 1 次操作。
# 新表达式的值为 0 。
#  
# 
#  示例 2： 
# 
#  输入：expression = "(0&0)&(0&0&0)"
# 输出：3
# 解释：我们可以将 "(0&0)&(0&0&0)" 变成 "(0|1)|(0&0&0)" ，执行了 3 次操作。
# 新表达式的值为 1 。
#  
# 
#  示例 3： 
# 
#  输入：expression = "(0|(1|0&1))"
# 输出：1
# 解释：我们可以将 "(0|(1|0&1))" 变成 "(0|(0|0&1))" ，执行了 1 次操作。
# 新表达式的值为 0 。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= expression.length <= 105 
#  expression 只包含 '1'，'0'，'&'，'|'，'(' 和 ')' 
#  所有括号都有与之匹配的对应括号。 
#  不会有空的括号（也就是说 "()" 不是 expression 的子字符串）。 
#  
#  Related Topics 栈 动态规划 
#  👍 9 👎 0
class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        states, ops = [], []
        for c in expression:
            if c in "01)":
                if c == "0":
                    states.append((0, 1))
                elif c == "1":
                    states.append((1, 0))
                else:
                    assert ops[-1] == "("
                    ops.pop()

                if len(ops) > 0 and ops[-1] != "(":
                    op = ops.pop()
                    p2, q2 = states.pop()
                    p1, q1 = states.pop()
                    if op == "&":
                        states.append((min(p1, p2), min(q1 + q2, 1 + min(q1, q2))))
                    else:
                        states.append((min(p1 + p2, 1 + min(p1, p2)), min(q1, q2)))
            else:
                ops.append(c)
        return max(states[-1])

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        def corr(s):
            stack, d = [], {}
            for i, v in enumerate(s):
                if v == "(":
                    stack.append(i)
                elif v == ")":
                    last = stack.pop()
                    d[i] = last
            return d

        def dfs(beg, end):
            if beg == end:
                return (int(expression[beg]), 1)
            beg2 = d.get(end, end)
            if beg2 == beg: return dfs(beg + 1, end - 1)
            p1, c1 = dfs(beg, beg2 - 2)
            p2, c2 = dfs(beg2, end)
            op = expression[beg2 - 1]

            t = {"|": lambda x, y: x | y, "&": lambda x, y: x & y}
            c3 = 1 if p1 + p2 == 1 else (min(c1, c2) + (p1 ^ (op == "&")))
            return (t[op](p1, p2), c3)

        d = corr(expression)
        return dfs(0, len(expression) - 1)[1]

# leetcode submit region end(Prohibit modification and deletion)
expression = "1&(0|1)"
# expression = "1|1"
print(Solution().minOperationsToFlip(expression))