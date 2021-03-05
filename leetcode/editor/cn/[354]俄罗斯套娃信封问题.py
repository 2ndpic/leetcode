# 给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如
# 同俄罗斯套娃一样。 
# 
#  请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。 
# 
#  说明: 
# 不允许旋转信封。 
# 
#  示例: 
# 
#  输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# 输出: 3 
# 解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
#  
#  Related Topics 二分查找 动态规划 
#  👍 329 👎 0

from typing import List
class Solution:
    # 超时版本时间复杂度O（N^2）
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort()
        n = len(envelopes)
        dp = [0] * (n + 1) # dp[i]表示以第i个信封作为最外层的信封的最多个数(1,...,n)
        for i in range(1, n + 1):
            w, h = envelopes[i - 1]     # w不用考虑肯定是最大的，h不一定，要找比h严格小的最近的那个信封
            for j in range(1, i):
                if envelopes[j-1][0] < w and envelopes[j-1][1] < h:
                    dp[i] = max(dp[i], dp[j])
            dp[i] += 1
        return max(dp)


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort(key = lambda x : (x[0]*x[1], x[0], x[1]))
        n = len(envelopes)
        dp = [0] * (n + 1) # dp[i]表示以第i个信封作为最外层的信封的最多个数(1,...,n)
        for i in range(n):
            w, h = envelopes[i]     # h不一定，要找比h严格小的最近的那个信封,在第[1,..,i)的信封大小合法且离i信封面积最近的那个信封
            lo, hi = 0, i  # 表示信封序号idx
            while lo < hi:
                mid = (lo + hi) // 2
                nw, nh = envelopes[mid]
                if nw >= w:
                    hi = mid
                else:
                    lo = mid + 1
                # elif nw < w and nh >= h:
                #     lo = mid + 1
                # elif nw < w and nh < h:
                #     lo = mid + 1
            # bisect_right的搜索方式，lo落到的范围是0,..,i
            # lo = lo - 1 if lo > 0 else -1
            dp[i + 1] = dp[lo] + 1
        return max(dp)

# leetcode submit region end(Prohibit modification and deletion)
envelopes = [[4,5],[4,6],[6,7],[2,3],[1,1]]
# envelopes = [[5,4],[6,4],[6,7],[2,3]]
# envelopes = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
envelopes = [[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]]
print(Solution().maxEnvelopes(envelopes))
import bisect