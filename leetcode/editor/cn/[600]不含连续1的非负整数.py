# leetcode submit region begin(Prohibit modification and deletion)
"""
f[i][j]表示二进制长度为i，且最高位不超过j时的合法方案数
                       这里的合法即二进制中没有连续的1
f[i][0]：如果当前位不超过0的话，需要统计所有满足(0...)形式的合法方案，低一位只能填1（填0会出现重复计数，即需要忽略前导0的数值）
f[i + 1][0] = f[i][1]
f[i][1]：如果当前位不超过1的话，需要统计所有满足(1...)和(0...)的合法方案
        (1...)情况，低一位只能不超过0，(0...)低一位情况只能不超过1
f[i+1][1] = f[i][0] + f[i][1]
"""
N = 32
f = [[0, 0] for _ in range(N)]
f[1][0], f[1][1] = 1, 2
for i in range(1, N - 1):
    f[i + 1][0] = f[i][1]
    f[i + 1][1] = f[i][0] + f[i][1]
class Solution:
    def findIntegers(self, n: int) -> int:
        def getLen(x):
            for i in range(31, -1, -1):
                if x >> i & 1 == 1:
                    return i
            return 0
        def dp(x):
            d = getLen(x)
            ans, prev = 0, 0
            for k in range(d, -1, -1):
                cur = x >> k & 1
                if cur == 1:
                    # 加上 长度为k+1AND最高位数值为0 时的合法方案数
                    ans += f[k+1][0]
                if prev == cur == 1:
                    break
                prev = cur
                if k == 0:
                    ans += 1
            return ans
        return dp(n)



# leetcode submit region end(Prohibit modification and deletion)
"""
数位dp
"""
from functools import lru_cache
class Solution:
    def findIntegers(self, n: int) -> int:
        @lru_cache(None)
        def f(i, is_limit, pre1):
            if i == len(s):
                return 1
            up = int(s[i]) if is_limit else 1
            ans = f(i + 1, is_limit and up == 0, False)
            if not pre1 and up == 1:
                ans += f(i + 1, is_limit, True)
            return ans
        s = bin(n)[2:]
        return f(0, True, False)