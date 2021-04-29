# 一只青蛙想要过河。 假定河流被等分为若干个单元格，并且在每一个单元格内都有可能放有一块石子（也有可能没有）。 青蛙可以跳上石子，但是不可以跳入水中。 
# 
#  给你石子的位置列表 stones（用单元格序号 升序 表示）， 请判定青蛙能否成功过河（即能否在最后一步跳至最后一块石子上）。 
# 
#  开始时， 青蛙默认已站在第一块石子上，并可以假定它第一步只能跳跃一个单位（即只能从单元格 1 跳至单元格 2 ）。 
# 
#  如果青蛙上一步跳跃了 k 个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1 个单位。 另请注意，青蛙只能向前方（终点的方向）跳跃。
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：stones = [0,1,3,5,6,8,12,17]
# 输出：true
# 解释：青蛙可以成功过河，按照如下方案跳跃：跳 1 个单位到第 2 块石子, 然后跳 2 个单位到第 3 块石子, 接着 跳 2 个单位到第 4 块石子, 然
# 后跳 3 个单位到第 6 块石子, 跳 4 个单位到第 7 块石子, 最后，跳 5 个单位到第 8 个石子（即最后一块石子）。 
# 
#  示例 2： 
# 
#  
# 输入：stones = [0,1,2,3,4,8,9,11]
# 输出：false
# 解释：这是因为第 5 和第 6 个石子之间的间距太大，没有可选的方案供青蛙跳跃过去。 
# 
#  
# 
#  提示： 
# 
#  
#  2 <= stones.length <= 2000 
#  0 <= stones[i] <= 231 - 1 
#  stones[0] == 0 
#  
#  Related Topics 动态规划 
#  👍 199 👎 0

from typing import List
import functools
import bisect
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        """
        f(i, j)上一步跳了 j 步，来到当前的 i 位置，基于此，能否最后抵达终点。
        """
        @functools.lru_cache(None)
        def f(i, j):
            if i == len(stones) - 1: return True
            if j == 0: steps = [1]
            elif j == 1: steps = [1, 2]
            else: steps = [j - 1, j, j + 1]
            for step in steps:
                idx = bisect.bisect_left(stones, stones[i] + step)
                if idx < len(stones) and (stones[idx] == stones[i] + step) and f(idx, step):
                    return True
            return False
        return f(0, 0)

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        """
        f(i, j)上一步跳了 j 步，来到当前的 i 位置，基于此，能否最后抵达终点。
        """
        @functools.lru_cache(None)
        def f(i, j):
            if i == len(stones) - 1: return True
            for k in [-1, 0, 1]:
                step = j + k
                if step <= 0 or stones[i] + step not in val2idx: continue
                idx = val2idx[stones[i] + step]
                if f(idx, step):
                    return True
            return False
        val2idx = {val:idx for idx, val in enumerate(stones)}
        return f(0, 0)

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        """
        考虑动态规划
        f[i][j]:表示上一步跳了 j 步，来到当前的 i 位置,是否能达到最后一个石头
        则第一维度为数组stones长度，第二维度是上一步的跳跃不长，也不会超过stones长度
        对于f[i][j]是否为真，取决于上衣位置k的状态值，结合每次步长的变化为[-1, 0, 1]可知：
        - 可从f[k][j - 1]状态而来，先经过j - 1步跳到k，再在原步长的基础上 + 1，跳到i位置
        - 可从f[k][j]状态而来，先经过j步跳到k，再在原步长，跳到i位置
        - 可从f[k][j + 1]状态而来，先经过j + 1步跳到k，再在原步长的基础上 - 1，跳到i位置

        只要以上三种情况为任一为真，则f[i][j]为真
        初始状态：f[1][1]=true,任意到达终点的路径必然通过f[1][1]
        """
        n = len(stones)
        f = [[False] * n for _ in range(n)]
        if stones[1] != 1: return False
        f[1][1] = True
        for i in range(2, n):
            for k in range(1, i):
                j = stones[i] - stones[k]
                if j <= k + 1:  # 最多跳k + 1步到达i位置
                    f[i][j] = f[k][j - 1] or f[k][j] or f[k][j + 1]

        return True in f[n - 1]

# leetcode submit region end(Prohibit modification and deletion)
stones = [0,1,3,5,6,8,12,17]
print(Solution().canCross(stones))