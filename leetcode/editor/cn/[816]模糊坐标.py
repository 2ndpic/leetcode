# 我们有一些二维坐标，如 "(1, 3)" 或 "(2, 0.5)"，然后我们移除所有逗号，小数点和空格，得到一个字符串S。返回所有可能的原始字符串到一个列表
# 中。 
# 
#  原始的坐标表示法不会存在多余的零，所以不会出现类似于"00", "0.0", "0.00", "1.0", "001", "00.01"或一些其他更小的数
# 来表示坐标。此外，一个小数点前至少存在一个数，所以也不会出现“.1”形式的数字。 
# 
#  最后返回的列表可以是任意顺序的。而且注意返回的两个数字中间（逗号之后）都有一个空格。 
# 
#  
# 
#  
# 示例 1:
# 输入: "(123)"
# 输出: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
#  
# 
#  
# 示例 2:
# 输入: "(00011)"
# 输出:  ["(0.001, 1)", "(0, 0.011)"]
# 解释: 
# 0.0, 00, 0001 或 00.01 是不被允许的。
#  
# 
#  
# 示例 3:
# 输入: "(0123)"
# 输出: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 
# 3)"]
#  
# 
#  
# 示例 4:
# 输入: "(100)"
# 输出: [(10, 0)]
# 解释: 
# 1.0 是不被允许的。
#  
# 
#  
# 
#  提示: 
# 
#  
#  4 <= S.length <= 12. 
#  S[0] = "(", S[S.length - 1] = ")", 且字符串 S 中的其他元素都是数字。 
#  
# 
#  
#  Related Topics 字符串 
#  👍 26 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def get_num(self, s):
        '''
        :param s:字符串如12或者00或者001或者010或者110
        对其中进行插点，要保证插点要符合规则
        :return:一个所有插点组合的列表
        '''
        res = []
        # 如果第一个字符是0且最后一个字符不为0，那么这个数是0.xxx;如果最后一个字符也是0的话，这个字符串就不能插点
        # 还有一种例外“0”
        if s[0] == '0':
            if s[-1] != '0':
                res.append(s[0]+"."+s[1:])
            elif len(s) == 1:
                    res.append(s)
            return res
        res.append(s)  # 不插点的情况
        # 最后一个字符为0，不可能插点
        if s[-1] == '0':
            return res

        for i in range(1, len(s)):
            res.append(s[:i]+"."+s[i:])
        return res


    def ambiguousCoordinates(self, S: str) -> List[str]:
        s = S[1:-1]
        ret = []
        for i in range(1, len(s)):
            x = self.get_num(s[:i])
            y = self.get_num(s[i:])
            for xi in x:
                for yi in y:
                    ret.append("({}, {})".format(xi, yi))
        return ret
        
# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.ambiguousCoordinates("(100)"))