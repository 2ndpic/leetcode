# 假设有从 1 到 N 的 N 个整数，如果从这 N 个数字中成功构造出一个数组，使得数组的第 i 位 (1 <= i <= N) 满足如下两个条件中的一个，
# 我们就称这个数组为一个优美的排列。条件： 
# 
#  
#  第 i 位的数字能被 i 整除 
#  i 能被第 i 位上的数字整除 
#  
# 
#  现在给定一个整数 N，请问可以构造多少个优美的排列？ 
# 
#  示例1: 
# 
#  
# 输入: 2
# 输出: 2
# 解释: 
# 
# 第 1 个优美的排列是 [1, 2]:
#   第 1 个位置（i=1）上的数字是1，1能被 i（i=1）整除
#   第 2 个位置（i=2）上的数字是2，2能被 i（i=2）整除
# 
# 第 2 个优美的排列是 [2, 1]:
#   第 1 个位置（i=1）上的数字是2，2能被 i（i=1）整除
#   第 2 个位置（i=2）上的数字是1，i（i=2）能被 1 整除
#  
# 
#  说明: 
# 
#  
#  N 是一个正整数，并且不会超过15。 
#  
#  Related Topics 深度优先搜索 回溯算法 
#  👍 133 👎 0
import collections
class Solution:
    def countArrangement(self, n: int) -> int:
        """
        回溯法。
        对排列的每个位置回溯，参数为start
        每个位置尝试[1,2,..,n]个数，检查之前是否使用过，对于此位置是否是优美的
        """
        def backtracking(start):
            if start == n + 1:
                ans[0] += 1
                return
            for i in range(1, n + 1):
                if seen[i] == 0 and (i % start == 0 or start % i == 0):
                    seen[i] = 1
                    backtracking(start + 1)
                    seen[i] = 0
        seen = [0] * (n + 1)
        ans = [0]
        backtracking(1)
        return ans[0]

class Solution:
    def countArrangement(self, n: int) -> int:
        """
        回溯法。
        对排列的每个位置回溯，参数为start
        每个位置尝试[1,2,..,n]个数，检查之前是否使用过，对于此位置是否是优美的
        """
        def backtracking(start):
            if start == n + 1:
                ans[0] += 1
                return
            for i in nums - visited:
                if i % start == 0 or start % i == 0:
                    visited.add(i)
                    backtracking(start + 1)
                    visited.remove(i)
        nums = set(range(1, n + 1))
        visited = set()
        ans = [0]
        backtracking(1)
        return ans[0]
class Solution:
    def countArrangement(self, n: int) -> int:
        """
        状态压缩
        因为最多15个数所以可以使用15位二进制数mask来表示。mask包含两个信息：使用数字的个数和分别是哪些数字。0表示未使用1表示使用。
        最终答案为sum(f[mask][i])
        f[mask][i]表示当前数字使用状态为mask，使用数字i的优美排列个数
        当 i % mask.count("1") == 0 or mask.count("1") % i == 0:
            f[mask][i] += f[mask\(i - 1)][j]    0<=j<n
        否则
            f[mask][i] = 0
        初始化f[0][0]=0
        """
        f = [[0] * (1 + n) for _ in range((1 << n))]
        f[0][0] = 1
        for mask in range(1, 1 << n):
            state = bin(mask).count("1")
            for i in range(1, n + 1):
                if mask & (1 << (i - 1)) and (i % state == 0 or state % i == 0):
                    for j in range(n + 1):
                        f[mask][i] += f[mask ^ (1 << (i - 1))][j]
        return sum(f[(1 << n) - 1][i] for i in range(1, n + 1))

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countArrangement(self, n: int) -> int:
        """
        官解状态压缩，时间复杂度更优秀.
        f[mask]表示状态为mask时的可行方案总数，答案为f[1<<n - 1]
        f[mask] = sum(f[mask ^ (1 << i)] if i ∈ mask and (i + 1 能被 num(mask) 整除 or num(mask) 能被 i + 1整除))
        """
        f = [1] + [0] * ((1 << n) - 1)
        for mask in range(1, 1 << n):
            num = bin(mask).count("1")
            for i in range(n):
                if mask & (1 << i) and ((i + 1) % num == 0 or num % (i + 1) == 0):
                    f[mask] += f[mask ^ (1 << i)]
        return f[(1 << n) - 1]
# leetcode submit region end(Prohibit modification and deletion)
print(Solution().countArrangement(2))
