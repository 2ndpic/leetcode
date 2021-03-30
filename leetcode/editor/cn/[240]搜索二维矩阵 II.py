# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性： 
# 
#  
#  每行的元素从左到右升序排列。 
#  每列的元素从上到下升序排列。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21
# ,23,26,30]], target = 5
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21
# ,23,26,30]], target = 20
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= n, m <= 300 
#  -109 <= matix[i][j] <= 109 
#  每行的所有元素从左到右升序排列 
#  每列的所有元素从上到下升序排列 
#  -109 <= target <= 109 
#  
#  Related Topics 二分查找 分治算法 
#  👍 580 👎 0

from typing import List
import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        时间复杂度O(mlogn)
        """
        def helper(i):
            if i == len(matrix):
                return False
            if matrix[i][0] <= target <= matrix[i][-1]:
                if matrix[i][bisect.bisect_left(matrix[i], target)] == target:
                    return True
            return helper(i + 1)

        return helper(0)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        迭代查找，时间复杂度O(m + n)
        从矩阵左下角开始查找。当前值大于target就向上走，小于target就向右走
        """
        m, n = len(matrix), len(matrix[0])
        row, col = m - 1, 0
        while 0 <= row <= m - 1 and 0 <= col <= n - 1:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                return True
        return False
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        对角线二分查找，二分查找该对角线的行和列。时间复杂度O(log(n!))
        """
        m, n = len(matrix), len(matrix[0])
        row, col = 0, 0
        while row < m and col < n:
            if matrix[row][col] > target:
                return False
            lo, hi = row, m
            while lo < hi:
                mid = (lo + hi) // 2
                if matrix[mid][col] < target: lo = mid + 1
                elif matrix[mid][col] > target: hi = mid
                else: return True
            lo, hi = col, n
            while lo < hi:
                mid = (lo + hi) // 2
                if matrix[row][mid] < target: lo = mid + 1
                elif matrix[row][mid] > target: hi = mid
                else: return True
            row, col = row + 1, col + 1
        return False



# leetcode submit region end(Prohibit modification and deletion)
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21 ,23,26,30]]
target = 15
print(Solution().searchMatrix(matrix, target))