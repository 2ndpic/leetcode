"""
[0...n]有多少个数字中出现了数字1
"""
from functools import lru_cache
class Solution:
    def getNumofOne(self, n):
        @lru_cache(None)
        def f(i, is_limit, appear):
            if i == len(s):
                return int(appear)
            ans = 0
            up = int(s[i]) if is_limit else 9
            for d in range(up + 1):
                ans += f(i + 1, is_limit and d == up, appear | (d == 1))
            return ans

        s = str(n)
        return f(0, True, False)

    def getNumofOneByDp(self, n):
        def dp(x):
            t = x
            nums = []
            while t:
                nums.append(t % 10)
                t //= 10
            d = len(nums)
            ans = 0
            app_one = False
            for k in range(d - 1, -1, -1):
                cur = nums[k]
                for d in range(cur - 1, -1, -1):
                    if app_one:
                        ans += 10 ** k
                    else:
                        ans += f[k] if d != 1 else 10 ** k
                app_one |= cur == 1
                if k == 0 and 1 in nums:
                    ans += 1
            return ans

        # f[i]表示长度为i的所有十进制数[0...0, ..., 9...9]中的合法方案数，即数字中有1的整数个数
        # f[i] = 9 * f[i - 1] + 10 ** (i - 1)
        N = 12
        f = [0] * N
        f[1] = 1
        for i in range(2, N):
            f[i] = f[i - 1] * 9 + 10 ** (i - 1)

        return dp(n)