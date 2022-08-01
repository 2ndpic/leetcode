from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        return int((2 * n + 0.25) ** 0.5 - 0.5)
# leetcode submit region end(Prohibit modification and deletion)
