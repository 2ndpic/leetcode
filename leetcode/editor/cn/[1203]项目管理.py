# 公司共有 n 个项目和 m 个小组，每个项目要不无人接手，要不就由 m 个小组之一负责。 
# 
#  group[i] 表示第 i 个项目所属的小组，如果这个项目目前无人接手，那么 group[i] 就等于 -1。（项目和小组都是从零开始编号的）小组可能存
# 在没有接手任何项目的情况。 
# 
#  请你帮忙按要求安排这些项目的进度，并返回排序后的项目列表： 
# 
#  
#  同一小组的项目，排序后在列表中彼此相邻。 
#  项目之间存在一定的依赖关系，我们用一个列表 beforeItems 来表示，其中 beforeItems[i] 表示在进行第 i 个项目前（位于第 i 个
# 项目左侧）应该完成的所有项目。 
#  
# 
#  如果存在多个解决方案，只需要返回其中任意一个即可。如果没有合适的解决方案，就请返回一个 空列表 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[
# 3,6],[],[],[]]
# 输出：[6,3,4,1,5,2,0,7]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[
# 3],[],[4],[]]
# 输出：[]
# 解释：与示例 1 大致相同，但是在排序后的列表中，4 必须放在 6 的前面。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= m <= n <= 3 * 104 
#  group.length == beforeItems.length == n 
#  -1 <= group[i] <= m - 1 
#  0 <= beforeItems[i].length <= n - 1 
#  0 <= beforeItems[i][j] <= n - 1 
#  i != beforeItems[i][j] 
#  beforeItems[i] 不含重复元素 
#  
#  Related Topics 深度优先搜索 图 拓扑排序 
#  👍 59 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque

def topo_sort(g, items, in_degrees):
    res = []
    degrees_0 = deque()
    for i in items:
        if in_degrees[i] == 0:
            degrees_0.append(i)

    while degrees_0:
        u = degrees_0.popleft()
        res.append(u)
        for v in g[u]:
            in_degrees[v] -= 1
            if in_degrees[v] == 0:
                degrees_0.append(v)

    if len(res) == len(items):
        return res
    return []

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # 初始化，对没有分配组的分配组,建立组-任务的一对多映射
        group_tasks = [[] for i in range(m)]
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
                group_tasks.append([i])
            else:
                group_tasks[group[i]].append(i)

        # 以出度建立邻接表
        g_group = [[] for _ in range(m)]
        g_task = [[] for _ in range(n)]
        group_indegrees = [0 for _ in range(m)]
        task_indegrees = [0 for _ in range(n)]

        for u in range(n):
            for v in beforeItems[u]:
                if group[u] != group[v]:
                    g_group[group[v]].append(group[u])
                    group_indegrees[group[u]] += 1
                else:
                    g_task[v].append(u)
                    task_indegrees[u] += 1
        res = []
        group_order = topo_sort(g_group, [i for i in range(m)], group_indegrees)
        if not group_order:
            return res
        for each_group in group_order:
            res.extend(topo_sort(g_task, group_tasks[each_group], task_indegrees))
        return res if len(res) == n else []


# leetcode submit region end(Prohibit modification and deletion)
n = 3
m = 2
group = [0, 1, 0]
beforeItems = [[2], [2], []]
print(Solution().sortItems(n, m, group, beforeItems))