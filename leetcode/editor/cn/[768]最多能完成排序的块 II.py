from typing import List
from collections import defaultdict
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for i in arr:
            if not stack or stack[-1] <= i:
                stack.append(i)
            else:
                mx = stack[-1]
                while stack and stack[-1] > i:
                    stack.pop()
                stack.append(mx)
        return len(stack)

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        cnt, ans = defaultdict(int), 0
        for a, b in zip(arr, sorted(arr)):
            cnt[a] += 1
            cnt[b] -= 1
            if cnt[a] == 0:
                del cnt[a]
            if cnt[b] == 0:
                del cnt[b]
            if len(cnt) == 0:
                ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)
