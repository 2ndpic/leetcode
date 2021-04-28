# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：c = 5
# 输出：true
# 解释：1 * 1 + 2 * 2 = 5
#  
# 
#  示例 2： 
# 
#  输入：c = 3
# 输出：false
#  
# 
#  示例 3： 
# 
#  输入：c = 4
# 输出：true
#  
# 
#  示例 4： 
# 
#  输入：c = 2
# 输出：true
#  
# 
#  示例 5： 
# 
#  输入：c = 1
# 输出：true 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= c <= 231 - 1 
#  
#  Related Topics 数学 
#  👍 195 👎 0
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        def check(n):
            t = int(n ** 0.5)
            return t * t == n
        for i in range(0, int(c ** 0.5) + 1):
            if check(c - i * i): return True
        return False

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        双指针
        lo, hi = 0, int(c ** 0.5)
        lo * lo + hi * hi < c  -> lo += 1
        lo * lo + hi * hi > c -> hi -= 1
        """
        lo, hi = 0, int(c ** 0.5)
        while lo <= hi:
            tmp = lo * lo + hi * hi
            if tmp == c: return True
            elif tmp < c: lo += 1
            else: hi -= 1
        return False
# leetcode submit region end(Prohibit modification and deletion)
for i in range(0, 6):
    print(Solution().judgeSquareSum(i))