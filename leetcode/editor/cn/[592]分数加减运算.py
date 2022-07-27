# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fractionAddition(self, expression: str) -> str:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a


# leetcode submit region end(Prohibit modification and deletion)
