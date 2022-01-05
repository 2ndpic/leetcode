# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"]
# ,["1","0","0","1","0"]]
# 输出：6
# 解释：最大矩形如上图所示。
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = []
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：matrix = [["0"]]
# 输出：0
#  
# 
#  示例 4： 
# 
#  
# 输入：matrix = [["1"]]
# 输出：1
#  
# 
#  示例 5： 
# 
#  
# 输入：matrix = [["0","0"]]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  rows == matrix.length 
#  cols == matrix[0].length 
#  1 <= row, cols <= 200 
#  matrix[i][j] 为 '0' 或 '1' 
#  
#  Related Topics 栈 数组 动态规划 矩阵 单调栈 👍 1138 👎 0
from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        left = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    left[i][j] += (left[i][j - 1] if j > 0 else 0) + 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0": continue
                width, area = left[i][j], left[i][j]
                for k in range(i - 1, -1, -1):
                    width = min(width, left[k][j])
                    area = max(area, (i - k + 1) * width)
                ans = max(ans, area)
        return ans

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        left = [[0] * n for _ in range(m)] + [[-1] * n]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    left[i][j] += (left[i][j - 1] if j > 0 else 0) + 1
        ans = 0
        for j in range(n):
            stack = []
            for i in range(m + 1):
                while stack and left[stack[-1]][j] > left[i][j]:
                    row = stack.pop()
                    if stack:
                        ans = max(ans, left[row][j] * (i - stack[-1] - 1))
                    else:
                        ans = max(ans, left[row][j] * i)
                stack.append(i)
        return ans
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n, ans = len(matrix), len(matrix[0]), 0
        pre = [0] * (n + 1)
        for i in range(m):
            for j in range(n):
                pre[j] = pre[j] + 1 if matrix[i][j] == "1" else 0
            stack = []
            for k, num in enumerate(pre):
                while stack and pre[stack[-1]] > num:
                    index = stack.pop()
                    ans = max(ans, pre[index] * ((k - stack[-1] - 1) if stack else k))
                stack.append(k)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
matrix = [["0","0","1","0"],
          ["0","0","1","0"],
          ["0","0","1","0"],
          ["0","0","1","1"],
          ["0","1","1","1"],
          ["0","1","1","1"],
          ["1","1","1","1"]]
print(Solution().maximalRectangle(matrix))