# 我们得到了一副藏宝图，藏宝图显示，在一个迷宫中存在着未被世人发现的宝藏。 
# 
#  迷宫是一个二维矩阵，用一个字符串数组表示。它标识了唯一的入口（用 'S' 表示），和唯一的宝藏地点（用 'T' 表示）。但是，宝藏被一些隐蔽的机关保护了起
# 来。在地图上有若干个机关点（用 'M' 表示），只有所有机关均被触发，才可以拿到宝藏。 
# 
#  要保持机关的触发，需要把一个重石放在上面。迷宫中有若干个石堆（用 'O' 表示），每个石堆都有无限个足够触发机关的重石。但是由于石头太重，我们一次只能搬一
# 个石头到指定地点。 
# 
#  迷宫中同样有一些墙壁（用 '#' 表示），我们不能走入墙壁。剩余的都是可随意通行的点（用 '.' 表示）。石堆、机关、起点和终点（无论是否能拿到宝藏）也是
# 可以通行的。 
# 
#  我们每步可以选择向上/向下/向左/向右移动一格，并且不能移出迷宫。搬起石头和放下石头不算步数。那么，从起点开始，我们最少需要多少步才能最后拿到宝藏呢？如果
# 无法拿到宝藏，返回 -1 。 
# 
#  示例 1： 
# 
#  
#  输入： ["S#O", "M..", "M.T"] 
# 
#  输出：16 
# 
#  解释：最优路线为： S->O, cost = 4, 去搬石头 O->第二行的M, cost = 3, M机关触发 第二行的M->O, cost = 3, 
# 我们需要继续回去 O 搬石头。 O->第三行的M, cost = 4, 此时所有机关均触发 第三行的M->T, cost = 2，去T点拿宝藏。 总步数为16。
#  
#  
# 
#  示例 2： 
# 
#  
#  输入： ["S#O", "M.#", "M.T"] 
# 
#  输出：-1 
# 
#  解释：我们无法搬到石头触发机关 
#  
# 
#  示例 3： 
# 
#  
#  输入： ["S#O", "M.T", "M.."] 
# 
#  输出：17 
# 
#  解释：注意终点也是可以通行的。 
#  
# 
#  限制： 
# 
#  
#  1 <= maze.length <= 100 
#  1 <= maze[i].length <= 100 
#  maze[i].length == maze[j].length 
#  S 和 T 有且只有一个 
#  0 <= M的数量 <= 16 
#  0 <= O的数量 <= 40，题目保证当迷宫中存在 M 时，一定存在至少一个 O 。 
#  
#  Related Topics 位运算 广度优先搜索 数组 动态规划 状态压缩 矩阵 
#  👍 161 👎 0
from typing import List
from collections import deque
from collections import defaultdict
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimalSteps(self, maze: List[str]) -> int:
        """
        在最开始一定会从S-O-M，对于特定M来说，枚举O就可以计算出最短距离。这样就得到S到每一个M的最短距离
        假设已经从起点S到达某个M了，接下来去又去某个O点搬石头触发其他M，这是M-O-M‘路线。对于给定M’,O也是可以通过枚举固定下来
           即可以确定一个O，使得M-O-M'距离最短，同样可以记录下这个最短距离，即得到所有M-M'的最短距离
        我们需要所有M都被触发，M触发的顺序不同会导致行走的路径长度不同。假设一共有n个M
        d(i, j)表示第i个M和第j个M经过某一个O的最短距离，因为M不超过16个，所以可使用16位的二进制数表示
        第i位为1/0表示触发/未触发，记这个二进制数为mask
        定义f(mask, i)表示当前在第i个M处，触发状态为mask(包含i)的最小步数，如果当前mask代表的已触发集合为T，未触发集合为U-T
        则转移方程为：f(mask, i) = min(f(mask\i, j) + d(j, i))   j ∈ T
        可以预处理得到所有的d(j, i)，就可以达成O(1)的查询
        """
        def bfs(x, y):
            ret = [[-1] * n for _ in range(m)]
            ret[x][y] = 0
            q = deque([(x, y)])
            while q:
                x, y = q.popleft()
                for dx, dy in direction:
                    nx, ny = x + dx, y + dy
                    if in_bound(nx, ny) and maze[nx][ny] != "#" and ret[nx][ny] != -1:
                        ret[nx][ny] = ret[x][y] + 1
                        q.append((nx, ny))
            return ret

        direction = ((1, 0), (-1, 0), (0, -1), (0, 1))
        m, n = len(maze), len(maze[0])
        in_bound = lambda x, y: 0 <= x < m and 0 <= y < n

        buttons, stones, start, end = [], [], None, None
        for i in range(m):
            for j in range(n):
                if maze[i][j] == "M": buttons.append((i, j))
                elif maze[i][j] == "O": stones.append((i, j))
                elif maze[i][j] == "S": start = (i, j)
                elif maze[i][j] == "T": end = (i, j)
        nb, ns = len(buttons), len(stones)
        start_dist = bfs(*start)
        # 没有机关
        if not nb: return start_dist[end[0]][end[1]]
        # 从某个机关到其他机关/起点与终点的最短距离
        dist = [[-1] * (nb + 2) for _ in range(nb)]
        # 中间结果
        dd = defaultdict(list)
        for i in range(nb):
            d = bfs(*buttons[i])
            dd[i] = d
            # 某个点到终点不需要拿石头
            dist[i][nb + 1] = d[end[0]][end[1]]

        for i in range(nb):
            tmp = float('inf')
            d = dd[i]
            for midx, midy in stones:
                if start_dist[midx][midy] != -1 and [midx][midy] != -1:
                    tmp = min(tmp, start_dist[midx][midy] + d[midx][midy])














# leetcode submit region end(Prohibit modification and deletion)
