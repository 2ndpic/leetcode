# 给你一个整数 n ，请你找出并返回第 n 个 丑数 。 
# 
#  丑数 就是只包含质因数 2、3 和/或 5 的正整数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 10
# 输出：12
# 解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：1
# 解释：1 通常被视为丑数。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 1690 
#  
#  Related Topics 堆 数学 动态规划 
#  👍 631 👎 0

import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        最小堆。每次取一个最小元素出来，同时把它乘上因子2,3,5
        """
        seen = set()
        fac = [2, 3, 5]
        ans, pq = [], [1]
        for i in range(n):
            ans.append(heapq.heappop(pq))
            for j in fac:
                if j * ans[-1] not in seen:
                    seen.add(ans[-1] * j)
                    heapq.heappush(pq, ans[-1] * j)
        return ans[-1]
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = [0] * (n + 1)
        ans[1] = 1
        p2 = p3 = p5 = 1
        for i in range(2, n + 1):
            n2, n3, n5 = ans[p2] * 2, ans[p3] * 3, ans[p5] * 5
            ans[i] = min(n2, n3, n5)
            if ans[i] == n2: p2 += 1
            if ans[i] == n3: p3 += 1
            if ans[i] == n5: p5 += 1
        return ans[n]
# leetcode submit region end(Prohibit modification and deletion)
print(Solution().nthUglyNumber(10))