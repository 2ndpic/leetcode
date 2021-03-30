# 给定一个三角形 triangle ，找出自顶向下的最小路径和。 
# 
#  每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果
# 正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# 输出：11
# 解释：如下面简图所示：
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
#  
# 
#  示例 2： 
# 
#  
# 输入：triangle = [[-10]]
# 输出：-10
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= triangle.length <= 200 
#  triangle[0].length == 1 
#  triangle[i].length == triangle[i - 1].length + 1 
#  -104 <= triangle[i][j] <= 104 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题吗？ 
#  
#  Related Topics 数组 动态规划 
#  👍 720 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = [[0] * m for _ in range(2)]
        dp[0][0] = triangle[0][0]
        for i in range(1, m):
            for j in range(i + 1):
                val = triangle[i][j]
                dp[i & 1][j] = float('inf')
                if j != 0:
                    dp[i & 1][j] = min(dp[i & 1][j], dp[(i - 1) & 1][j - 1] + val)
                if j != i:
                    dp[i & 1][j] = min(dp[i & 1][j], dp[(i - 1) & 1][j] + val)
        return min(dp[(m - 1) & 1])
# leetcode submit region end(Prohibit modification and deletion)
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(Solution().minimumTotal(triangle))