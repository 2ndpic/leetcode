# 给定一个化学式formula（作为字符串），返回每种原子的数量。 
# 
#  原子总是以一个大写字母开始，接着跟随0个或任意个小写字母，表示原子的名字。 
# 
#  如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。例如，H2O 和 H2O2 是可行的，但 H1O2 这个表达是不可行的。
#  
# 
#  两个化学式连在一起是新的化学式。例如 H2O2He3Mg4 也是化学式。 
# 
#  一个括号中的化学式和数字（可选择性添加）也是化学式。例如 (H2O2) 和 (H2O2)3 是化学式。 
# 
#  给定一个化学式，输出所有原子的数量。格式为：第一个（按字典序）原子的名子，跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），跟着它的数
# 量（如果数量大于 1），以此类推。 
# 
#  示例 1: 
# 
#  
# 输入: 
# formula = "H2O"
# 输出: "H2O"
# 解释: 
# 原子的数量是 {'H': 2, 'O': 1}。
#  
# 
#  示例 2: 
# 
#  
# 输入: 
# formula = "Mg(OH)2"
# 输出: "H2MgO2"
# 解释: 
# 原子的数量是 {'H': 2, 'Mg': 1, 'O': 2}。
#  
# 
#  示例 3: 
# 
#  
# 输入: 
# formula = "K4(ON(SO3)2)2"
# 输出: "K4N2O14S4"
# 解释: 
# 原子的数量是 {'K': 4, 'N': 2, 'O': 14, 'S': 4}。
#  
# 
#  注意: 
# 
#  
#  所有原子的第一个字母为大写，剩余字母都是小写。 
#  formula的长度在[1, 1000]之间。 
#  formula只包含字母、数字和圆括号，并且题目中给定的是合法的化学式。 
#  
#  Related Topics 栈 哈希表 字符串 
#  👍 160 👎 0

from collections import defaultdict
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def getname(index):
            name = [formula[index]]
            index += 1
            while index < len(formula) and formula[index].islower():
                name.append(formula[index])
                index += 1
            return "".join(name), index

        def getnum(index):
            num = 0
            while index < len(formula) and formula[index].isdigit():
                num = num * 10 + int(formula[index])
                index += 1
            return num if num else 1, index

        stack = [defaultdict(int)]
        i = 0
        while i < len(formula):
            ch = formula[i]
            if ch == "(":
                stack.append(defaultdict(int))
                i += 1
            elif ch.isalnum():
                name, i = getname(i)
                num, i = getnum(i)
                stack[-1][name] += num
            else:
                d2 = stack.pop()
                num, i = getnum(i + 1)
                for k, v in d2.items():
                    stack[-1][k] += (v * num)

        d = stack.pop()
        ans = []
        for name in sorted(d.keys()):
            ans.append(name)
            if d[name] > 1:
                ans.append(str(d[name]))
        return "".join(ans)
# leetcode submit region end(Prohibit modification and deletion)
formula = "K4(ON(SO3)2)2" # "K4N2O14S4"
print(Solution().countOfAtoms(formula))