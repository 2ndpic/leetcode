# 给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。 
# 
#  请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。 
# 
#  nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
# 输出: [-1,3,-1]
# 解释:
#     对于 num1 中的数字 4 ，你无法在第二个数组中找到下一个更大的数字，因此输出 -1 。
#     对于 num1 中的数字 1 ，第二个数组中数字1右边的下一个较大数字是 3 。
#     对于 num1 中的数字 2 ，第二个数组中没有下一个更大的数字，因此输出 -1 。 
# 
#  示例 2: 
# 
#  
# 输入: nums1 = [2,4], nums2 = [1,2,3,4].
# 输出: [3,-1]
# 解释:
#     对于 num1 中的数字 2 ，第二个数组中的下一个较大数字是 3 。
#     对于 num1 中的数字 4 ，第二个数组中没有下一个更大的数字，因此输出 -1 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums1.length <= nums2.length <= 1000 
#  0 <= nums1[i], nums2[i] <= 104 
#  nums1和nums2中所有整数 互不相同 
#  nums1 中的所有整数同样出现在 nums2 中 
#  
# 
#  
# 
#  进阶：你可以设计一个时间复杂度为 O(nums1.length + nums2.length) 的解决方案吗？ 
#  Related Topics 栈 
#  👍 379 👎 0

from typing import List
"""
当然，直接两层循环暴力求解可以出结果， 这个题目也可以ac，复杂度是O(N^2)。但是这个当然不是我们需要讨论的。
先从几个小数据的特殊例子开始：
[1,2,3]—> [2,3,-1]
[3,2,1]—> [-1,-1,-1]
[1,2,3,2]—> [2,3,-1,-1]
[3,2,1,4]—> [4,4,4,4]

从上面例子可以看到，
* 如果数组是一个单调递增的数组， 那么每个index的结果就是index+1的结果。
* 如果数组是一个单调递减的数组，那么每个index的结果都是-1。
* 如果数组是前面是单调递增的，后面变成其他数，可以看到前面的结果不受影响。因为对于任何一个数来说，只要遇到一个比他大的数，结果就确定了。
* 如果数组前面是单调递减的，后面遇到更大的数，可以看到前面所有的结果都可能会受到影响。
也就是说:
    如果数组在从左向右遍历的过程中，如果遇到了一个更大的数，那结果当时就可以完全确定下来。 
    如果遇到更小的数，结果就暂时不能确定，直到遇到一个更大的数才可以确定。而且，在遇到一个更大的数的时候，会可能影响到前面几个单调递减的数的结果。

那么，我们可以用一个stack来保存暂时不能出结果的数（默认结果都是-1），也就数单调递减的数，然后遇到一个更大数的时候，就可以把前面的更小数都算出结果，pop出来。
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        memo = {}
        stack = []
        for i in nums2:
            while stack and i > stack[-1]:
                memo[stack.pop()] = i
            stack.append(i)
        while stack:
            memo[stack.pop()] = -1
        return [memo[i] for i in nums1]
    """
    stack, memo = [], {}
        for i in nums2:
            while stack and i > stack[-1]:
                memo[stack.pop()] = i
            stack.append(i)
        return [memo.get(i, -1) for i in nums1]
    """
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        除了上面实现的从左往右遍历，还可以从右往左遍历
        如果每次遇到一个数，比stack.top()要大， 那么stack.top()已经不需要了， 因为左边剩下的元素的值遇到的第一个大数一定最少是当前数，而不可能是stack.top(),
            所以可以直接pop。
        但是nums2[i] < stack.top()的时候，也就直接压栈， 因为有可能两个数分别是左边不同数的结果
        比如[3,1,2,8,7,6]， 从右向左遍历的时候, 压栈和出栈的顺序可以体会一下
        """
        stack, memo = [], {}
        for i in nums2[::-1]:
            while stack and i > stack[-1]:
                j = stack.pop()
                memo[j] = stack[-1] if stack else -1
            else:
                stack.append(i)
        while stack:
            j = stack.pop()
            memo[j] = stack[-1] if stack else -1
        return [memo[i] for i in nums1]
    """
    stack, memo = [], {}
        for i in nums2[::-1]:
            while stack and i > stack[-1]:
                stack.pop()
            if stack:
                memo[i] = stack[-1]
            stack.append(i)
        return [memo.get(i, -1) for i in nums1]
    """
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        如果不给nums1，直接让返回所有位置的呢？
        """
        ans = [-1] * len(nums2)
        stack = []
        for idx, v in enumerate(nums2):
            while stack and v > stack[-1][1]:
                ans[stack.pop()[0]] = v
            stack.append((idx, v))
        return ans

# leetcode submit region end(Prohibit modification and deletion)
nums1 = [3,1,7]
nums2 = [3,1,2,8,7,6]
print(Solution().nextGreaterElement(nums1, nums2))