# 给你一个整数方阵 arr ，定义「非零偏移下降路径」为：从 arr 数组中的每一行选择一个数字，且按顺序选出来的数字中，相邻数字不在原数组的同一列。 
# 
#  请你返回非零偏移下降路径数字和的最小值。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：arr = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：13
# 解释：
# 所有非零偏移下降路径包括：
# [1,5,9], [1,5,7], [1,6,7], [1,6,8],
# [2,4,8], [2,4,9], [2,6,7], [2,6,8],
# [3,4,8], [3,4,9], [3,5,7], [3,5,9]
# 下降路径中数字和最小的是 [1,5,7] ，所以答案是 13 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length == arr[i].length <= 200 
#  -99 <= arr[i][j] <= 99 
#  
#  Related Topics 动态规划 
#  👍 41 👎 0

from typing import List


class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        """
        f[i][j]表示到达位置arr[i][j]的路径和最小值
        f[i][j] = min(f[i-1][j-1], f[i-1][j+1])

        O(n^3)超时
        """
        m, n = len(arr), len(arr[0])
        f = [arr[0] for _ in range(2)]
        for i in range(1, m):
            f[i&1] = [float('inf')] * n
            for j in range(n):
                for p in range(n):
                    if p != j:
                        f[i & 1][j] = min(f[i & 1][j], f[(i - 1) & 1][p] + arr[i][j])
        return min(f[(m - 1) & 1])
import heapq
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        """
        状态的遍历肯定不能优化了，O(n^2)固定
        遍历上一行的过程中可以优化，其实只会用到上一行的两个统计，最小值和次小值
        如果如果f[i-1]的最小值位置在j,f[i][j]=上一行次小值+arr[i][j]，其他位置就用最小值更新
        """
        m, n = len(arr), len(arr[0])
        f = [arr[0] for _ in range(2)]
        pre = []
        for i, v in enumerate(arr[0]):
            heapq.heappush(pre, (-v, i))
            if len(pre) > 2:
                heapq.heappop(pre)

        for i in range(1, m):
            f[i&1] = [float('inf')] * n
            cur = []
            for j in range(n):
                f[i&1][j] = -(pre[1][0] if pre[1][1] != j else pre[0][0]) + arr[i][j]
                heapq.heappush(cur, (-f[i&1][j], j))
                if len(cur) > 2:
                    heapq.heappop(cur)
            pre = cur
        return min(f[(m-1)&1])

# leetcode submit region end(Prohibit modification and deletion)
nums = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().minFallingPathSum(nums))