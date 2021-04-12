# 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。 
# 
#  注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [10,2]
# 输出："210" 
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,30,34,5,9]
# 输出："9534330"
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1]
# 输出："1"
#  
# 
#  示例 4： 
# 
#  
# 输入：nums = [10]
# 输出："10"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 100 
#  0 <= nums[i] <= 109 
#  
#  Related Topics 排序 
#  👍 540 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
def all_num(n):
    ans = [0] * 20
    m = 1000000000
    i = 0
    while m:
        if m > n:
            m //= 10
            continue
        ans[i] = (n // m) % 10
        i += 1
        m //= 10
    for j in range(i, 20):
        ans[j] = ans[0 + j - i]
    return ans
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if nums.count(0) == len(nums): return "0"
        nums.sort(key=lambda x: all_num(x), reverse=True)
        return "".join(str(i) for i in nums)
# leetcode submit region end(Prohibit modification and deletion)
nums = [3,30,34,5,9]
# nums = [23, 2]
# nums = [432,43243]
# nums = [34323,3432]
# print(first_num(11))
# nums = [64, 645]
nums = [0, 0, 0]
print(Solution().largestNumber(nums))