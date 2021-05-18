# 在一座城市里，你需要建 n 栋新的建筑。这些新的建筑会从 1 到 n 编号排成一列。 
# 
#  这座城市对这些新建筑有一些规定： 
# 
#  
#  每栋建筑的高度必须是一个非负整数。 
#  第一栋建筑的高度 必须 是 0 。 
#  任意两栋相邻建筑的高度差 不能超过 1 。 
#  
# 
#  除此以外，某些建筑还有额外的最高高度限制。这些限制会以二维整数数组 restrictions 的形式给出，其中 restrictions[i] = [id
# i, maxHeighti] ，表示建筑 idi 的高度 不能超过 maxHeighti 。 
# 
#  题目保证每栋建筑在 restrictions 中 至多出现一次 ，同时建筑 1 不会 出现在 restrictions 中。 
# 
#  请你返回 最高 建筑能达到的 最高高度 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 5, restrictions = [[2,1],[4,1]]
# 输出：2
# 解释：上图中的绿色区域为每栋建筑被允许的最高高度。
# 我们可以使建筑高度分别为 [0,1,2,1,2] ，最高建筑的高度为 2 。 
# 
#  示例 2： 
# 
#  
# 输入：n = 6, restrictions = []
# 输出：5
# 解释：上图中的绿色区域为每栋建筑被允许的最高高度。
# 我们可以使建筑高度分别为 [0,1,2,3,4,5] ，最高建筑的高度为 5 。
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 10, restrictions = [[5,3],[2,5],[7,4],[10,3]]
# 输出：5
# 解释：上图中的绿色区域为每栋建筑被允许的最高高度。
# 我们可以使建筑高度分别为 [0,1,2,3,3,4,4,5,4,3] ，最高建筑的高度为 5 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= n <= 109 
#  0 <= restrictions.length <= min(n - 1, 105) 
#  2 <= idi <= n 
#  idi 是 唯一的 。 
#  0 <= maxHeighti <= 109 
#  
#  Related Topics 贪心算法 二分查找 
#  👍 24 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        if not restrictions: return n - 1
        restrictions.sort(key = lambda x: x[0])
        if restrictions[0][0] != 1: restrictions = [[1, 0]] + restrictions
        if restrictions[-1][0] != n: restrictions.append([n, n-1])
        m = len(restrictions)
        # 从左往右，限制下一个受限房子的高度
        for idx in range(m - 1):
            (i, hi), (j, hj) = restrictions[idx], restrictions[idx + 1]
            hj = min(hj, hi + (j - i))
            restrictions[idx + 1][1] = hj
        # 从右往左，限制上一个受限房子的高度
        for idx in range(m - 1, 0, -1):
            (i, hi), (j, hj) = restrictions[idx], restrictions[idx - 1]
            hj = min(hj, hi + (i - j))
            restrictions[idx -1][1] = hj
        ans = 0
        for idx in range(m - 1):
            (i, limit_i), (j, limit_j) = restrictions[idx], restrictions[idx + 1]
            ans = max(ans, ((j - i) + limit_i + limit_j) // 2) # 过相邻受限房子的斜率为1，-1直线的交点为最大高度
        return ans

# leetcode submit region end(Prohibit modification and deletion)
n = 5;restrictions = [[2,1],[4,1]] #2
n = 6;restrictions = []  #5
# n = 10;restrictions = [[5,3],[2,5],[7,4],[10,3]]
print(Solution().maxBuilding(n, restrictions)) # 2
