# 给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是 nums[i] 右侧小于 num
# s[i] 的元素的数量。 
# 
#  
# 
#  示例： 
# 
#  输入：nums = [5,2,6,1]
# 输出：[2,1,1,0] 
# 解释：
# 5 的右侧有 2 个更小的元素 (2 和 1)
# 2 的右侧仅有 1 个更小的元素 (1)
# 6 的右侧有 1 个更小的元素 (1)
# 1 的右侧有 0 个更小的元素
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 10^5 
#  -10^4 <= nums[i] <= 10^4 
#  
#  Related Topics 排序 树状数组 线段树 二分查找 分治算法 
#  👍 586 👎 0

from typing import List
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        N = 20050
        c = [0] * N
        n = len(nums)
        def lowbit(x):
            return x & (-x)
        def update(i):
            while i <= N:
                c[i] += 1
                i += lowbit(i)
        def query(i):
            ans = 0
            while i:
                ans += c[i]
                i -= lowbit(i)
            return ans
        ans = [0] * n
        for i in range(len(nums), 0, -1):
            ans[i - 1] = query(nums[i - 1] -1 + 10009)
            update(nums[i - 1] + 10009)
        return ans

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def f(idx):
            pass
        n = len(nums)
        ans = [0] * n
        for i in range(n-1, -1, -1):
            ans[i] = f(i)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
nums = [5,2,6,1]
print(Solution().countSmaller(nums))