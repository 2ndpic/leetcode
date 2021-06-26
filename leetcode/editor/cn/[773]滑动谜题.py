# 在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示. 
# 
#  一次移动定义为选择 0 与一个相邻的数字（上下左右）进行交换. 
# 
#  最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。 
# 
#  给出一个谜板的初始状态，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。 
# 
#  示例： 
# 
#  
# 输入：board = [[1,2,3],[4,0,5]]
# 输出：1
# 解释：交换 0 和 5 ，1 步完成
#  
# 
#  
# 输入：board = [[1,2,3],[5,4,0]]
# 输出：-1
# 解释：没有办法完成谜板
#  
# 
#  
# 输入：board = [[4,1,2],[5,0,3]]
# 输出：5
# 解释：
# 最少完成谜板的最少移动次数是 5 ，
# 一种移动路径:
# 尚未移动: [[4,1,2],[5,0,3]]
# 移动 1 次: [[4,1,2],[0,5,3]]
# 移动 2 次: [[0,1,2],[4,5,3]]
# 移动 3 次: [[1,0,2],[4,5,3]]
# 移动 4 次: [[1,2,0],[4,5,3]]
# 移动 5 次: [[1,2,3],[4,5,0]]
#  
# 
#  
# 输入：board = [[3,2,4],[1,5,0]]
# 输出：14
#  
# 
#  提示： 
# 
#  
#  board 是一个如上所述的 2 x 3 的数组. 
#  board[i][j] 是一个 [0, 1, 2, 3, 4, 5] 的排列. 
#  
#  Related Topics 广度优先搜索 数组 矩阵 
#  👍 163 👎 0

from typing import List
import collections
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = "123450"
        board = "".join(str(i) for i in board[0] + board[1])
        q = collections.deque([board])
        ans = 0
        visited = {board}
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == target: return ans
                index_0 = cur.index("0")
                for d in (1, -1, 3, -3):
                    if (index_0 == 2 and d == 1) or (index_0 == 3 and d == -1): continue
                    new_0 = index_0 + d
                    if 0 <= new_0 < 6:
                        tmp = list(cur)
                        tmp[index_0], tmp[new_0] = tmp[new_0], tmp[index_0]
                        tmp = "".join(tmp)
                        if tmp not in visited:
                            q.append(tmp)
                            visited.add(tmp)
            ans += 1
        return -1
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        """
        双向BFS
        """
        def update(q, cur, other):
            state = q.popleft()
            x = state.index("0")
            for y in NEIGHBORS[x]:
                tmp = list(state)
                tmp[x], tmp[y] = tmp[y], tmp[x]
                tmp = "".join(tmp)
                if tmp in cur: continue
                if tmp in other: return cur[state] + 1 + other[tmp]
                else:
                    cur[tmp] = cur[state] + 1
                    q.append(tmp)
            return -1

        target = "123450"
        board = "".join(str(i) for i in board[0] + board[1])
        if board == target: return 0
        NEIGHBORS = ((1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4))
        q1, q2 = collections.deque([board]), collections.deque([target])
        m1, m2 = {board: 0}, {target: 0}
        while q1 and q2:
            if len(q1) <= len(q2):
                t = update(q1, m1, m2)
            else:
                t = update(q2, m2, m1)
            if t != -1: return t
        return -1
# leetcode submit region end(Prohibit modification and deletion)
board = [[1,2,3],[4,0,5]]
# board = [[1,2,3],[5,4,0]]
# board = [[4,1,2],[5,0,3]]
# board = [[3,2,4],[1,5,0]]
print(Solution().slidingPuzzle(board))