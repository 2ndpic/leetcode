from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def cal_steps(x):
            dis = [n] * n
            steps = 0
            while x >= 0 and dis[x] == n:
                dis[x] = steps
                steps += 1
                x = edges[x]
            return dis
        n, min_dis, ans = len(edges), len(edges), -1
        for i, d1, d2 in zip(range(n), cal_steps(node1), cal_steps(node2)):
            d = max(d1, d2)
            if d < min_dis:
                min_dis, ans = d, i
        return ans

# leetcode submit region end(Prohibit modification and deletion)
print(Solution().closestMeetingNode([2,2,3,-1], 0, 1))