# 给你一个数组 routes ，表示一系列公交线路，其中每个 routes[i] 表示一条公交线路，第 i 辆公交车将会在上面循环行驶。 
# 
#  
#  例如，路线 routes[0] = [1, 5, 7] 表示第 0 辆公交车会一直按序列 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 
# -> ... 这样的车站路线行驶。 
#  
# 
#  现在从 source 车站出发（初始时不在公交车上），要前往 target 车站。 期间仅可乘坐公交车。 
# 
#  求出 最少乘坐的公交车数量 。如果不可能到达终点车站，返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：routes = [[1,2,7],[3,6,7]], source = 1, target = 6
# 输出：2
# 解释：最优策略是先乘坐第一辆公交车到达车站 7 , 然后换乘第二辆公交车到车站 6 。 
#  
# 
#  示例 2： 
# 
#  
# 输入：routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
# 输出：-1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= routes.length <= 500. 
#  1 <= routes[i].length <= 105 
#  routes[i] 中的所有值 互不相同 
#  sum(routes[i].length) <= 105 
#  0 <= routes[i][j] < 106 
#  0 <= source, target < 106 
#  
#  Related Topics 广度优先搜索 数组 哈希表 
#  👍 178 👎 0

from typing import List
import collections
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        st2car = collections.defaultdict(set)  # key=station,val={car_num...}
        g = collections.defaultdict(set) # 邻接表
        n = len(routes)
        # 记录每一个station属于哪些公交
        for car_num in range(n):
            for st in routes[car_num]:
                st2car[st].add(car_num)
        # 遍历每一个车站,将多条经过该车站的公交连边
        for car_num in range(n):
            for st in routes[car_num]:
                g[car_num].update(st2car[st])
        vis = set()
        q = collections.deque()
        for car_num in st2car[source]:
            q.append((car_num, 1))
            vis.add(car_num)
        while q:
            car_num, step = q.popleft()
            if car_num in st2car[target]:
                return step
            for i in g[car_num]:
                if i not in vis:
                    q.append((i, step + 1))
                    vis.add(i)
        return -1

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        n = len(routes)
        edge = [[False] * n for _ in range(n)]
        st2car = collections.defaultdict(set)
        for i in range(n):
            for st in routes[i]:
                for j in st2car[st]:
                    edge[i][j] = True
                    edge[j][i] = True
                st2car[st].add(i)
        visited = [False] * n
        q = collections.deque()
        for car in st2car[source]:
            q.append((car, 1))
            visited[car] = True
        while q:
            car, step = q.popleft()
            if car in st2car[target]:
                return step
            for other in range(n):
                if edge[car][other] and not visited[other]:
                    q.append((other, step + 1))
                    visited[other] = True
        return -1

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        n = len(routes)
        edge = [[False] * n for _ in range(n)]
        st2car = collections.defaultdict(list)
        for i in range(n):
            for st in routes[i]:
                for j in st2car[st]:
                    edge[i][j] = True
                    edge[j][i] = True
                st2car[st].append(i)
        q = collections.deque()
        dis = [-1] * n
        for car in st2car[source]:
            dis[car] = 1
            q.append(car)
        while q:
            car = q.popleft()
            for other in range(n):
                if edge[car][other] and dis[other] == -1:
                    q.append(other)
                    dis[other] = dis[car] + 1
        ans = float('inf')
        for car in st2car[target]:
            if dis[car] != -1:
                ans = min(ans, dis[car])
        return ans if ans < float('inf') else -1
# leetcode submit region end(Prohibit modification and deletion)
routes = [[1,2,7],[3,6,7]];source = 1; target = 6
# routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]; source = 15; target = 12
print(Solution().numBusesToDestination(routes, source, target))