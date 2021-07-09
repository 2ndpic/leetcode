# 数组中占比超过一半的元素称之为主要元素。给你一个 整数 数组，找出其中的主要元素。若没有，返回 -1 。请设计时间复杂度为 O(N) 、空间复杂度为 O(1
# ) 的解决方案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：[1,2,5,9,5,9,5,5,5]
# 输出：5 
# 
#  示例 2： 
# 
#  
# 输入：[3,2]
# 输出：-1 
# 
#  示例 3： 
# 
#  
# 输入：[2,2,1,1,1,2,2]
# 输出：2 
#  Related Topics 数组 计数 
#  👍 147 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = -1, 0
        for i in nums:
            if count == 0:
                candidate = i
            count += 1 if i == candidate else -1
        count = 0
        for i in nums:
            if i == candidate:
                count += 1
        return candidate if count * 2 > len(nums) else -1
# leetcode submit region end(Prohibit modification and deletion)
