# 我们有 n 栋楼，编号从 0 到 n - 1 。每栋楼有若干员工。由于现在是换楼的季节，部分员工想要换一栋楼居住。 
# 
#  给你一个数组 requests ，其中 requests[i] = [fromi, toi] ，表示一个员工请求从编号为 fromi 的楼搬到编号为 
# toi 的楼。 
# 
#  一开始 所有楼都是满的，所以从请求列表中选出的若干个请求是可行的需要满足 每栋楼员工净变化为 0 。意思是每栋楼 离开 的员工数目 等于 该楼 搬入 的员
# 工数数目。比方说 n = 3 且两个员工要离开楼 0 ，一个员工要离开楼 1 ，一个员工要离开楼 2 ，如果该请求列表可行，应该要有两个员工搬入楼 0 ，一个员
# 工搬入楼 1 ，一个员工搬入楼 2 。 
# 
#  请你从原请求列表中选出若干个请求，使得它们是一个可行的请求列表，并返回所有可行列表中最大请求数目。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
# 输出：5
# 解释：请求列表如下：
# 从楼 0 离开的员工为 x 和 y ，且他们都想要搬到楼 1 。
# 从楼 1 离开的员工为 a 和 b ，且他们分别想要搬到楼 2 和 0 。
# 从楼 2 离开的员工为 z ，且他想要搬到楼 0 。
# 从楼 3 离开的员工为 c ，且他想要搬到楼 4 。
# 没有员工从楼 4 离开。
# 我们可以让 x 和 b 交换他们的楼，以满足他们的请求。
# 我们可以让 y，a 和 z 三人在三栋楼间交换位置，满足他们的要求。
# 所以最多可以满足 5 个请求。 
# 
#  示例 2： 
# 
#  
# 
#  输入：n = 3, requests = [[0,0],[1,2],[2,1]]
# 输出：3
# 解释：请求列表如下：
# 从楼 0 离开的员工为 x ，且他想要回到原来的楼 0 。
# 从楼 1 离开的员工为 y ，且他想要搬到楼 2 。
# 从楼 2 离开的员工为 z ，且他想要搬到楼 1 。
# 我们可以满足所有的请求。 
# 
#  示例 3： 
# 
#  输入：n = 4, requests = [[0,3],[3,1],[1,2],[2,0]]
# 输出：4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 20 
#  1 <= requests.length <= 16 
#  requests[i].length == 2 
#  0 <= fromi, toi < n 
#  
#  Related Topics 位运算 枚举 👍 16 👎 0
from typing import List
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        """
        f[mask]表示满足请求状态为mask，n个房间的迁入迁出
        f[mask] = f[mask\i][requests[i][0]] - 1, f[mask\i][requests[i][1]] + 1
        遍历mask过程中，统计all(n) == 0, ans = max(ans, bin(mask).count("1"))
        时间复杂度O(2^m * m * n)，超时
        必须把n给优化掉
        """
        m = len(requests)
        f = [[0] * n for _ in range(1 << m)]
        ans = 0
        for mask in range(1, 1 << m):
            for i in range(m):
                if mask & (1 << i):
                    from_build, to_build = requests[i]
                    f[mask] = f[mask ^ (1 << i)].copy()
                    f[mask][from_build] -= 1
                    f[mask][to_build] += 1
                    if all(f[mask][i] == 0 for i in range(n)):
                        ans = max(ans, bin(mask).count("1"))
        return ans
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        """
        直接暴力，状态压缩
        遍历每个状态，检查每个状态时间复杂度为O(max(n, m))
        总时间复杂度：O(2^m * max(n, m))
        """
        m = len(requests)
        ans = 0
        for mask in range(1, 1 << m):
            f, idx, tmp = [0] * n, 0, mask
            while tmp:
                if tmp & 1:
                    from_bulid, to_build = requests[idx]
                    f[from_bulid] -= 1
                    f[to_build] += 1
                tmp >>= 1
                idx += 1
            if all(f[i] == 0 for i in range(n)):
                ans = max(ans, bin(mask).count("1"))
        return ans
# leetcode submit region end(Prohibit modification and deletion)
n = 20
requests = [[1,1],[1,3],[3,10],[3,14],[4,14],[7,10],[9,19],[10,1],[10,3],[13,4],[13,13],[14,7],[14,13],[19,5],[19,9],[19,19]]
print(Solution().maximumRequests(n, requests))