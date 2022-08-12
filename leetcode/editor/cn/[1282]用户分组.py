from typing import List
from collections import defaultdict
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        memo = defaultdict(list)
        for i, gs in enumerate(groupSizes):
            memo[gs].append(i)
            if len(memo[gs]) == gs:
                ans.append(memo[gs])
                memo[gs] = []
        return ans

# leetcode submit region end(Prohibit modification and deletion)
