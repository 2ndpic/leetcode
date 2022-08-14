# leetcode submit region begin(Prohibit modification and deletion)
f = [[1] * 10 for _ in range(10)]
for i in range(1, 10):
    for j in range(i, 10):
        f[i][j] = f[i][j - 1] * j


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        """
        数位DP
        f[l][r]表示从i到j的累积
        res1: d位且最高位小于n的数
        res2: d位且最高位等于n的数
        res3: 小于d位的数
        dp(x): 返回[0,..,x]内的合法的数目
        求解res2是关键:
        对x进行从「从高到低」的处理（x的数位为n），对于第k位而言，（k不是最高位）
        假设在第k位为cur，那么为了满足「大小限制」关系，只能在[0,cur-1]范围内取数，
        同时为了满足「相同数字只能使用一次」的限制，需要使用一个int变量s来记录使用情况
        统计[0,cur-1]范围内同时符合两个限制条件的数的个数，记为cnt
        当第k位有cnt种合法选择后，后面的位数(共k-1位)可以在满足「相同数字只能使用一次」的限制条件下
        任意选择：k-1位     k-2位      k-3位     。。。  0位          （共k位）
               10-(d-k) 10-(d-k)-1 10-(d-k)-2 。。。 10-(d-k)-(k-1)
        为了快速得到剩下k位有多少方案，可以预处理乘积数组f[l][r]表示l*(l+1)*...*(r-1)*r
        """

        def dp(x):
            t = x
            nums = []
            while t:
                nums.append(t % 10)
                t //= 10
            d = len(nums)
            if d <= 1:
                return x + 1

            ans = 0
            s = 0
            # 位数相同（res1 + res2）
            for k in range(d - 1, -1, -1):
                cur = nums[k]
                cnt = 0
                # 计算第k位，满足 [0,..,cur-1] and (没有使用过) 的数字个数
                for i in range(cur - 1, -1, -1):
                    if k == d - 1 and i == 0:
                        # 最高位不能为0
                        continue
                    if ((s >> i) & 1) == 0:
                        cnt += 1
                l, r = 10 - (d - k) - (k - 1), 10 - (d - k)
                ans += (cnt * f[l][r]) if l <= r else cnt
                # 准备固定第k位，检查是否有重复
                if ((s >> cur) & 1) == 1:
                    break
                s |= (1 << cur)
                if k == 0:
                    # 最低位之前加的结果都是比cur小的方案（cnt没有包含cur），
                    # 如果没有提前break，那么说明数x也是合法的
                    ans += 1
            # 位数少于d（res3）
            ans += 10  # 1位的情况
            cur = 9
            for i in range(2, d):
                cur *= (10 - i + 1)
                ans += cur
            return ans

        return dp(10 ** n - 1)

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        ans = 10 # 1位的情况
        cur = 9
        for i in range(2, n + 1):
            cur *= (10 - i + 1)
            ans += cur
        return ans
# leetcode submit region end(Prohibit modification and deletion)
