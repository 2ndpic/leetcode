# 给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：points = [[1,1],[2,2],[3,3]]
# 输出：3
#  
# 
#  示例 2： 
# 
#  
# 输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# 输出：4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= points.length <= 300 
#  points[i].length == 2 
#  -104 <= xi, yi <= 104 
#  points 中的所有点 互不相同 
#  
#  Related Topics 几何 哈希表 数学 
#  👍 289 👎 0

from typing import List
import collections
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        memo = collections.defaultdict(set)
        for i in range(n):
            for j in range(i + 1, n):
                (x1, y1), (x2, y2) = points[i], points[j]
                if x2 == x1:
                    memo[f"x={x2}"].add(i)
                    memo[f"x={x2}"].add(j)
                else:
                    k = (y2 - y1) / (x2 - x1)
                    b = (x2 * y1 - x1 * y2) / (x2 - x1)
                    memo[f"{k:.6f} {b:.6f}"].add(i)
                    memo[f"{k:.6f} {b:.6f}"].add(j)

        return max(len(i) for i in memo.values())

# leetcode submit region end(Prohibit modification and deletion)
points = [[1,1],[2,2],[3,3]]
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
print(Solution().maxPoints(points))