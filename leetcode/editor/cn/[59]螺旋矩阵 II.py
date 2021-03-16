# 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：[[1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 20 
#  
#  Related Topics 数组 
#  👍 333 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[None] * n for _ in range(n)]
        i, j = 0, 0
        di, dj = 0, 1
        for k in range(1, n * n + 1):
            ans[i][j] = k
            if ans[(i + di) % n][(j + dj) % n] is not None:
                di, dj = dj, -di
            i += di
            j += dj

        return ans
# leetcode submit region end(Prohibit modification and deletion)
print(Solution().generateMatrix(5))