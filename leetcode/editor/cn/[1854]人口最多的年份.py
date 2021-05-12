# 给你一个二维整数数组 logs ，其中每个 logs[i] = [birthi, deathi] 表示第 i 个人的出生和死亡年份。 
# 
#  年份 x 的 人口 定义为这一年期间活着的人的数目。第 i 个人被计入年份 x 的人口需要满足：x 在闭区间 [birthi, deathi - 1] 内
# 。注意，人不应当计入他们死亡当年的人口中。 
# 
#  返回 人口最多 且 最早 的年份。 
# 
#  
# 
#  示例 1： 
# 
#  输入：logs = [[1993,1999],[2000,2010]]
# 输出：1993
# 解释：人口最多为 1 ，而 1993 是人口为 1 的最早年份。
#  
# 
#  示例 2： 
# 
#  输入：logs = [[1950,1961],[1960,1971],[1970,1981]]
# 输出：1960
# 解释： 
# 人口最多为 2 ，分别出现在 1960 和 1970 。
# 其中最早年份是 1960 。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= logs.length <= 100 
#  1950 <= birthi < deathi <= 2050 
#  
#  Related Topics 数组 
#  👍 5 👎 0
import collections
from typing import List
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        def get_live(x):
            ans = 0
            for b, d in logs:
                if b <= x < d:
                    ans += 1
            return ans
        alive = 0
        for year in range(1950, 2051):
            cur_alive = get_live(year)
            if cur_alive > alive:
                alive = cur_alive
                ans = year
        return ans

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        b = collections.Counter(i[0] for i in logs)
        d = collections.Counter(i[1] for i in logs)
        alive, max_alive = 0, 0
        for i in range(1950, 2051):
            alive = alive + b[i] - d[i]
            b[i], d[i] = 0, 0
            if alive > max_alive:
                max_alive = alive
                ans = i
        return ans
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        """
        差分数组
        """
        delta = [0] * 101
        offset = 1950
        for b, d in logs:
            delta[b-offset] += 1
            delta[d-offset] -= 1
        mx, cur, ans = 0, 0, 0
        for i in range(len(delta)):
            cur += delta[i]
            if cur > mx:
                mx, ans = cur, i
        return ans + offset


# leetcode submit region end(Prohibit modification and deletion)
logs = [[1993,1999],[2000,2010]]
logs = [[2025,2041],[1988,2007],[2003,2046],[2045,2049],[2025,2027],[2014,2040],[2014,2027],[2011,2027],[1972,2019]]
print(Solution().maximumPopulation(logs))