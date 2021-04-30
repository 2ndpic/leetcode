# 给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,2,3,2]
# 输出：3
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1,0,1,0,1,99]
# 输出：99
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 3 * 104 
#  -231 <= nums[i] <= 231 - 1 
#  nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 
#  
# 
#  
# 
#  进阶：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？ 
#  Related Topics 位运算 
#  👍 608 👎 0

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        将每个数用二进制数相加，相同位数上的加法采用十进制，
        最后对每一位对3取余，转成10进制就是答案
        因为如果都是三个数，那么每一位加起来的数字都应该是3的倍数
        """
        ans = 0
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)
            if total % 3:
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = b = 0
        for num in nums:
            a, b = (~a & b & num) | (a & ~b & ~num), ~a & (b ^ num)
        return b
# leetcode submit region end(Prohibit modification and deletion)
nums = [2,2,3,2]
nums = [0,1,0,1,0,1,99]
nums = [-2,-2,1,1,4,1,4,4,-4,-2]
print(Solution().singleNumber(nums))