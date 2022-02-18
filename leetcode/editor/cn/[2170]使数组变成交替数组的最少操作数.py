# 给你一个下标从 0 开始的数组 nums ，该数组由 n 个正整数组成。 
# 
#  如果满足下述条件，则数组 nums 是一个 交替数组 ： 
# 
#  
#  nums[i - 2] == nums[i] ，其中 2 <= i <= n - 1 。 
#  nums[i - 1] != nums[i] ，其中 1 <= i <= n - 1 。 
#  
# 
#  在一步 操作 中，你可以选择下标 i 并将 nums[i] 更改 为 任一 正整数。 
# 
#  返回使数组变成交替数组的 最少操作数 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [3,1,3,2,4,3]
# 输出：3
# 解释：
# 使数组变成交替数组的方法之一是将该数组转换为 [3,1,3,1,3,1] 。
# 在这种情况下，操作数为 3 。
# 可以证明，操作数少于 3 的情况下，无法使数组变成交替数组。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,2,2,2]
# 输出：2
# 解释：
# 使数组变成交替数组的方法之一是将该数组转换为 [1,2,1,2,1].
# 在这种情况下，操作数为 2 。
# 注意，数组不能转换成 [2,2,2,2,2] 。因为在这种情况下，nums[0] == nums[1]，不满足交替数组的条件。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  1 <= nums[i] <= 10⁵ 
#  
#  Related Topics 贪心 数组 哈希表 计数 👍 17 👎 0
from typing import List
from collections import Counter
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def get(start):
            """
            :param start: 0表示偶数下标，1表示奇数下标
            :return: 最大次数对应的值, 最大次，次大次数对应的值, 次大次数
            """
            freq = Counter(nums[start::2])
            best = freq.most_common(2)
            if not best:
                return 0, 0, 0, 0
            if len(best) == 1:
                return *best[0], 0, 0
            return *best[0], *best[1]

        n = len(nums)
        e1k, e1v, e2k, e2v = get(0)
        o1k, o1v, o2k, o2v = get(1)
        if e1k != o1k: return n - e1v - o1v
        return n - max(e1v + o2v, e2v + o1v)
# leetcode submit region end(Prohibit modification and deletion)
