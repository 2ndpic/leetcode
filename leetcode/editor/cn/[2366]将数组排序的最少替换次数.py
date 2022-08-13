from  typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n, ans, m = len(nums), 0, nums[-1]
        for i in range(n - 2, -1, -1):
            x = (nums[i] + m - 1) // m
            ans += x - 1
            m = nums[i] // x
        return ans
# leetcode submit region end(Prohibit modification and deletion)
