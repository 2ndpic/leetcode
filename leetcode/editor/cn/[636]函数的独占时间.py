from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []
        for log in logs:
            idx, tp, timestamp = log.split(":")
            idx, timestamp = int(idx), int(timestamp)
            if tp[0] == "s":
                if stack:
                    ans[stack[-1][0]] += timestamp - stack[-1][1]
                stack.append([idx, timestamp])
            else:
                i, t = stack.pop()
                ans[i] += timestamp - t + 1
                if stack:
                    stack[-1][1] = timestamp + 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
