"""
数位DP + KMP的匹配思想
"""
from functools import lru_cache
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        @lru_cache(None)
        def f(i, stats, bound):
            if stats == len(evil):
                return 0
            if i == n:
                return 1

            lo = ord(s1[i]) if bound & 1 else ord('a')
            hi = ord(s2[i]) if bound & 2 else ord('z')
            ans = 0
            for d in range(lo, hi + 1):
                ch = chr(d)
                nxt_stats = stats
                while nxt_stats >= 0 and evil[nxt_stats] != ch:
                    nxt_stats = nxt[nxt_stats]
                nxt_stats += 1
                if bound == 0:
                    nxt_bound = 0
                elif bound == 1:
                    nxt_bound = 1 if d == lo else 0
                elif bound == 2:
                    nxt_bound = 2 if d == hi else 0
                else:
                    if lo == hi:
                        nxt_bound = 3
                    elif d == lo:
                        nxt_bound = 1
                    elif d == hi:
                        nxt_bound = 2
                    else:
                        nxt_bound = 0
                ans += f(i + 1, nxt_stats, nxt_bound)
            return ans


        nxt = [-1] * len(evil)
        i, j = 0, -1
        while i < len(evil) - 1:
            if j == -1 or evil[j] == evil[i]:
                i += 1
                j += 1
                nxt[i] = j
            else:
                j = nxt[j]
        return f(0, 0, 3)


# leetcode submit region end(Prohibit modification and deletion)

def getNext(s):
    nxt = [-1] * len(s)
    i, j = 0, -1
    while i < len(s) - 1:
        if j == -1 or s[i] == s[j]:
            i += 1
            j += 1
            nxt[i] = j
        else:
            j = nxt[j]
    return nxt

class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        def get_evil_int(ch, evil_int):
            while evil_int != -1 and evil[evil_int] != ch:
                evil_int = nxt[evil_int]
            return evil_int + 1

        @lru_cache(None)
        def f(i, evil_int, is_down_limit, is_up_limit):
            if evil_int == len(evil):
                return 0
            if i == n:
                return 1
            ans = 0
            down = ord(s1[i]) if is_down_limit else ord('a')
            up = ord(s2[i]) if is_up_limit else ord('z')
            for j in range(down, up + 1):
                ans = (ans + f(i + 1, get_evil_int(chr(j), evil_int), is_down_limit and j == down, is_up_limit and j == up)) % mod
            return ans

        mod = 10 ** 9 + 7
        nxt = getNext(evil)
        return f(0, 0, True, True)





n = 2
s1 = "aa"
s2 = "az"
evil = "b"
print(Solution().findGoodStrings(n, s1, s2, evil))