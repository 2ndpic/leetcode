# 给定一个整数数组 A，坡是元组 (i, j)，其中 i < j 且 A[i] <= A[j]。这样的坡的宽度为 j - i。 
# 
#  找出 A 中的坡的最大宽度，如果不存在，返回 0 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[6,0,8,2,1,5]
# 输出：4
# 解释：
# 最大宽度的坡为 (i, j) = (1, 5): A[1] = 0 且 A[5] = 5.
#  
# 
#  示例 2： 
# 
#  输入：[9,8,1,0,1,9,4,0,4,1]
# 输出：7
# 解释：
# 最大宽度的坡为 (i, j) = (2, 9): A[2] = 1 且 A[9] = 1.
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= A.length <= 50000 
#  0 <= A[i] <= 50000 
#  
# 
#  
#  Related Topics 栈 数组 单调栈 👍 149 👎 0
from typing import List
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        """
        暴力枚举ij超时
        固定i，j从后向前遍历，if nums[j] >= nums[i]，更新答案后就可以中止了继续i+1的遍历
        对于i < i1，如果nums[i1] >= nums[i]，那么(i1, j)不可能作为答案
        - 若nums[j] >= nums[i1] >= nums[i]，那么(i, j)作为答案是优于(i1, j)
        - 若nums[j] < nums[i1]，那么根据答案定义，(i1, j)不可能是答案
        所以利用严格递减单调栈先来记录每个可能成为答案的i
        然后j从后向前遍历，在栈中寻找满足nums[j] >= nums[i]的i， 将满足的i用来更新答案并且弹出，因为此时的(i, j)相较于后面可能合法的(i, j - x)是更优答案
        时间复杂度O(N)
        """
        stack = []
        for i, v in enumerate(nums):
            if not stack or v < nums[stack[-1]]:
                stack.append(i)
        ans = 0
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                ans = max(ans, j - stack.pop())
        return ans

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ans, m = 0, float('inf')
        for i in sorted(range(len(nums)), key=lambda x: nums[x]):
            ans = max(ans, i - m)
            m = min(m, i)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
nums = [6,0,8,2,1,5]
print(Solution().maxWidthRamp(nums))