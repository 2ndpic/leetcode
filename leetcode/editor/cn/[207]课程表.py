# 你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。 
# 
#  在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1] 
# 
#  给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？ 
# 
#  
# 
#  示例 1: 
# 
#  输入: 2, [[1,0]] 
# 输出: true
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。 
# 
#  示例 2: 
# 
#  输入: 2, [[1,0],[0,1]]
# 输出: false
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。 
# 
#  
# 
#  提示： 
# 
#  
#  输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。 
#  你可以假定输入的先决条件中没有重复的边。 
#  1 <= numCourses <= 10^5 
#  
#  Related Topics 深度优先搜索 广度优先搜索 图 拓扑排序 
#  👍 685 👎 0

from typing import List
from collections import deque
# leetcode submit region begin(Prohibit modification and deletion)
def topo_sort(g):
    in_degrees = [0] * len(g)
    for u in g:
        for v in u:
            in_degrees[v] += 1
    degrees_0 = deque()
    for index, value in enumerate(in_degrees):
        if value == 0:
            degrees_0.append(index)
    n = 0
    while degrees_0:
        u = degrees_0.popleft()
        n += 1
        for v in g[u]:
            in_degrees[v] -= 1
            if in_degrees[v] == 0:
                degrees_0.append(v)
    return n == len(g)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        - 以出度建立邻接表
        - 构建入度统计
        """
        g = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            g[v].append(u)
        return topo_sort(g)
# leetcode submit region end(Prohibit modification and deletion)
