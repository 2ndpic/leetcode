# 设计一种算法，打印 N 皇后在 N × N 棋盘上的各种摆法，其中每个皇后都不同行、不同列，也不在对角线上。这里的“对角线”指的是所有的对角线，不只是平分整
# 个棋盘的那两条对角线。 
# 
#  注意：本题相对原题做了扩展 
# 
#  示例: 
# 
#   输入：4
#  输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
#  解释: 4 皇后问题存在如下两个不同的解法。
# [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
# 
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
#  
#  Related Topics 回溯算法 
#  👍 75 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtracking(start, path):
            if start == n:
                ans.append(path)
                return
            for i in range(n):
                if col[i] or diag[n - start + i] or ant_diag[start + i]: continue
                col[i] = True
                diag[n - start + i] = True
                ant_diag[start + i] = True
                backtracking(start + 1, path + [path_memo[i]])
                col[i] = False
                diag[n - start + i] = False
                ant_diag[start + i] = False

        path_memo = []
        for i in range(n):
            path_memo.append("." * i + "Q" + "." * (n-i-1))
        ans = []
        col, diag, ant_diag = [False] * n, [False] * (2 * n), [False] * (2 * n)
        backtracking(0, [])
        return ans
# leetcode submit region end(Prohibit modification and deletion)
print(Solution().solveNQueens(5))
