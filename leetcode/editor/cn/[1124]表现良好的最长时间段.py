# 给你一份工作时间表 hours，上面记录着某一位员工每天的工作小时数。 
# 
#  我们认为当员工一天中的工作小时数大于 8 小时的时候，那么这一天就是「劳累的一天」。 
# 
#  所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 大于「不劳累的天数」。 
# 
#  请你返回「表现良好时间段」的最大长度。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：hours = [9,9,6,0,6,6,9]
# 输出：3
# 解释：最长的表现良好时间段是 [9,9,6]。 
# 
#  示例 2： 
# 
#  
# 输入：hours = [6,6,6]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= hours.length <= 10⁴ 
#  0 <= hours[i] <= 16 
#  
#  Related Topics 栈 数组 哈希表 前缀和 单调栈 👍 165 👎 0
from typing import List
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        """
        将hours重新赋值，大于8的看作1，小于等于8的看作-1，那么就是找一段最长区间，其区间和大于0
        当前遍历到hours[r]，设hours[0,...,r]的前缀和为curr
        - if curr > 0: 那么当前hours[0,..,r]就是当前最长区间了，直接更新答案为r+1
        - 否则我们希望找到一个最小的下标l，使得区间[l+1,..,r] > 0，即curr - sum(hours[0,..,l]) > 0，但是这样并不好找到l，可以换个思路。
            我们去寻找curr-1是否作为前缀和出现过，如果出现过，我们采用最早出现的下标l（使用字典来查询和记录），必然有curr - sum(hours[0,..,l]) > 0, 其中sum(hours[0,..,l]) = curr - 1
            但是需要思考的是，在满足前缀和小于curr的前提下，前缀和curr-1对应的下标l是否是最小下标了，是否还有比curr-1更小的前缀和对应的下标l'更小，即会不会有curr-2，curr-3对应的下标更小。
            这里用反证法证明，假设最早出现curr-2的下标l' < 最早出现curr-1的下标l
            由于curr - 2 <= 0, 最早出现的curr-2只能从curr - 1转移过来，所以curr-1比curr-2先出现，那么l' > l，与假设矛盾
            所以只用查询最早出现curr-1对应的下标即可，假设为l, 那么curr - sum(hours[0,..,l])  == sum(hours[l + 1, ..., r]) > 0
            如果curr-1不存在，那么curr-2， curr-3...也不可能存在
        """
        memo, curr, ans = dict(), 0, 0
        for i, h in enumerate(hours):
            curr += (1 if h > 8 else -1)
            if curr > 0: ans = i + 1
            elif curr - 1 in memo: ans = max(ans, i - memo[curr - 1])  # i - (memo[curr - 1] + 1) + 1
            if curr not in memo: memo[curr] = i
        return ans


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        pre_sum = [0]
        for h in hours:
            pre_sum.append(pre_sum[-1] + (1 if h > 8 else -1))
        stack = []
        for i, h in enumerate(pre_sum):
            if not stack or pre_sum[stack[-1]] > h:
                stack.append(i)
        ans = 0
        for j in range(len(pre_sum) - 1, -1, -1):
            while stack and pre_sum[j] > pre_sum[stack[-1]]:
                ans = max(ans, j - stack.pop())
        return ans
# leetcode submit region end(Prohibit modification and deletion)
hours = [9, 9, 6, 0,  6,  6,  9]
#    [0, 1, 2, 1, 0, -1, -2, -1]
print(Solution().longestWPI(hours))