# 有 n 个人排成一个队列，从左到右 编号为 0 到 n - 1 。给你以一个整数数组 heights ，每个整数 互不相同，heights[i] 表示第 i
#  个人的高度。 
# 
#  一个人能 看到 他右边另一个人的条件是这两人之间的所有人都比他们两人 矮 。更正式的，第 i 个人能看到第 j 个人的条件是 i < j 且 min(he
# ights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1]) 。 
# 
#  请你返回一个长度为 n 的数组 answer ，其中 answer[i] 是第 i 个人在他右侧队列中能 看到 的 人数 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：heights = [10,6,8,5,11,9]
# 输出：[3,1,2,1,1,0]
# 解释：
# 第 0 个人能看到编号为 1 ，2 和 4 的人。
# 第 1 个人能看到编号为 2 的人。
# 第 2 个人能看到编号为 3 和 4 的人。
# 第 3 个人能看到编号为 4 的人。
# 第 4 个人能看到编号为 5 的人。
# 第 5 个人谁也看不到因为他右边没人。
#  
# 
#  示例 2： 
# 
#  
# 输入：heights = [5,1,2,3,10]
# 输出：[4,1,1,1,0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == heights.length 
#  1 <= n <= 105 
#  1 <= heights[i] <= 105 
#  heights 中所有数 互不相同 。 
#  
#  Related Topics 栈 
#  👍 4 👎 0
from typing import List
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        """
        倒序遍历维护一个单调递减栈
        """
        n = len(heights)
        stack, ans = [], [0] * n
        for i in range(n - 1, -1, -1):
            while stack and heights[i] > stack[-1]:
                stack.pop()
                ans[i] += 1
            if stack: ans[i] += 1
            stack.append(heights[i])
        return ans
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        """
        倒序遍历维护一个单调递减栈
        """
        n = len(heights)
        stack, ans = [], [0] * n
        for i in range(n - 1, -1, -1):
            while stack:
                ans[i] += 1 # i 可以看到j
                if heights[i] > stack[-1]:
                    stack.pop()
                else:
                    break  # i 可以看到j但是看不到j右侧的所有人
            stack.append(heights[i])
        return ans
# leetcode submit region end(Prohibit modification and deletion)
heights = [10,6,8,5,11,9]
print(Solution().canSeePersonsCount(heights))