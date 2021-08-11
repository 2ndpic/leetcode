# 给你一个整数数组 nums ，返回 nums 中所有 等差子序列 的数目。 
# 
#  如果一个序列中 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该序列为等差序列。 
# 
#  
#  例如，[1, 3, 5, 7, 9]、[7, 7, 7, 7] 和 [3, -1, -5, -9] 都是等差序列。 
#  再例如，[1, 1, 2, 5, 7] 不是等差序列。 
#  
# 
#  数组中的子序列是从数组中删除一些元素（也可能不删除）得到的一个序列。 
# 
#  
#  例如，[2,5,10] 是 [1,2,1,2,4,1,5,10] 的一个子序列。 
#  
# 
#  题目数据保证答案是一个 32-bit 整数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,4,6,8,10]
# 输出：7
# 解释：所有的等差子序列为：
# [2,4,6]
# [4,6,8]
# [6,8,10]
# [2,4,6,8]
# [4,6,8,10]
# [2,4,6,8,10]
# [2,6,10]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [7,7,7,7,7]
# 输出：16
# 解释：数组中的任意子序列都是等差子序列。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 1000 
#  -231 <= nums[i] <= 231 - 1 
#  
#  Related Topics 数组 动态规划 
#  👍 171 👎 0
from typing import List
from collections import defaultdict
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        官解。定义至少两个元素的等差子序列为弱等差项
        f[i][d]表示尾项为nums[i]公差为d的弱等差序列的个数
        f[i][d] = sum(f[j][d] + 1)  nums[i] - nums[j] = d and j < i
        由于题目要统计的等差子序列至少有三个元素
        将nums[i]加到以nums[j]为尾项公差为d的弱等差子序列末尾，这一操作，实际上就构成了至少三个元素的等差子序列
        因此将循环中的f[j][d]累加即为答案
        由于nums[i]的范围很大，所以第二维会很大，可以用hash表代替
        """
        ans = 0
        f = [defaultdict(int) for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                d = nums[i] - nums[j]
                f[i][d] += f[j][d] + 1
                ans += f[j][d]
        return ans
# leetcode submit region end(Prohibit modification and deletion)
