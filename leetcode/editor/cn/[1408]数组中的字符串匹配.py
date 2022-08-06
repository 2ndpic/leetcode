from typing import List
from itertools import permutations
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i, w1 in enumerate(words):
            for j, w2 in enumerate(words):
                if i != j and w1 in w2:
                    ans.append(w1)
                    break
        return ans

# leetcode submit region end(Prohibit modification and deletion)
