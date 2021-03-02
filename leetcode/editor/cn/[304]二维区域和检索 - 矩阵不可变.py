# 给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2)。 
# 
#  
# 上图子矩阵左上角 (row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。 
# 
#  示例: 
# 
#  给定 matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]
# 
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
#  
# 
#  说明: 
# 
#  
#  你可以假设矩阵不可变。 
#  会多次调用 sumRegion 方法。 
#  你可以假设 row1 ≤ row2 且 col1 ≤ col2。 
#  
#  Related Topics 动态规划 
#  👍 158 👎 0

from typing import List
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        """
        建立行和的前缀和，单独每一行的前缀和
        """
        if matrix == []:
            self.dp = []
        else:
            self.n, self.m = len(matrix), len(matrix[0])
            self.dp = [0] * (self.n * self.m + 1)
            for i in range(self.n):
                for j in range(self.m):
                    k = self.m * i + j + 1
                    self.dp[k] = self.dp[k-1] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1, row2 + 1):
            ans += self.dp[i * self.m + col2 + 1] - self.dp[i * self.m + col1]
        return ans

# leetcode submit region begin(Prohibit modification and deletion)
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if matrix == []:
            self.dp = []
        else:
            n, m = len(matrix), len(matrix[0])
            self.dp = [[0] * (m + 1) for _ in range(n + 1)]
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    self.dp[i][j] = self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2+1][col2+1] - self.dp[row2+1][col1] - self.dp[row1][col2+1] + self.dp[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# leetcode submit region end(Prohibit modification and deletion)
print(NumMatrix([[-1]]).sumRegion(0, 0, 0, 0))
