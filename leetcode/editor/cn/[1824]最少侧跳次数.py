# 给你一个长度为 n 的 3 跑道道路 ，它总共包含 n + 1 个 点 ，编号为 0 到 n 。一只青蛙从 0 号点第二条跑道 出发 ，它想要跳到点 n 处
# 。然而道路上可能有一些障碍。 
# 
#  给你一个长度为 n + 1 的数组 obstacles ，其中 obstacles[i] （取值范围从 0 到 3）表示在点 i 处的 obstacles
# [i] 跑道上有一个障碍。如果 obstacles[i] == 0 ，那么点 i 处没有障碍。任何一个点的三条跑道中 最多有一个 障碍。 
# 
#  
#  比方说，如果 obstacles[2] == 1 ，那么说明在点 2 处跑道 1 有障碍。 
#  
# 
#  这只青蛙从点 i 跳到点 i + 1 且跑道不变的前提是点 i + 1 的同一跑道上没有障碍。为了躲避障碍，这只青蛙也可以在 同一个 点处 侧跳 到 另外
# 一条 跑道（这两条跑道可以不相邻），但前提是跳过去的跑道该点处没有障碍。 
# 
#  
#  比方说，这只青蛙可以从点 3 处的跑道 3 跳到点 3 处的跑道 1 。 
#  
# 
#  这只青蛙从点 0 处跑道 2 出发，并想到达点 n 处的 任一跑道 ，请你返回 最少侧跳次数 。 
# 
#  注意：点 0 处和点 n 处的任一跑道都不会有障碍。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：obstacles = [0,1,2,3,0]
# 输出：2 
# 解释：最优方案如上图箭头所示。总共有 2 次侧跳（红色箭头）。
# 注意，这只青蛙只有当侧跳时才可以跳过障碍（如上图点 2 处所示）。
#  
# 
#  示例 2： 
# 
#  
# 输入：obstacles = [0,1,1,3,3,0]
# 输出：0
# 解释：跑道 2 没有任何障碍，所以不需要任何侧跳。
#  
# 
#  示例 3： 
# 
#  
# 输入：obstacles = [0,2,1,0,3,0]
# 输出：2
# 解释：最优方案如上图所示。总共有 2 次侧跳。
#  
# 
#  
# 
#  提示： 
# 
#  
#  obstacles.length == n + 1 
#  1 <= n <= 5 * 105 
#  0 <= obstacles[i] <= 3 
#  obstacles[0] == obstacles[n] == 0 
#  
#  Related Topics 广度优先搜索 动态规划 
#  👍 13 👎 0

from typing import List
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        """
        dp[i][j]表示到达第i处j跑道最少跳跃次数
        """
        dp = [[10 ** 9] * 4 for _ in range(len(obstacles))]
        dp[0][1], dp[0][2], dp[0][3] = 1, 0, 1
        for i in range(1, len(obstacles)):
            if obstacles[i] != 1: dp[i][1] = dp[i - 1][1]
            if obstacles[i] != 2: dp[i][2] = dp[i - 1][2]
            if obstacles[i] != 3: dp[i][3] = dp[i - 1][3]
            if obstacles[i] != 1: dp[i][1] = min(dp[i][1], dp[i][2] + 1, dp[i][3] + 1)
            if obstacles[i] != 2: dp[i][2] = min(dp[i][2], dp[i][1] + 1, dp[i][3] + 1)
            if obstacles[i] != 3: dp[i][3] = min(dp[i][3], dp[i][1] + 1, dp[i][2] + 1)
        return min(dp[len(obstacles) - 1])
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        """
        贪心
        """
        n, ans, cur_path = len(obstacles), 0, 2
        for i in range(1, n):
            if obstacles[i] == cur_path:



# leetcode submit region end(Prohibit modification and deletion)
obstacles = [0,1,1,3,3,0]
obstacles = [0,1,2,3,0]
obstacles = [0,2,1,0,3,0]
print(Solution().minSideJumps(obstacles))
"""
class Solution:
    def minSideJumps(self, obstacles):
        length = len(obstacles)
        ret = 0
        num = 2
        choices = {1, 2, 3}
        for i in range(length - 1):
            if obstacles[i + 1] == num:
                _choice = choices - {num, obstacles[i]}
                if len(_choice) == 1:
                    num = _choice.pop()
                    ret += 1
                else:
                    tmp = {}
                    for j in _choice:
                        n = i
                        while n < length and obstacles[n] != j:
                            n += 1
                        tmp[n] = j
                    num = tmp[max(tmp)]
                    ret += 1
        return ret
        
        
青蛙初始入赛道数记为num，然后for循环一直前行
当判断i + 1 等于num时，我们需要考虑两点
如果位置是否有障碍(因为走到了当前所有障碍肯定不是num)，然后只有三条赛道，所以此时求差集后直接次数加一继续即可
4 如果当前位置无障碍，这需要贪心思维，获取除num以外的两个赛道，谁能下一次走的更远，选择最远的跳过去
重复2,3,4，完成解题...
"""
