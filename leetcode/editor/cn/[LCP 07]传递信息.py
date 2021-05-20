# 小朋友 A 在和 ta 的小伙伴们玩传信息游戏，游戏规则如下： 
# 
#  
#  有 n 名玩家，所有玩家编号分别为 0 ～ n-1，其中小朋友 A 的编号为 0 
#  每个玩家都有固定的若干个可传信息的其他玩家（也可能没有）。传信息的关系是单向的（比如 A 可以向 B 传信息，但 B 不能向 A 传信息）。 
#  每轮信息必须需要传递给另一个人，且信息可重复经过同一个人 
#  
# 
#  给定总玩家数 n，以及按 [玩家编号,对应可传递玩家编号] 关系组成的二维数组 relation。返回信息从小 A (编号 0 ) 经过 k 轮传递到编号
# 为 n-1 的小伙伴处的方案数；若不能到达，返回 0。 
# 
#  示例 1： 
# 
#  
#  输入：n = 5, relation = [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]], k = 3 
# 
#  输出：3 
# 
#  解释：信息从小 A 编号 0 处开始，经 3 轮传递，到达编号 4。共有 3 种方案，分别是 0->2->0->4， 0->2->1->4， 0->2->
# 3->4。 
#  
# 
#  示例 2： 
# 
#  
#  输入：n = 3, relation = [[0,2],[2,1]], k = 2 
# 
#  输出：0 
# 
#  解释：信息不能从小 A 处经过 2 轮传递到编号 2 
#  
# 
#  限制： 
# 
#  
#  2 <= n <= 10 
#  1 <= k <= 5 
#  1 <= relation.length <= 90, 且 relation[i].length == 2 
#  0 <= relation[i][0],relation[i][1] < n 且 relation[i][0] != relation[i][1] 
#  
#  👍 48 👎 0

from typing import List
import collections
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        g = collections.defaultdict(list)
        for u, v in relation:
            g[u].append(v)
        q = collections.deque([0])
        for i in range(k):
            for _ in range(len(q)):
                u = q.popleft()
                q.extend(g[u])
        return sum(i == n - 1 for i in q)

class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
       """
       深度优先搜索
       """
       def dfs(index, num):
            nonlocal ans
            if num == k:
                if index == n - 1:
                    ans += 1
                return
            for i in g[index]:
                dfs(i, num + 1)
       g = collections.defaultdict(list)
       for u, v in relation:
           g[u].append(v)
       ans = 0
       dfs(0, 0)
       return ans


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        """
        动态规划
        dp[i][j]表示第i轮传递给j的方案数，dp[0][0] = 1
        d[i][j] = sum(dp[i-1][k])  k -> j
        """
        dp = [[0] * n for _ in range(2)]
        dp[0][0] = 1
        for i in range(1, k + 1):
            dp[i & 1] = [0] * n
            for u, v in relation:
                dp[i & 1][v] += dp[(i - 1) & 1][u]
        return dp[k & 1][n-1]
# leetcode submit region end(Prohibit modification and deletion)
n = 5; relation = [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]]; k = 3
print(Solution().numWays(n, relation, k))