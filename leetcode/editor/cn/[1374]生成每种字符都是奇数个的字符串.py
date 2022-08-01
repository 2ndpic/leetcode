# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateTheString(self, n: int) -> str:
        return "a" * n if n & 1 else "a" * (n - 1) + "b"
# leetcode submit region end(Prohibit modification and deletion)
