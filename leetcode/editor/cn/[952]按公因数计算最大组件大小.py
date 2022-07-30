from typing import List
from collections import Counter

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv: return
            if ranks[pu] < ranks[pv]:
                parents[pu] = pv
            elif ranks[pv] < ranks[pu]:
                parents[pv] = pu
            else:
                parents[pv] = pu
                ranks[pu] += 1
        def find(u):
            if parents[u] != u:
                parents[u] = find(parents[u])
            return parents[u]

        max_num = max(nums)
        parents = [i for i in range(max_num + 1)]
        ranks = [0] * (max_num + 1)

        for num in nums:
            i = 2
            while i * i <= num:
                if num % i == 0:
                    union(num, i)
                    union(num, num // i)
                i += 1
        return max(Counter(find(num) for num in nums).values())

N = 10 ** 5
is_prime = [True] * (N + 1)
primes = []
for i in range(2, N + 1):
    if is_prime: primes.append(i)
    for prime in primes:
        if prime * i > N: break
        is_prime[i * prime] = False
        if i % prime == 0: break
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv: return
            if ranks[pu] < ranks[pv]:
                parents[pu] = pv
            elif ranks[pv] < ranks[pu]:
                parents[pv] = pu
            else:
                parents[pv] = pu
                ranks[pu] += 1

        def find(u):
            if parents[u] != u:
                parents[u] = find(parents[u])
            return parents[u]

        max_num = max(nums)
        parents = [i for i in range(max_num + 1)]
        ranks = [0] * (max_num + 1)
        for num in nums:
            i = num
            for prime in primes:
                if prime * prime > i: break
                if i % prime == 0:
                    union(num, prime)
                    while i % prime == 0:
                        i //= prime
            if i > 1: union(num, i)
        return max(Counter(find(num) for num in nums).values())

# leetcode submit region end(Prohibit modification and deletion)
nums = [4,6,15,35]
print(Solution().largestComponentSize(nums))