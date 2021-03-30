# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性： 
# 
#  
#  每行中的整数从左到右按升序排列。 
#  每行的第一个整数大于前一行的最后一个整数。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
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
#  1 <= m, n <= 100 
#  -104 <= matrix[i][j], target <= 104 
#  
#  Related Topics 数组 二分查找 
#  👍 356 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        第一步：二分搜索到matirx行首<=target的上界，即>value的下界 - 1.（bisect_right() - 1）
        第二部：找到行后，二分查找该行的列，bisect_left()
        """
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m
        while lo < hi:
            mid = (lo + hi) // 2
            if matrix[mid][0] > target: hi = mid
            else: lo = mid + 1
        row, lo, hi = lo - 1, 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if matrix[row][mid] < target: lo = mid + 1
            else: hi = mid
        return matrix[row][lo] == target
# leetcode submit region end(Prohibit modification and deletion)
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 61
print(Solution().searchMatrix(matrix, target))