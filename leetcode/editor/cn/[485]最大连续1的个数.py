# 给定一个二进制数组， 计算其中最大连续1的个数。 
# 
#  示例 1: 
# 
#  
# 输入: [1,1,0,1,1,1]
# 输出: 3
# 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
#  
# 
#  注意： 
# 
#  
#  输入的数组只包含 0 和1。 
#  输入数组的长度是正整数，且不超过 10,000。 
#  
#  Related Topics 数组 
#  👍 184 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        nums.append("#")
        for i in nums:
            if i == 1:
                cur += 1
            else:
                res = max(res, cur)
                cur = 0
        return res
        
# leetcode submit region end(Prohibit modification and deletion)
