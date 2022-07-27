from math import *
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fractionAddition(self, expression: str) -> str:
        def cal(n1, d1, n2, d2):
            c = lcm(d1, d2)
            n1 *= c // d1
            n2 *= c // d2
            d1 = c
            n1 = n1 + n2
            c = gcd(n1, d1)
            return n1 // c, d1 // c
        l, r = 0, 0
        fraction = [0, 1]
        while r <= len(expression):
            if r == len(expression) or (r != 0 and expression[r] in "+-"):
                numerator, denominator = [int(s) for s in expression[l:r].split("/")]
                fraction[0], fraction[1] = cal(fraction[0], fraction[1], numerator, denominator)
                l = r
            r += 1
        return "/".join(map(str, fraction))

class Solution:
    def fractionAddition(self, expression: str) -> str:
        numerator, denominator = 0, 1  # 分子，分母
        i, n = 0, len(expression)
        while i < n:
            # 读取分子
            numerator1, sign = 0, 1
            if expression[i] in "+-":
                if expression[i] == '-':
                    sign = -1
                i += 1
            while i < n and expression[i].isdigit():
                numerator1 = numerator1 * 10 + int(expression[i])
                i += 1
            numerator1 = sign * numerator1
            i += 1

            # 读取分母
            denominator1 = 0
            while i < n and expression[i].isdigit():
                denominator1 = denominator1 * 10 + int(expression[i])
                i += 1

            numerator = numerator * denominator1 + numerator1 * denominator
            denominator *= denominator1
        if numerator == 0:
            return "0/1"
        g = gcd(abs(numerator), denominator)
        return f"{numerator // g}/{denominator // g}"


# leetcode submit region end(Prohibit modification and deletion)
test = "-1/2+1/2"
print(Solution().fractionAddition(test))