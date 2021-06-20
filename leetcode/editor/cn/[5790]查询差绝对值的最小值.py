# 一个数组 a 的 差绝对值的最小值 定义为：0 <= i < j < a.length 且 a[i] != a[j] 的 |a[i] - a[j]| 的 最
# 小值。如果 a 中所有元素都 相同 ，那么差绝对值的最小值为 -1 。 
# 
#  
#  比方说，数组 [5,2,3,7,2] 差绝对值的最小值是 |2 - 3| = 1 。注意答案不为 0 ，因为 a[i] 和 a[j] 必须不相等。 
#  
# 
#  给你一个整数数组 nums 和查询数组 queries ，其中 queries[i] = [li, ri] 。对于每个查询 i ，计算 子数组 nums[
# li...ri] 中 差绝对值的最小值 ，子数组 nums[li...ri] 包含 nums 数组（下标从 0 开始）中下标在 li 和 ri 之间的所有元素（
# 包含 li 和 ri 在内）。 
# 
#  请你返回 ans 数组，其中 ans[i] 是第 i 个查询的答案。 
# 
#  子数组 是一个数组中连续的一段元素。 
# 
#  |x| 的值定义为： 
# 
#  
#  如果 x >= 0 ，那么值为 x 。 
#  如果 x < 0 ，那么值为 -x 。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,3,4,8], queries = [[0,1],[1,2],[2,3],[0,3]]
# 输出：[2,1,4,1]
# 解释：查询结果如下：
# - queries[0] = [0,1]：子数组是 [1,3] ，差绝对值的最小值为 |1-3| = 2 。
# - queries[1] = [1,2]：子数组是 [3,4] ，差绝对值的最小值为 |3-4| = 1 。
# - queries[2] = [2,3]：子数组是 [4,8] ，差绝对值的最小值为 |4-8| = 4 。
# - queries[3] = [0,3]：子数组是 [1,3,4,8] ，差的绝对值的最小值为 |3-4| = 1 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [4,5,2,2,7,10], queries = [[2,3],[0,2],[0,5],[3,5]]
# 输出：[-1,1,1,3]
# 解释：查询结果如下：
# - queries[0] = [2,3]：子数组是 [2,2] ，差绝对值的最小值为 -1 ，因为所有元素相等。
# - queries[1] = [0,2]：子数组是 [4,5,2] ，差绝对值的最小值为 |4-5| = 1 。
# - queries[2] = [0,5]：子数组是 [4,5,2,2,7,10] ，差绝对值的最小值为 |4-5| = 1 。
# - queries[3] = [3,5]：子数组是 [2,7,10] ，差绝对值的最小值为 |7-10| = 3 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= nums.length <= 105 
#  1 <= nums[i] <= 100 
#  1 <= queries.length <= 2 * 104 
#  0 <= li < ri < nums.length 
#  
#  Related Topics 数组 
#  👍 9 👎 0
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        """
        pre[i][c]表示考虑nums前i个元素包含元素c的个数
        那么对于区间[i,..,j]是否存在元素c,可表示为pre[j+1][c] - pre[i][c] > 0
        那么就从1-100遍历相邻元素更新最小差绝对值
        """
        n = len(nums)
        pre = [[0] * 101 for _ in range(n + 1)]
        for i in range(1, n + 1):
            pre[i][nums[i - 1]] = pre[i - 1][nums[i - 1]] + 1
            if i + 1 < n + 1:
                pre[i + 1] = pre[i][:]

        ans = []
        for i, j in queries:
            cur = None
            tmp = 1000
            for num in range(1, 101):
                if pre[j + 1][num] - pre[i][num] > 0:
                    if cur is not None:
                        tmp = min(tmp, num - cur)
                    cur = num
            ans.append(tmp if tmp < 1000 else -1)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
nums = [1,3,4,8]; queries = [[0,1],[1,2],[2,3],[0,3]]
print(Solution().minDifference(nums, queries))