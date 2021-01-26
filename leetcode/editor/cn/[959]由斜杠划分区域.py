# 在由 1 x 1 方格组成的 N x N 网格 grid 中，每个 1 x 1 方块由 /、\ 或空格构成。这些字符会将方块划分为一些共边的区域。 
# 
#  （请注意，反斜杠字符是转义的，因此 \ 用 "\\" 表示。）。 
# 
#  返回区域的数目。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：
# [
#   " /",
#   "/ "
# ]
# 输出：2
# 解释：2x2 网格如下：
#  
# 
#  示例 2： 
# 
#  输入：
# [
#   " /",
#   "  "
# ]
# 输出：1
# 解释：2x2 网格如下：
#  
# 
#  示例 3： 
# 
#  输入：
# [
#   "\\/",
#   "/\\"
# ]
# 输出：4
# 解释：（回想一下，因为 \ 字符是转义的，所以 "\\/" 表示 \/，而 "/\\" 表示 /\。）
# 2x2 网格如下：
#  
# 
#  示例 4： 
# 
#  输入：
# [
#   "/\\",
#   "\\/"
# ]
# 输出：5
# 解释：（回想一下，因为 \ 字符是转义的，所以 "/\\" 表示 /\，而 "\\/" 表示 \/。）
# 2x2 网格如下：
#  
# 
#  示例 5： 
# 
#  输入：
# [
#   "//",
#   "/ "
# ]
# 输出：3
# 解释：2x2 网格如下：
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= grid.length == grid[0].length <= 30 
#  grid[i][j] 是 '/'、'\'、或 ' '。 
#  
#  Related Topics 深度优先搜索 并查集 图 
#  👍 139 👎 0
from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
def find(u, parents):
    if u != parents[u]:
        parents[u] = find(parents[u], parents)
    return parents[u]
def union(u, v, parents, ranks):
    pu, pv = find(u, parents), find(v, parents)
    if pu == pv:
        return False
    if ranks[pu] > ranks[pv]:
        parents[pv] = pu
    elif ranks[pv] > ranks[pu]:
        parents[pu] = pv
    else:
        parents[pv] = pu
        ranks[pu] += 1
    return True
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parents = [i for i in range(n*n*2)]
        ranks = [0 for _ in range(n*n*2)]
        for i in range(n):
            for j in range(n):
                front = (i * n + j) * 2
                back = front + 1
                left = front - 1 if j > 0 else None
                right = back + 1 if j < n-1 else None
                if left is not None:
                    union(front, left, parents, ranks)
                if right is not None:
                    union(back, right, parents, ranks)
                if i-1 < 0:
                    up = None
                elif grid[i-1][j] == "/":
                    up = ((i - 1) * n + j) * 2 + 1
                else:
                    up = ((i - 1) * n + j) * 2
                if i+1 >= n:
                    down = None
                elif grid[i+1][j] == "/":
                    down = ((i + 1) * n + j) * 2
                else:
                    down = ((i + 1) * n + j) * 2 + 1
                if grid[i][j] == "\\":
                    if down is not None:
                        union(front, down, parents, ranks)
                    if up is not None:
                        union(back, up, parents ,ranks)

                elif grid[i][j] == "/":
                    if up is not None:
                        union(front, up, parents, ranks)
                    if down is not None:
                        union(back, down, parents, ranks)
                else:
                    if down is not None:
                        union(front, down, parents, ranks)
                    if up is not None:
                        union(back, up, parents ,ranks)
                    union(front, back, parents, ranks)
        res = set()
        for i in range(n*n*2):
            res.add(find(i, parents))
        return len(res)
        
# leetcode submit region end(Prohibit modification and deletion)
grid = ["//",
  "/ "]
print(Solution().regionsBySlashes(grid))