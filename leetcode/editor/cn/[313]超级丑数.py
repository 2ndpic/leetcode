# 超级丑数 是一个正整数，并满足其所有质因数都出现在质数数组 primes 中。 
# 
#  给你一个整数 n 和一个整数数组 primes ，返回第 n 个 超级丑数 。 
# 
#  题目数据保证第 n 个 超级丑数 在 32-bit 带符号整数范围内。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 12, primes = [2,7,13,19]
# 输出：32 
# 解释：给定长度为 4 的质数数组 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,
# 28,32] 。 
# 
#  示例 2： 
# 
#  
# 输入：n = 1, primes = [2,3,5]
# 输出：1
# 解释：1 不含质因数，因此它的所有质因数都在质数数组 primes = [2,3,5] 中。
#  
#  
# 
#  
#  
#  
#  提示： 
# 
#  
#  1 <= n <= 106 
#  1 <= primes.length <= 100 
#  2 <= primes[i] <= 1000 
#  题目数据 保证 primes[i] 是一个质数 
#  primes 中的所有值都 互不相同 ，且按 递增顺序 排列 
#  
#  
#  
#  
#  Related Topics 数组 哈希表 数学 动态规划 堆（优先队列） 
#  👍 226 👎 0
from typing import List
import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        seen = {1}
        heap = [1]
        for i in range(n):
            ugly = heapq.heappop(heap)
            for prime in primes:
                nxt = ugly * prime
                if nxt not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)
        return ugly

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        m = len(primes)
        pointers = [1] * m
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[pointers[j]] * primes[j] for j in range(m))
            for j in range(m):
                if dp[i] == dp[pointers[j]] * primes[j]:
                    pointers[j] += 1
        return dp[n]
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        m = len(primes)
        dp = [1] * n
        # 存放三元组(val, p, idx) dp[idx] * primes[p] = val
        pq = [(val, p, 0) for p, val in enumerate(primes)]
        for i in range(1, n):
            dp[i] = pq[0][0]
            while pq and pq[0][0] == dp[i]:
                _, p, idx = heapq.heappop(pq)
                heapq.heappush(pq, (dp[idx + 1] * primes[p], p, idx + 1))
        return dp[-1]
# leetcode submit region end(Prohibit modification and deletion)
n = 12; primes = [2,7,13,19]
print(Solution().nthSuperUglyNumber(n, primes))