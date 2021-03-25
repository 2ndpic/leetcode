# 给你一个整数数组 nums ，数组中共有 n 个整数。132 模式的子序列 由三个整数 nums[i]、nums[j] 和 nums[k] 组成，并同时满足
# ：i < j < k 和 nums[i] < nums[k] < nums[j] 。 
# 
#  如果 nums 中存在 132 模式的子序列 ，返回 true ；否则，返回 false 。 
# 
#  
# 
#  进阶：很容易想到时间复杂度为 O(n^2) 的解决方案，你可以设计一个时间复杂度为 O(n logn) 或 O(n) 的解决方案吗？ 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3,4]
# 输出：false
# 解释：序列中不存在 132 模式的子序列。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,1,4,2]
# 输出：true
# 解释：序列中有 1 个 132 模式的子序列： [1, 4, 2] 。
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [-1,3,2,0]
# 输出：true
# 解释：序列中有 3 个 132 模式的的子序列：[-1, 3, 2]、[-1, 3, 0] 和 [-1, 2, 0] 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == nums.length 
#  1 <= n <= 104 
#  -109 <= nums[i] <= 109 
#  
#  Related Topics 栈 
#  👍 473 👎 0

from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """
        超时。数据量在O(10^5)。时间复杂度O(n^2)
        """
        for i in range(len(nums)):
            stack = [nums[i]]
            for j in nums[i + 1:]:
                if len(stack) == 1:
                    if j < stack[-1]:
                        stack.pop()
                    stack.append(j)
                elif len(stack) == 2:
                    if j > stack[-1]:
                        stack.pop()
                        stack.append(j)
                    elif stack[-2] < j < stack[-1]:
                        stack.append(j)
                if len(stack) == 3:
                    return True
        return False
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """
        直觉告诉我这是一个单调栈解决的问题。
        先固定一个数
        - 如果枚举i，需要找到jk对，所以需要从后往前遍历。
            找jk对转换为找k，在[i,k]区间内存在大于k的j，要利用k知道j的存在，就需要维护一个单调栈
            这个单调栈的性质在于k被更新，必须j比k大，所以维护一个单调递减栈（栈顶最小）
            一旦k被更新了，就知道是有一个比k更大的数把一个数从单调栈pop出来了。
            所以只用比较i和k的值即可，k比i大即存在j比i大 and j 必大于 k
        """
        stack = []
        k = float('-inf')
        for i in nums[::-1]:
            if k > i:
                return True
            while stack and i > stack[-1]:
                k = stack.pop()
            stack.append(i)
        return False
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """
        直觉告诉我这是一个单调栈解决的问题。
        先固定一个数
        - 如果枚举j，
            由于 j 是 132 结构里最大的数，因此我们需要在 j 的右边中比 j 小的「最大」的数，
            在 j 的左边找比 j 小的「最小」的数。
            这很容易联想到单调栈，但是朴素的单调栈是帮助我们找到左边或者右边「最近」的数，无法直接满足我们「最大」和「最小」的要求，需要引入额外逻辑。
        """
        mj = []     # mi 维护 nums[i] 左侧的最小值,mi是有单调减的（栈顶最小）
        stack = []  # 维护 nums[i] 右侧比 mi[i] 大的值
        for j in nums:
            if not mj:
                mj.append(j)
            else:
                mj.append(min(mj[-1], j))
        for j in range(len(nums)-1, -1, -1):
            if nums[j] > mj[j]:
                """
                现在nums[j]右边找一个比mi[j]大的元素
                如果栈顶比mi[j]要小，之后肯定也不会用到了，丢掉（因为mi越往左走越大）
                栈顶坐标>j,mj[j]坐标小于j，如果nums[j]的值比栈顶大，就直接返回了
                """
                while stack and stack[-1] <= mj[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
        return False



# leetcode submit region end(Prohibit modification and deletion)
nums = [1,2,3,4]
# nums = [3,1,4,2]
# nums = [-1,3,2,0]
# nums = [3,5,0,3,4] # True
print(Solution().find132pattern(nums))