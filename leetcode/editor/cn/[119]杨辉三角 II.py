# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。 
# 
#  
# 
#  在杨辉三角中，每个数是它左上方和右上方的数的和。 
# 
#  示例: 
# 
#  输入: 3
# 输出: [1,3,3,1]
#  
# 
#  进阶： 
# 
#  你可以优化你的算法到 O(k) 空间复杂度吗？ 
#  Related Topics 数组 
#  👍 231 👎 0

from typing import List
class S1:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1]*(rowIndex+1) for _ in range(rowIndex+1)]
        for i in range(rowIndex+1):
            for j in range(1, i):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        return dp[rowIndex]
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [1] + [0] * rowIndex
        for i in range(rowIndex):
            for j in range(i+1, 0, -1):
                dp[j] = dp[j-1] + dp[j]
        return dp
# leetcode submit region end(Prohibit modification and deletion)
print(Solution().getRow(4))