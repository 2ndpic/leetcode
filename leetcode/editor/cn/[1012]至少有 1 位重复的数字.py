# leetcode submit region begin(Prohibit modification and deletion)
f = [[1] * 10 for _ in range(10)]
for i in range(1, 10):
    for j in range(i, 10):
        f[i][j] = f[i][j - 1] * j
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        """
        数位DP
        dp(x): [0,...,x]中没有重复数字的正整数个数
        ans = n - dp(n) + 1
        """
        def dp(x):
            t = x
            nums = []
            while t:
                nums.append(t % 10)
                t //= 10
            d = len(nums)
            if d == 1:
                return x + 1
            ans, s = 0, 0
            for k in range(d - 1, -1, -1):
                cur = nums[k]
                cnt = 0
                for i in range(cur - 1, -1, -1):
                    if k == d - 1 and i == 0: continue
                    if ((s >> i) & 1) == 0: cnt += 1
                l, r = 10 - (d - k) - (k - 1), 10 - (d - k) # 后面数位的可用方案连乘的上下界
                ans += (cnt * f[l][r]) if l <= r else cnt
                if ((s >> cur) & 1) == 1: break
                s |= (1 << cur)
                if k == 0: ans += 1
            ans += 10
            cur = 9
            for i in range(2, d):
                cur *= (10 - i + 1)
                ans += cur
            return ans

        return n - dp(n) + 1

# leetcode submit region end(Prohibit modification and deletion)
from functools import lru_cache

class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        @lru_cache(None)
        def f(i, mask, is_limit, is_num, is_valid):
            """
            f(i)表示从高到低第i位及其之后数位的合法方案数
            """
            if i == len(s):
                return int(is_valid)
            ans = 0
            if not is_num:
                ans += f(i + 1, 0, False, False, False)
            up = int(s[i]) if is_limit else 9
            for d in range(0 if is_num else 1, up + 1):
                ans += f(i + 1, mask | (1 << d), is_limit and d == up, True, is_valid or mask >> d & 1 == 1)
            return ans

        s = str(n)
        return f(0, 0, True, False, False)

print(Solution().numDupDigitsAtMostN(11))