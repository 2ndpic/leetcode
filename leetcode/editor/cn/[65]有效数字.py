# 有效数字（按顺序）可以分成以下几个部分： 
# 
#  
#  一个 小数 或者 整数 
#  （可选）一个 'e' 或 'E' ，后面跟着一个 整数 
#  
# 
#  小数（按顺序）可以分成以下几个部分： 
# 
#  
#  （可选）一个符号字符（'+' 或 '-'） 
#  下述格式之一：
#  
#  至少一位数字，后面跟着一个点 '.' 
#  至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字 
#  一个点 '.' ，后面跟着至少一位数字 
#  
#  
#  
# 
#  整数（按顺序）可以分成以下几个部分： 
# 
#  
#  （可选）一个符号字符（'+' 或 '-'） 
#  至少一位数字 
#  
# 
#  部分有效数字列举如下： 
# 
#  
#  ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1",
#  "53.5e93", "-123.456e789"] 
#  
# 
#  部分无效数字列举如下： 
# 
#  
#  ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"] 
#  
# 
#  给你一个字符串 s ，如果 s 是一个 有效数字 ，请返回 true 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "0"
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "e"
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "."
# 输出：false
#  
# 
#  示例 4： 
# 
#  
# 输入：s = ".1"
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 20 
#  s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，或者点 '.' 。 
#  
#  Related Topics 数学 字符串 
#  👍 240 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from enum import Enum
class Solution:
    def isNumber(self, s: str) -> bool:
        """
        有限状态自动机
        所有状态:
        0.初始状态 1.非指数符号位 2.整数部分数字 3.左侧有数字的小数点
        4.左侧无数字的小数点 5.小数部分数字 6.字符e
        7.指数部分符号位 8.指数部分数字
        初始状态就是状态0，接受状态集合为2，3，5，8
        注意：2.e3 == 2000.0 也是合法的
        """
        State = Enum("State", [
            "STATE_INITIAL",
            "STATE_INT_SIGN",
            "STATE_INTEGER",
            "STATE_POINT",
            "STATE_POINT_WITHOUT_INT",
            "STATE_FRACTION",
            "STATE_EXP",
            "STATE_EXP_SIGN",
            "STATE_EXP_NUMBER",
            "STATE_END"
        ])
        Chartype = Enum("Chartype", [
            "CHAR_NUMBER",
             "CHAR_EXP",
             "CHAR_POINT",
             "CHAR_SIGN",
             "CHAR_ILLEGAL"
        ])

        def toChartype(ch: str) -> Chartype:
            if ch.isdigit():
                return Chartype.CHAR_NUMBER
            elif ch.lower() == "e":
                return Chartype.CHAR_EXP
            elif ch == ".":
                return Chartype.CHAR_POINT
            elif ch in "+-":
                return Chartype.CHAR_SIGN
            else:
                return Chartype.CHAR_ILLEGAL

        transfer = {
            State.STATE_INITIAL: {
                Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                Chartype.CHAR_SIGN: State.STATE_INT_SIGN,
                Chartype.CHAR_POINT: State.STATE_POINT_WITHOUT_INT
            },
            State.STATE_INT_SIGN: {
                Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                Chartype.CHAR_POINT: State.STATE_POINT_WITHOUT_INT
            },
            State.STATE_INTEGER: {
                Chartype.CHAR_EXP: State.STATE_EXP,
                Chartype.CHAR_POINT: State.STATE_POINT,
                Chartype.CHAR_NUMBER: State.STATE_INTEGER
            },
            State.STATE_POINT: {
                Chartype.CHAR_NUMBER: State.STATE_FRACTION,
                Chartype.CHAR_EXP: State.STATE_EXP
            },
            State.STATE_POINT_WITHOUT_INT: {
                Chartype.CHAR_NUMBER: State.STATE_FRACTION
            },
            State.STATE_FRACTION: {
                Chartype.CHAR_NUMBER: State.STATE_FRACTION,
                Chartype.CHAR_EXP: State.STATE_EXP
            },
            State.STATE_EXP: {
                Chartype.CHAR_SIGN: State.STATE_EXP_SIGN,
                Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER
            },
            State.STATE_EXP_SIGN: {
                Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER
            },
            State.STATE_EXP_NUMBER: {
                Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER
            }
        }
        st = State.STATE_INITIAL
        for ch in s:
            typ = toChartype(ch)
            if typ not in transfer[st]:
                return False
            st = transfer[st][typ]

        return st in [State.STATE_INTEGER, State.STATE_POINT,
                      State.STATE_FRACTION, State.STATE_EXP_NUMBER, State.STATE_END]







# leetcode submit region end(Prohibit modification and deletion)
#  ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1",
#  "53.5e93", "-123.456e789"]