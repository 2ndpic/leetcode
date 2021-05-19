# 给你一个二维矩阵 matrix 和一个整数 k ，矩阵大小为 m x n 由非负整数组成。 
# 
#  矩阵中坐标 (a, b) 的 值 可由对所有满足 0 <= i <= a < m 且 0 <= j <= b < n 的元素 matrix[i][j]（下
# 标从 0 开始计数）执行异或运算得到。 
# 
#  请你找出 matrix 的所有坐标中第 k 大的值（k 的值从 1 开始计数）。 
# 
#  
# 
#  示例 1： 
# 
#  输入：matrix = [[5,2],[1,6]], k = 1
# 输出：7
# 解释：坐标 (0,1) 的值是 5 XOR 2 = 7 ，为最大的值。 
# 
#  示例 2： 
# 
#  输入：matrix = [[5,2],[1,6]], k = 2
# 输出：5
# 解释：坐标 (0,0) 的值是 5 = 5 ，为第 2 大的值。 
# 
#  示例 3： 
# 
#  输入：matrix = [[5,2],[1,6]], k = 3
# 输出：4
# 解释：坐标 (1,0) 的值是 5 XOR 1 = 4 ，为第 3 大的值。 
# 
#  示例 4： 
# 
#  输入：matrix = [[5,2],[1,6]], k = 4
# 输出：0
# 解释：坐标 (1,1) 的值是 5 XOR 2 XOR 1 XOR 6 = 0 ，为第 4 大的值。 
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 1000 
#  0 <= matrix[i][j] <= 106 
#  1 <= k <= m * n 
#  
#  Related Topics 数组 
#  👍 32 👎 0

from typing import List
import heapq
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        """
        用堆来记录第几大的值
        size为k的最小堆，堆顶就是第k大的值
        """
        heap, m, n = [], len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = matrix[i - 1][j - 1] ^ dp[i - 1][j - 1] ^ dp[i][j - 1] ^ dp[i - 1][j]
                if len(heap) < k:
                    heapq.heappush(heap, dp[i][j])
                elif heap[0] < dp[i][j]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, dp[i][j])
        return heap[0]
# leetcode submit region end(Prohibit modification and deletion)
matrix = [[5,2],[1,6]]; k = 1
matrix = [[5,2],[1,6]]; k = 2
matrix = [[5,2],[1,6]]; k = 3
matrix = [[5,2],[1,6]]; k = 4
print(Solution().kthLargestValue(matrix, k))


