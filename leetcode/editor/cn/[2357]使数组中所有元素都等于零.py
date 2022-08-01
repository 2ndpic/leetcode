from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = set(nums)
        return len(nums) - (0 in nums)

# leetcode submit region end(Prohibit modification and deletion)
