# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 10 
#  -100 <= matrix[i][j] <= 100 
#  
#  Related Topics 数组 
#  👍 656 👎 0

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []
        def helper(start_row, end_row, start_col, end_col):
            # 左闭右闭
            if start_row > end_row or start_col > end_col:
                return
            ans.extend(matrix[start_row][start_col:end_col + 1])
            for i in range(start_row + 1, end_row):
                ans.append(matrix[i][end_col])
            if end_row != start_row:
                ans.extend(matrix[end_row][start_col:end_col + 1][::-1])
            if end_col != start_col:
                for i in range(end_row - 1, start_row, -1):
                    ans.append(matrix[i][start_col])
            helper(start_row + 1, end_row - 1, start_col + 1, end_col - 1)
        helper(0, m - 1, 0, n - 1)
        return ans
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []
        x, y, dx, dy = 0, 0, 0, 1
        for _ in range(m * n):
            ans.append(matrix[x][y])
            matrix[x][y] = None
            if matrix[(x + dx) % m][(y + dy) % n] is None:
                dx, dy = dy, -dx
            x += dx
            y += dy
        return ans
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        每次抽取出矩阵的第一行，然后将新矩阵逆时针反转90度（最后一列变成第一行），递归，直到矩阵为空
        """
        ans = []
        if not matrix:
            return ans
        ans.extend(matrix[0])
        new = [reversed(i) for i in matrix[1:]]
        ans.extend(self.spiralOrder(list(zip(*new))))
        return ans



# leetcode submit region end(Prohibit modification and deletion)
matrix = [[1,2,3],[4,5,6],[7,8,9], [10, 11, 12], [13, 14, 15]]
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(Solution().spiralOrder(matrix))