# 给你一个 m * n 的矩阵 seats 表示教室中的座位分布。如果座位是坏的（不可用），就用 '#' 表示；否则，用 '.' 表示。 
# 
#  学生可以看到左侧、右侧、左上、右上这四个方向上紧邻他的学生的答卷，但是看不到直接坐在他前面或者后面的学生的答卷。请你计算并返回该考场可以容纳的一起参加考试
# 且无法作弊的最大学生人数。 
# 
#  学生必须坐在状况良好的座位上。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：seats = [["#",".","#","#",".","#"],
#               [".","#","#","#","#","."],
#               ["#",".","#","#",".","#"]]
# 输出：4
# 解释：教师可以让 4 个学生坐在可用的座位上，这样他们就无法在考试中作弊。 
#  
# 
#  示例 2： 
# 
#  输入：seats = [[".","#"],
#               ["#","#"],
#               ["#","."],
#               ["#","#"],
#               [".","#"]]
# 输出：3
# 解释：让所有学生坐在可用的座位上。
#  
# 
#  示例 3： 
# 
#  输入：seats = [["#",".",".",".","#"],
#               [".","#",".","#","."],
#               [".",".","#",".","."],
#               [".","#",".","#","."],
#               ["#",".",".",".","#"]]
# 输出：10
# 解释：让学生坐在第 1、3 和 5 列的可用座位上。
#  
# 
#  
# 
#  提示： 
# 
#  
#  seats 只包含字符 '.' 和'#' 
#  m == seats.length 
#  n == seats[i].length 
#  1 <= m <= 8 
#  1 <= n <= 8 
#  
#  Related Topics 位运算 数组 动态规划 状态压缩 矩阵 👍 131 👎 0
from typing import List
from functools import reduce, lru_cache

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        f = [[0] * (1 << n) for _ in range(2)]
        for i in range(1, m + 1):
            mask = subset = reduce(lambda x, y: x | (1 << y), [j for j, ch in enumerate(seats[i - 1]) if ch == "."], 0)
            while subset:
                if subset & (subset << 1) == subset & (subset >> 1) == 0:
                    cnt = bin(subset).count("1")
                    for j in range(1 << n):
                        if subset & (j << 1) or subset & (j >> 1): continue
                        f[i & 1][subset] = max(f[i & 1][subset], f[(i - 1) & 1][j] + cnt)
                subset = (subset - 1) & mask
            f[i & 1][0] = max(f[(i - 1) & 1]) # 没有枚举到此行不坐人的情况

        return max(f[m & 1])


class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        @lru_cache(None)
        def dfs(row, premask):
            if row == m: return 0
            ans = 0
            for mask in range(1 << n):
                if mask & (mask << 1) == mask & (mask >> 1) == premask & (mask << 1) == premask & (mask >> 1) == 0 and valid[row] & mask == mask:
                    ans = max(ans, dfs(row + 1, mask) + bin(mask).count("1"))
            return ans

        m, n = len(seats), len(seats[0])
        valid = [reduce(lambda x, y: x | (1 << y), [j for j, ch in enumerate(row) if ch == "."], 0) for row in seats]
        return dfs(0, 0)


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        @lru_cache(None)
        def dfs(row, premask):
            if row < 0: return 0
            ans = 0
            for mask in range(1 << n):
                if mask & (mask << 1) == mask & (mask >> 1) == premask & (mask << 1) == premask & (mask >> 1) == 0 and valid[row] & mask == mask:
                    ans = max(ans, dfs(row - 1, mask) + bin(mask).count("1"))
            return ans

        m, n = len(seats), len(seats[0])
        valid = [reduce(lambda x, y: x | (1 << y), [j for j, ch in enumerate(row) if ch == "."], 0) for row in seats]
        return dfs(m - 1, 0)
# leetcode submit region end(Prohibit modification and deletion)
seats = [["#",".","#","#",".","#"],[".","#","#","#","#","."],["#",".","#","#",".","#"]]
print(Solution().maxStudents(seats))