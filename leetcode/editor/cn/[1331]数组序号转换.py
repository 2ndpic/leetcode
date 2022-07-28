from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # arr_sort = sorted(arr)
        # memo = {}
        # index = 1
        # for v in arr_sort:
        #     if v not in memo:
        #         memo[v] = index
        #         index += 1
        # return [memo[v] for v in arr]
        # arr_sort = sorted([(i, v) for i, v in enumerate(arr)], key=lambda x: x[1])
        # ans = [0] * len(arr)
        # count, pre_v = 0, 0
        # for i, v in arr_sort:
        #     if i == 0 or v != pre_v:
        #         count += 1
        #         pre_v = v
        #     ans[i] = count
        # return ans
        memo = {v: i for i, v in enumerate(sorted(set(arr)), 1)}
        return [memo[v] for v in arr]
# leetcode submit region end(Prohibit modification and deletion)
print(Solution().arrayRankTransform([37,12,28,9,100,56,80,5,12]))