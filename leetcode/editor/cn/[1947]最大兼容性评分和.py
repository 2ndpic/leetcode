# 有一份由 n 个问题组成的调查问卷，每个问题的答案要么是 0（no，否），要么是 1（yes，是）。 
# 
#  这份调查问卷被分发给 m 名学生和 m 名导师，学生和导师的编号都是从 0 到 m - 1 。学生的答案用一个二维整数数组 students 表示，其中 
# students[i] 是一个整数数组，包含第 i 名学生对调查问卷给出的答案（下标从 0 开始）。导师的答案用一个二维整数数组 mentors 表示，其中 
# mentors[j] 是一个整数数组，包含第 j 名导师对调查问卷给出的答案（下标从 0 开始）。 
# 
#  每个学生都会被分配给 一名 导师，而每位导师也会分配到 一名 学生。配对的学生与导师之间的兼容性评分等于学生和导师答案相同的次数。 
# 
#  
#  例如，学生答案为[1, 0, 1] 而导师答案为 [0, 0, 1] ，那么他们的兼容性评分为 2 ，因为只有第二个和第三个答案相同。 
#  
# 
#  请你找出最优的学生与导师的配对方案，以 最大程度上 提高 兼容性评分和 。 
# 
#  给你 students 和 mentors ，返回可以得到的 最大兼容性评分和 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：students = [[1,1,0],[1,0,1],[0,0,1]], mentors = [[1,0,0],[0,0,1],[1,1,0]]
# 输出：8
# 解释：按下述方式分配学生和导师：
# - 学生 0 分配给导师 2 ，兼容性评分为 3 。
# - 学生 1 分配给导师 0 ，兼容性评分为 2 。
# - 学生 2 分配给导师 1 ，兼容性评分为 3 。
# 最大兼容性评分和为 3 + 2 + 3 = 8 。 
# 
#  示例 2： 
# 
#  输入：students = [[0,0],[0,0],[0,0]], mentors = [[1,1],[1,1],[1,1]]
# 输出：0
# 解释：任意学生与导师配对的兼容性评分都是 0 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == students.length == mentors.length 
#  n == students[i].length == mentors[j].length 
#  1 <= m, n <= 8 
#  students[i][k] 为 0 或 1 
#  mentors[j][k] 为 0 或 1 
#  
#  Related Topics 位运算 数组 动态规划 回溯 状态压缩 👍 20 👎 0
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        """
        按照编号顺序给每一名学生分配老师
        长度为m的二进制数mask表示每一名老师是否被分配了学生，1表示分配
        记f[mask]表示当老师被分配学生的状态为mask时，最大的兼容性评分和
        由于规定按照编号给每一名学生分配老师，那么mask中包含c个1，就说明分配的学生编号为0,..,c-1
        因此在状态转移时，可以枚举编号为c-1的学生被分配的是哪一名老师，这样就可以得到状态转移方程
        f[mask] = max(f[mask\i] + g[c - 1][i]) mask的第i位为1
        mask\i表示将mask的第i位从1变成0
        最终答案为f[2^m - 1]
        """
        m, n = len(students), len(students[0])
        g = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                g[i][j] = sum(u == v for u, v in zip(students[i], mentors[j]))

        f = [0] * (1 << m)
        for mask in range(1, 1 << m):
            c = bin(mask).count("1")
            for i in range(m):
                if mask & (1 << i):
                    f[mask] = max(f[mask], f[mask ^ (1 << i)] + g[c - 1][i])
        return f[(1 << m) - 1]

# leetcode submit region end(Prohibit modification and deletion)
