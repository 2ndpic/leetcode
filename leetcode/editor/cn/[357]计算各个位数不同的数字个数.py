# 给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10n 。 
# 
#  示例: 
# 
#  输入: 2
# 输出: 91 
# 解释: 答案应为除去 11,22,33,44,55,66,77,88,99 外，在 [0,100) 区间内的所有数字。
#  
#  Related Topics 数学 动态规划 回溯算法 
#  👍 128 👎 0
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        """
        回溯法
        关键是最开始把最高位的搜索范围是限定在[1,10)之间
        能全部搜完
        """
        def backtracking(start):
            nonlocal ans
            if start > n: return
            ans += 1
            for i in range(start==0, 10):
                if used[i]: continue
                used[i] = True
                backtracking(start + 1)
                used[i] = False

        ans = 0
        used = [False] * 10
        backtracking(0)
        return ans
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        """
        回溯法
        思路是一样的，最高位的搜索路径是[1, 9],其他位都是[1, 10]能把结果穷尽
        """
        def backtracking(l, path):
            nonlocal ans
            if path == [0] or len(path) > n: return
            ans += 1
            for i in range(len(l)):
                backtracking(l[:i] + l[i + 1:], path + [l[i]])
        ans = 0
        backtracking(list(range(10)), [])
        return ans
# leetcode submit region begin(Prohibit modification and deletion)
def n_nums(n):
    ans = 9
    for i in range(1, n):
        ans *= (10 + i - n)
    return ans
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        """
        动态规划
        dp[n] = dp[n-1] + 第n位的答案
        第n位的答案 = n位（最高位）的选择有9种[1,..,9](不能为0) * n-1位的选择有9种(除开n位的选择数) * n - 2位置的选择有8种 ... * 第i位的选择有10 + i - n种
        """
        dp = [1] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + n_nums(i)
        return dp[n]

# leetcode submit region end(Prohibit modification and deletion)
print(Solution().countNumbersWithUniqueDigits(2)) # 3 -> 739