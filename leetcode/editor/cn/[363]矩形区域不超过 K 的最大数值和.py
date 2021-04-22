# 给你一个 m x n 的矩阵 matrix 和一个整数 k ，找出并返回矩阵内部矩形区域的不超过 k 的最大数值和。 
# 
#  题目数据保证总会存在一个数值和不超过 k 的矩形区域。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [[1,0,1],[0,-2,3]], k = 2
# 输出：2
# 解释：蓝色边框圈出来的矩形区域 [[0, 1], [-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = [[2,2,-1]], k = 3
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 100 
#  -100 <= matrix[i][j] <= 100 
#  -105 <= k <= 105 
#  
# 
#  
# 
#  进阶：如果行数远大于列数，该如何设计解决方案？ 
#  Related Topics 队列 二分查找 动态规划 
#  👍 227 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
from sortedcontainers import SortedList
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], K: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j - 1]
        ans = float("-inf")
        for i in range(n):
            for j in range(i, n):
                pres = SortedList([0])
                pre = 0
                for k in range(m):
                    pre += matrix[k][j] - (0 if i == 0 else matrix[k][i - 1])
                    # 寻找小于等于 pre - k 的最大数。
                    # 为了达到这个目的，可以使用 bisect_left 来完成。（使用 bisect_right 不包含等号）
                    idx = pres.bisect_left(pre - K)
                    # 如果 i == len(pre) 表示无解
                    if idx < len(pres):
                        ans = max(ans, pre - pres[idx])
                    pres.add(pre)

        return ans
# leetcode submit region end(Prohibit modification and deletion)
matrix = [[1,0,1],[0,-2,3]]
print(Solution().maxSumSubmatrix(matrix, 1))
