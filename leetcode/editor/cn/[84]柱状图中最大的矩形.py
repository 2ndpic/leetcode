# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。 
# 
#  求在该柱状图中，能够勾勒出来的矩形的最大面积。 
# 
#  
# 
#  
# 
#  以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。 
# 
#  
# 
#  
# 
#  图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。 
# 
#  
# 
#  示例: 
# 
#  输入: [2,1,5,6,2,3]
# 输出: 10 
#  Related Topics 栈 数组 
#  👍 1263 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        1.此题的本质是找到每个柱形条左边和右边最近的比自己低的矩形条，然后用宽度乘上当前柱形条的高度就是以当前柱形条作为矩形高的矩形,作为备选答案。
        2.解决此类问题的经典做法是单调栈，维护一个单调递增的栈，
            如果当前柱形条i的高度比栈顶要低，则栈顶元素cur出栈。
                出栈后，cur右边第一个比它低的柱形条就是i，左边第一个比它低的柱形条是当前栈中的top,pop出去计算得到的就是以cur作为矩形高的矩形面积
            不断出栈直到栈为空或者柱形条i不再比top低。
        3.满足2之后，当前矩形条i进栈
        4.所有元素都要入栈出栈一次，所以时间复杂度O(n)

        注意：实际上由于重复元素的存在，pop出来的元素在计算以其为高的面积的时候并不是准确的，但是可以保证最大值是准确的
        """
        # 为了最后所有元素出栈方便，heights数组末尾添加高度-1
        res = 0
        heights.append(-1)  # 加了一个最小值，可以保证栈中所有元素出栈，这样每个元素作为高都计算得到一个矩形了
        stack = []  # 单调递增栈,里面存的索引
        for i in range(len(heights)):
            while stack and heights[i] <= heights[stack[-1]]:
                cur = heights[stack.pop()]
                if stack:
                    res = max(res, cur * (i - stack[-1] - 1))  # i - (stack[-1] + 1)
                else:
                    res = max(res, cur * i)  # 此时cur前面没有元素了，自己画图体会下

            stack.append(i)
        return res
# leetcode submit region end(Prohibit modification and deletion)
