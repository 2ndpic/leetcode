from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        n = max(nums) + 1
        cnt, cnt_freq = [0] * (n + 1), [0] * (len(nums) + 1)
        max_freq = 0
        ans = 0
        for i, v in enumerate(nums):
            cnt[v] += 1
            freq = cnt[v]
            cnt_freq[freq] += 1
            cnt_freq[freq - 1] -= 1
            max_freq = max(max_freq, freq)

            if max_freq == 1: ans = i + 1
            if max_freq * cnt_freq[max_freq] + 1 == i + 1: ans = i + 1
            if (max_freq - 1) * (cnt_freq[max_freq - 1] + 1) + 1 == i + 1: ans = i + 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
