# 已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。 
# 
#  在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，使数组变为 [nums[k], nums
# [k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,
# 2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。 
# 
#  给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 nums 中存在这个目标值 targ
# et ，则返回 true ，否则返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,5,6,0,0,1,2], target = 0
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,5,6,0,0,1,2], target = 3
# 输出：false 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 5000 
#  -104 <= nums[i] <= 104 
#  题目数据保证 nums 在预先未知的某个下标上进行了旋转 
#  -104 <= target <= 104 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  这是 搜索旋转排序数组 的延伸题目，本题中的 nums 可能包含重复元素。 
#  这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？ 
#  
#  Related Topics 数组 二分查找 
#  👍 334 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        因为重复元素的存在，nums[0]和nums[-1]的值可能相同而丧失二段性
        所以先去除首尾两端的重复元素恢复二段性，保证:左半段 >= nums[0]，右半段 <nums[0]
        然后再去找旋转点,判断target在左半段还是右半段
        """
        l, r = 0, len(nums) - 1
        while l < r and nums[l] == nums[r]:
            if nums[l] == target: return True
            l, r = l + 1, r - 1
        lo, hi = l, r + 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[l]: hi = mid
            else: lo = mid + 1
        lo, hi = (l, lo) if target >= nums[l] else (lo, r + 1)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target: hi = mid
            elif nums[mid] < target: lo = mid + 1
            else: return True
        return False

# leetcode submit region end(Prohibit modification and deletion)
nums = [2,5,6,7,0,0,1,2]
nums = [2,5,6,0,0,1,2]
nums = [1, 2, 3, 4, 5]
nums = [1,2,2,3,1]
nums = [1,0,1,1,1]
target = 0
print(Solution().search(nums, target))