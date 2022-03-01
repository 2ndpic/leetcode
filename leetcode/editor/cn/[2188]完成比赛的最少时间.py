# 给你一个下标从 0 开始的二维整数数组 tires ，其中 tires[i] = [fi, ri] 表示第 i 种轮胎如果连续使用，第 x 圈需要耗时 
# fi * ri⁽ˣ⁻¹⁾ 秒。 
# 
#  
#  比方说，如果 fi = 3 且 ri = 2 ，且一直使用这种类型的同一条轮胎，那么该轮胎完成第 1 圈赛道耗时 3 秒，完成第 2 圈耗时 3 * 2 
# = 6 秒，完成第 3 圈耗时 3 * 2² = 12 秒，依次类推。 
#  
# 
#  同时给你一个整数 changeTime 和一个整数 numLaps 。 
# 
#  比赛总共包含 numLaps 圈，你可以选择 任意 一种轮胎开始比赛。每一种轮胎都有 无数条 。每一圈后，你可以选择耗费 changeTime 秒 换成 
# 任意一种轮胎（也可以换成当前种类的新轮胎）。 
# 
#  请你返回完成比赛需要耗费的 最少 时间。 
# 
#  
# 
#  示例 1： 
# 
#  输入：tires = [[2,3],[3,4]], changeTime = 5, numLaps = 4
# 输出：21
# 解释：
# 第 1 圈：使用轮胎 0 ，耗时 2 秒。
# 第 2 圈：继续使用轮胎 0 ，耗时 2 * 3 = 6 秒。
# 第 3 圈：耗费 5 秒换一条新的轮胎 0 ，然后耗时 2 秒完成这一圈。
# 第 4 圈：继续使用轮胎 0 ，耗时 2 * 3 = 6 秒。
# 总耗时 = 2 + 6 + 5 + 2 + 6 = 21 秒。
# 完成比赛的最少时间为 21 秒。
#  
# 
#  示例 2： 
# 
#  输入：tires = [[1,10],[2,2],[3,4]], changeTime = 6, numLaps = 5
# 输出：25
# 解释：
# 第 1 圈：使用轮胎 1 ，耗时 2 秒。
# 第 2 圈：继续使用轮胎 1 ，耗时 2 * 2 = 4 秒。
# 第 3 圈：耗时 6 秒换一条新的轮胎 1 ，然后耗时 2 秒完成这一圈。
# 第 4 圈：继续使用轮胎 1 ，耗时 2 * 2 = 4 秒。
# 第 5 圈：耗时 6 秒换成轮胎 0 ，然后耗时 1 秒完成这一圈。
# 总耗时 = 2 + 4 + 6 + 2 + 4 + 6 + 1 = 25 秒。
# 完成比赛的最少时间为 25 秒。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= tires.length <= 10⁵ 
#  tires[i].length == 2 
#  1 <= fi, changeTime <= 10⁵ 
#  2 <= ri <= 10⁵ 
#  1 <= numLaps <= 1000 
#  
#  👍 36 👎 0
from typing import List
from heapq import heapify, heappush, heappop
class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        min_sec = [float('inf')] * 18
        for f, r in tires:
            cur, x, total = f, 1, 0
            while cur <= changeTime + f:
                total += cur
                min_sec[x] = min(min_sec[x], total)
                x += 1
                cur *= r


        f = [0] * (numLaps + 1)
        for i in range(1, numLaps + 1):
            f[i] = min(f[i - j] + changeTime + min_sec[j] for j in range(1, min(i + 1, 18)))
        return f[numLaps] - changeTime

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        # 不换轮子 连走i轮需要的最短时间
        minCost = [float('inf')] * 18
        for f, r in tires:
            cost, cur, idx = 0, f, 1
            while cur <= f + changeTime:
                cost += cur
                minCost[idx] = min(minCost[idx], cost)
                cur *= r
                idx += 1

        # dijk求最短路
        pq = [(minCost[i], i) for i in range(1, min(numLaps + 1, 18))]

        dist = [float('inf')] * (numLaps + 1)
        while pq:
            cost, step = heappop(pq)
            if step == numLaps:
                return cost
            for i in range(1, min(numLaps - step + 1, 18)):
                nextCost = cost + changeTime + minCost[i]
                if nextCost < dist[step + i]:
                    dist[step + i] = nextCost
                    heappush(pq, (nextCost, step + i))

        return -1
# leetcode submit region end(Prohibit modification and deletion)