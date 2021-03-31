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


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        def backtracking(start, num):
            ans[0] += 1
            if start == n:
                return
            for i in range(10):
                if i not in num:
                    num.add(i)
                    backtracking(start + 1, num)
                    num.remove(i)


        ans = [0]
        num = set()
        for i in range(10):
            num.add(i)
            num.add(0)
            backtracking(1, num)
            num.remove(i)
            print(i, ans[0])
        return ans[0]
# leetcode submit region end(Prohibit modification and deletion)
print(Solution().countNumbersWithUniqueDigits(3)) # 3 -> 739