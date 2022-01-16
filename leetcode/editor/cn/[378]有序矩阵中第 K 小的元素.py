# 给你一个 n x n 矩阵 matrix ，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。 
# 请注意，它是 排序后 的第 k 小元素，而不是第 k 个 不同 的元素。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# 输出：13
# 解释：矩阵中的元素为 [1,5,9,10,11,12,13,13,15]，第 8 小元素是 13
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = [[-5]], k = 1
# 输出：-5
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == matrix.length 
#  n == matrix[i].length 
#  1 <= n <= 300 
#  -10⁹ <= matrix[i][j] <= 10⁹ 
#  题目数据 保证 matrix 中的所有行和列都按 非递减顺序 排列 
#  1 <= k <= n² 
#  
#  Related Topics 数组 二分查找 矩阵 排序 堆（优先队列） 👍 737 👎 0

from typing import List
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        q = [(matrix[i][0], i, 0) for i in range(n)]
        for _ in range(k):
            ans, i, j = heapq.heappop(q)
            if j + 1 < n: heapq.heappush(q, (matrix[i][j + 1], i, j + 1))
        return ans


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def cal(num):
            i, j, cnt = 0, n - 1, 0
            while i < n and j >= 0:
                if matrix[i][j] > num:
                    j -= 1
                else:
                    i += 1
                    cnt += j + 1
            return cnt
        n = len(matrix)
        lo, hi = matrix[0][0], matrix[n-1][n-1]
        while lo < hi:
            mid = (lo + hi) // 2
            if cal(mid) < k: lo = mid + 1
            else: hi = mid
        return lo
# leetcode submit region end(Prohibit modification and deletion)
