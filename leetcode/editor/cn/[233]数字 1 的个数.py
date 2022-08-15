# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 13
# 输出：6
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 0
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 2 * 109 
#  
#  Related Topics 递归 数学 动态规划 
#  👍 278 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countDigitOne(self, n: int) -> int:
        """
        数位DP
        """
        def dp(x):
            t = x
            nums = []
            while t:
                nums.append(t % 10)
                t //= 10
            d = len(nums)
            ans = 0
            for k in range(d - 1, -1, -1):
                cur = nums[k]
                base = 10 ** k
                # k位置前面的高位不是最大值的情况
                ans += (n // base // 10) * base
                # k位置前面的高位是最大值的情况
                if cur == 1:
                    ans += (n % base) + 1
                elif cur > 1:
                    ans += base
            return ans
        return dp(n)
from functools import lru_cache
class Solution:
    def countDigitOne(self, n: int) -> int:
        @lru_cache(None)
        def f(i, cnt1, is_limit):
            if i == len(s):
                return cnt1
            ans = 0
            up = int(s[i]) if is_limit else 9
            for d in range(up + 1):
                ans += f(i + 1, cnt1 + (d == 1), is_limit and d == up)
            return ans

        s = str(n)
        return f(0, 0, True)

class Solution:
    def countDigitOne(self, n: int) -> int:
        """
        假设n是123456，考虑从[0,123456]这些数，百位上的1一共有多少个
        存在千位数的：(n // 1000) * 100 = 123 * 100
        不存在千位数的[0,..,n‘]，n'=n%1000=456，百位上的1一共有:
        - 0 <= n' < 100    |   0
        - 100 <= n' < 200  |   n' - 100 + 1
        - n' >= 200        |   100
        百位上的1总计：max(min(n' - 100 + 1, 100), 0) + n // 1000 * 100
        抽象合计：max(min(n % (10 ^ (i + 1)) - 10^i + 1, 10^i), 0) + n // 10^(i + 1) * 10^i
        """
        ans, cur = 0, 1
        while cur <= n:
            ans += max(min(n % (cur * 10) - cur + 1, cur), 0) + n // (cur * 10) * cur
            cur *= 10
        return ans
# leetcode submit region end(Prohibit modification and deletion)
print(Solution().countDigitOne(123456))