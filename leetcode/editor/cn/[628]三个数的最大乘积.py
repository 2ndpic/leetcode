# 给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。 
# 
#  示例 1: 
# 
#  
# 输入: [1,2,3]
# 输出: 6
#  
# 
#  示例 2: 
# 
#  
# 输入: [1,2,3,4]
# 输出: 24
#  
# 
#  注意: 
# 
#  
#  给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。 
#  输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。 
#  
#  Related Topics 数组 数学 
#  👍 219 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
def s1(nums: List[int]) -> int:
    b1, b2, b3, f1, f2 = -2000, -2000, -2000, 0, 0
    for i in nums:
        if i > b3:
            b1, b2, b3 = b2, b3, i
        elif i > b2:
            b1, b2 = b2, i
        elif i > b1:
            b1 = i
        if i < f1:
            f1, f2 = i, f1
        elif i < f2:
            f2 = i
    return max(f1 * f2 * b3, b1 * b2 * b3)

def s2(nums):
    nums.sort()
    return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        b1, b2, b3, f1, f2 = -2000, -2000, -2000, 0, 0
        for i in nums:
            if i > b3:
                b1, b2, b3 = b2, b3, i
            elif i > b2:
                b1, b2 = b2, i
            elif i > b1:
                b1 = i
            if i < f1:
                f1, f2 = i, f1
            elif i < f2:
                f2 = i
        return max(f1 * f2 * b3, b1 * b2 * b3)
# leetcode submit region end(Prohibit modification and deletion)
