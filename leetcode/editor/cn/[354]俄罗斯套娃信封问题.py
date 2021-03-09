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
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        if not n: return n
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [1] * n # dp[i]表示以第i个元素结尾的LIS长度
        for i in range(n):
            for j in range(i): # [6, 7], [6, 4]
                """
                envelopes[i][1] > envelopes[j][1]
                因为j<i的，且第二个维度是递减的，所以上式成立只有在envelopes[i][0] > envelopes[j][0]的情况
                """
                if envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        贪心+二分
        贪心策略是：尽可能使此LIS固定的时候，w和h的选择是最小的，这样才能叠加更多的信封
        叠加的规则是：old_w < w, old_h < h
        按w升序排列，w相同h按降序排列。因为只有这样，w相同的信封才不会多次选择
        如[[6, 3], [6, 4], [6, 5]](h升序排列)，此时遍历对比得到，old_h < h，但是我们不能确定old_w是否一定小于w（可能相等）
        而[[6, 5], [6, 4], [6, 3]](h降序排列)，此时遍历对比得到，old_h < h，我们一定可以确定old_w一定小于w，(因为如果old_w == w, old_h >= h)
        定义low数组表示：low[:i]代表LIS长度等于i的情况下，信封高度的最小值,注意low里面存的是高度值
        - 如果当前遍历到的h > low[-1]，前面提到过h > old_h情况，w > old_w,所以我们可以在当前基础上又叠加一个信封，即low数组增加一个元素，其值是当前的h
        - 如果当前遍历到的h < low[-1]，则去low数组中找到第一个大于等于h的元素并替换（此元素的w必然小于等于此时的w），因为是替换操作，low数组不会增加元素。
            例如low = [2, 3, 5]替换的是low最后一个元素变成了[2, 3, 4]，意味着原先LIS长度等于3的情况下，信封高度的最小值由5变成了4
        上面的查找操作，可以用O(logn)的二分查找完成，使用寻找第一个大于等于的bisect_left算法，即可找到位置
        """
        n = len(envelopes)
        if not n: return n
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        low = []              # low[:i]代表LIS=i的情况下，信封高度的最小值
        for w, h in envelopes:
            idx = bisect.bisect_left(low, h)
            if idx == len(low): low.append(h)
            else: low[idx] = h
        return len(low)

import bisect
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        贪心+二分
        贪心策略是：尽可能使此LIS固定的时候，w和h的选择是最小的，这样才能叠加更多的信封
        叠加的规则是：old_w < w, old_h < h
        按w升序排列，w相同h按降序排列。因为只有这样，w相同的信封才不会多次选择
        如[[6, 3], [6, 4], [6, 5]](h升序排列)，此时遍历对比得到，old_h < h，但是我们不能确定old_w是否一定小于w（可能相等）
        而[[6, 5], [6, 4], [6, 3]](h降序排列)，此时遍历对比得到，old_h < h，我们一定可以确定old_w一定小于w，(因为如果old_w == w, old_h >= h)
        定义low数组表示：low[:i]代表LIS长度等于i的情况下，信封高度的最小值,注意low里面存的是高度值
        - 如果当前遍历到的h > low[-1]，前面提到过h > old_h情况，w > old_w,所以我们可以在当前基础上又叠加一个信封，即low数组增加一个元素，其值是当前的h
        - 如果当前遍历到的h < low[-1]，则去low数组中找到第一个大于等于h的元素并替换（此元素的w必然小于等于此时的w），因为是替换操作，low数组不会增加元素。
            例如low = [2, 3, 5]替换的是low最后一个元素变成了[2, 3, 4]，意味着原先LIS长度等于3的情况下，信封高度的最小值由5变成了4
        上面的查找操作，可以用O(logn)的二分查找完成，使用寻找第一个大于等于的bisect_left算法，即可找到位置
        """
        n = len(envelopes)
        if not n: return n
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        low = []              # low[:i]代表LIS=i的情况下，信封高度的最小值
        for w, h in envelopes:# [5, 3], [6, 5], [6, 4], [6, 3]
            if not low or h > low[-1]: low.append(h)
            else: low[bisect.bisect_left(low, h)] = h
        return len(low)





# leetcode submit region end(Prohibit modification and deletion)
# envelopes = [[4,5],[4,6],[6,7],[2,3],[1,1]]
# envelopes = [[5,4],[6,4],[6,7],[2,3]]
# envelopes = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
# envelopes = [[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]]
envelopes = [[1,2],[2,3],[3,4],[3,5],[4,5],[5,5],[5,6],[6,7],[7,8]] # 7
print(Solution().maxEnvelopes(envelopes))
