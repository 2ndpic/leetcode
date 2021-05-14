# 有一个长度为 arrLen 的数组，开始有一个指针在索引 0 处。 
# 
#  每一步操作中，你可以将指针向左或向右移动 1 步，或者停在原地（指针不能被移动到数组范围外）。 
# 
#  给你两个整数 steps 和 arrLen ，请你计算并返回：在恰好执行 steps 次操作以后，指针仍然指向索引 0 处的方案数。 
# 
#  由于答案可能会很大，请返回方案数 模 10^9 + 7 后的结果。 
# 
#  
# 
#  示例 1： 
# 
#  输入：steps = 3, arrLen = 2
# 输出：4
# 解释：3 步后，总共有 4 种不同的方法可以停在索引 0 处。
# 向右，向左，不动
# 不动，向右，向左
# 向右，不动，向左
# 不动，不动，不动
#  
# 
#  示例 2： 
# 
#  输入：steps = 2, arrLen = 4
# 输出：2
# 解释：2 步后，总共有 2 种不同的方法可以停在索引 0 处。
# 向右，向左
# 不动，不动
#  
# 
#  示例 3： 
# 
#  输入：steps = 4, arrLen = 2
# 输出：8
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= steps <= 500 
#  1 <= arrLen <= 10^6 
#  
#  Related Topics 动态规划 
#  👍 124 👎 0

import functools
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @functools.lru_cache(None)
        def f(index, rest_steps):
            """
            在rest_steps下，从index出发到0的路径数
            """
            if index < 0 or index >= arrLen: return 0
            if rest_steps == 0:
                return int(index == 0)
            return (f(index + 1, rest_steps - 1) + f(index - 1, rest_steps - 1) + f(index, rest_steps - 1)) % mod
        mod = 10 ** 9 + 7
        return f(0, steps)

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        """
        f[i][j]表示剩余操作数为i，所在位置为j的回到0的所有方案数
        初始化:
            起始位置为0，操作次数为step，即有初始条件f[step][0]=1,f[0][0]则是最终答案
        f[i][j]可以由下面三种状态转移过来：
        - 原地不动，消耗一次操作，此时由f[i+1][j]转移而来
        - 右走一步，消耗一次操作，此时由f[i+1][j-1]转移来
        - 左走一步，消耗一次操作，此时由f[i+1][j+1]转移来

        因为最终要回到下标0位置，最远只能到达位置为step/2(再远就回不来了)。所以可以确定index位置
        """
        max_index, mod = min(steps // 2, arrLen - 1), 10 ** 9 + 7
        f = [[0] * (max_index + 1) for _ in range(steps + 1)]
        f[steps][0] = 1
        for i in range(steps - 1, -1, -1):
            for j in range(0, max_index + 1):
                f[i][j] += f[i + 1][j]
                f[i][j] += f[i + 1][j - 1] if j - 1 >= 0 else 0
                f[i][j] += f[i + 1][j + 1] if j + 1 <= max_index else 0
                f[i][j] %= mod
        return f[0][0]

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        """
        优化
        f[i]只依赖于f[i+1]的状态
        而且随着可操作次数的减少，可到达的最远位置下标也在缩小。从f[0][0]倒推的话
        会发现，可达到的最远位置等于可操作次数
        所以可以从两者取最小值，能够有效减少无效状态的计算。
        """
        max_index, mod = min(steps // 2, arrLen - 1), 10 ** 9 + 7
        f = [[0] * (max_index + 1) for _ in range(steps + 1)]
        f[steps][0] = 1
        for i in range(steps - 1, -1, -1):
            edge = min(i, max_index)
            for j in range(0, edge + 1):
                f[i][j] += f[i + 1][j]
                f[i][j] += f[i + 1][j - 1] if j - 1>= 0 else 0
                f[i][j] += f[i + 1][j + 1] if j + 1 <= max_index else 0
                f[i][j] %= mod
        return f[0][0]

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        """
        优化
        滚动数组优化
        """
        max_index, mod = min(steps // 2, arrLen - 1), 10 ** 9 + 7
        f = [[0] * (max_index + 1) for _ in range(2)]
        f[steps & 1][0] = 1
        for i in range(steps - 1, -1, -1):
            edge = min(i, max_index)
            a, b = i & 1, (i + 1) & 1
            for j in range(0, edge + 1):
                f[a][j] = 0
                f[a][j] += f[b][j]
                f[a][j] += f[b][j - 1] if j - 1 >= 0 else 0
                f[a][j] += f[b][j + 1] if j + 1 <= max_index else 0
                f[a][j] %= mod
        return f[0][0]

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        """
        优化
        另外一种状态定义
        f[i][j]表示消耗i次操作，到达位置j的方案数.f[0][0] = 1, f[0][j] = 0
        f[i][j] = f[i-1][j] + f[i-1][j-1] + f[i-1][j+1]
        """
        max_index, mod = min(steps // 2, arrLen - 1), 10 ** 9 + 7
        f = [[0] * (max_index + 1) for _ in range(2)]
        f[0][0] = 1
        for i in range(1, steps + 1):
            a, b = i & 1, (i - 1) & 1
            for j in range(0, min(i, max_index) + 1):
                f[a][j] = f[b][j]
                f[a][j] += f[b][j - 1] if j - 1 >= 0 else 0
                f[a][j] += f[b][j + 1] if j + 1 <= max_index else 0
                f[a][j] %= mod

        return f[steps & 1][0]



        
# leetcode submit region end(Prohibit modification and deletion)
steps = 3;arrLen = 2 # 4
steps = 4;arrLen = 2 # 8
print(Solution().numWays(steps, arrLen))