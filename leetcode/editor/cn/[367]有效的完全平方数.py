# 给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。 
# 
#  说明：不要使用任何内置的库函数，如 sqrt。 
# 
#  示例 1： 
# 
#  输入：16
# 输出：True 
# 
#  示例 2： 
# 
#  输入：14
# 输出：False
#  
#  Related Topics 数学 二分查找 
#  👍 189 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo, hi = 1, num
        while lo < hi:
            mid = (lo + hi) // 2
            if mid * mid < num: lo = mid + 1
            else: hi = mid
        return True if lo * lo == num else False
# leetcode submit region end(Prohibit modification and deletion)
print(Solution().isPerfectSquare(16))