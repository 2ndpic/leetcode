from typing import List
from functools import lru_cache
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        @lru_cache(None)
        def f(i, is_limit, is_num):
            if i == len(s):
                return int(is_num)
            res = 0
            if not is_num:
                res += f(i + 1, False, False)
            for d in digits:
                if d <= s[i] or not is_limit:
                    res += f(i + 1, is_limit and d == s[i], True)
            return res

        s = str(n)
        return f(0, True, False)

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        def dp(x):
            t = x
            nums = []
            while t:
                nums.append(t % 10)
                t //= 10
            d = len(nums)
            ans = 0
            # 位数相同的情况
            for k in range(d - 1, -1, -1):
                cur = nums[k]
                l, r = 0, len(digits)
                while l < r:
                    mid = (l + r) // 2
                    if digits[mid] > cur: r = mid
                    else: l = mid + 1
                index = l - 1
                if index == -1:
                    break
                elif digits[index] == cur:
                    ans += index * (len(digits) ** k)
                    if k == 0: ans += 1
                else:
                    ans += (index + 1) * (len(digits) ** k)
                    # 因为此时的digit[index]小于cur，而下一次循环的意义在于固定住k位置的cur
                    # 但是digit并没有cur，所以之后的方案是构建不出来的，所以提前break
                    break

            cur = len(digits)
            for i in range(d - 1):
                ans += cur
                cur *= len(digits)
            return ans

        digits = list(map(int, digits))
        return dp(n)

# leetcode submit region end(Prohibit modification and deletion)
digits = ["1", "2", "3"]
n=143
print(Solution().atMostNGivenDigitSet(digits, 143))