# 我们正在玩一个猜数游戏，游戏规则如下： 
# 
#  我从 1 到 n 之间选择一个数字，你来猜我选了哪个数字。 
# 
#  每次你猜错了，我都会告诉你，我选的数字比你的大了或者小了。 
# 
#  然而，当你猜了数字 x 并且猜错了的时候，你需要支付金额为 x 的现金。直到你猜到我选的数字，你才算赢得了这个游戏。 
# 
#  示例: 
# 
#  n = 10, 我选择了8.
# 
# 第一轮: 你猜我选择的数字是5，我会告诉你，我的数字更大一些，然后你需要支付5块。
# 第二轮: 你猜是7，我告诉你，我的数字更大一些，你支付7块。
# 第三轮: 你猜是9，我告诉你，我的数字更小一些，你支付9块。
# 
# 游戏结束。8 就是我选的数字。
# 
# 你最终要支付 5 + 7 + 9 = 21 块钱。
#  
# 
#  给定 n ≥ 1，计算你至少需要拥有多少现金才能确保你能赢得这个游戏。 
#  Related Topics 数学 动态规划 博弈 
#  👍 274 👎 0

import functools
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @functools.lru_cache(None)
        def cal(low, high):
            if low >= high:
                return 0
            ans = float('inf')
            for i in range((low + high) // 2, high + 1):
                tmp = i + max(cal(low, i - 1), cal(i + 1, high))
                ans = min(ans, tmp)
            return ans
        cal.cache_clear()
        return cal(1, n)
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for length in range(2, n + 1):
            for start in range(1, n - length + 2):
                end = start + length - 1
                min_tmp = float('inf')
                for piv in range((start + end) // 2, end + 1):
                    tmp = piv + max(dp[start][piv - 1], dp[piv + 1][end] if piv + 1 <= end else 0)
                    min_tmp = min(min_tmp, tmp)
                dp[start][end] = min_tmp

        return dp[1][n]
# leetcode submit region end(Prohibit modification and deletion)
print(Solution().getMoneyAmount(10))