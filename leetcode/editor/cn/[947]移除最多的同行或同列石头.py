# n 块石头放置在二维平面中的一些整数坐标点上。每个坐标点上最多只能有一块石头。 
# 
#  如果一块石头的 同行或者同列 上有其他石头存在，那么就可以移除这块石头。 
# 
#  给你一个长度为 n 的数组 stones ，其中 stones[i] = [xi, yi] 表示第 i 块石头的位置，返回 可以移除的石子 的最大数量。 
# 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# 输出：5
# 解释：一种移除 5 块石头的方法如下所示：
# 1. 移除石头 [2,2] ，因为它和 [2,1] 同行。
# 2. 移除石头 [2,1] ，因为它和 [0,1] 同列。
# 3. 移除石头 [1,2] ，因为它和 [1,0] 同行。
# 4. 移除石头 [1,0] ，因为它和 [0,0] 同列。
# 5. 移除石头 [0,1] ，因为它和 [0,0] 同行。
# 石头 [0,0] 不能移除，因为它没有与另一块石头同行/列。 
# 
#  示例 2： 
# 
#  
# 输入：stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# 输出：3
# 解释：一种移除 3 块石头的方法如下所示：
# 1. 移除石头 [2,2] ，因为它和 [2,0] 同行。
# 2. 移除石头 [2,0] ，因为它和 [0,0] 同列。
# 3. 移除石头 [0,2] ，因为它和 [0,0] 同行。
# 石头 [0,0] 和 [1,1] 不能移除，因为它们没有与另一块石头同行/列。 
# 
#  示例 3： 
# 
#  
# 输入：stones = [[0,0]]
# 输出：0
# 解释：[0,0] 是平面上唯一一块石头，所以不可以移除它。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= stones.length <= 1000 
#  0 <= xi, yi <= 10^4
#  不会有两块石头放在同一个坐标点上 
#  
#  Related Topics 深度优先搜索 并查集 
#  👍 121 👎 0
# class Solution:
#     def removeStones(self, stones: List[List[int]]) -> int:
#         row_cols = defaultdict(set)
#         col_rows = defaultdict(set)
#         n_rows = 0
#         for row, col in stones:
#             row_cols[row] |= {col}
#             col_rows[col] |= {row}
#             n_rows = max(row, n_rows)
#
#         res = 0
#         for i in range(n_rows+1):
#             if i not in row_cols:
#                 continue
#             res += 1
#             stack = {i}
#             while stack:
#                 row = stack.pop()
#                 for col in row_cols[row]:
#                     if col in col_rows:
#                         stack |= col_rows[col]
#                         del col_rows[col]
#
#                 del row_cols[row]
#         return len(stones) - res
from typing import List
import collections
# leetcode submit region begin(Prohibit modification and deletion)
def dfs(start, g, visited):
    visited.add(start)
    for i in g[start]:
        if i not in visited:
            dfs(i, g, visited)

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        rec = collections.defaultdict(list)
        for i, (x, y) in enumerate(stones):
            rec[x].append(i)
            rec[y+10001].append(i)
        for ss in rec.values():
            for i in range(1, len(ss)):
                g[ss[i-1]].append(ss[i])
                g[ss[i]].append(ss[i-1])

        visited = set()
        num = 0
        for i in range(len(stones)):
            if i not in visited:
                num += 1
                dfs(i, g, visited)

        return len(stones) - num

# leetcode submit region end(Prohibit modification and deletion)
stones = [[0,0], [1,1]]
print(Solution().removeStones(stones))