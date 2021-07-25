# 存在一个由 n 个不同元素组成的整数数组 nums ，但你已经记不清具体内容。好在你还记得 nums 中的每一对相邻元素。 
# 
#  给你一个二维整数数组 adjacentPairs ，大小为 n - 1 ，其中每个 adjacentPairs[i] = [ui, vi] 表示元素 ui
#  和 vi 在 nums 中相邻。 
# 
#  题目数据保证所有由元素 nums[i] 和 nums[i+1] 组成的相邻元素对都存在于 adjacentPairs 中，存在形式可能是 [nums[i]
# , nums[i+1]] ，也可能是 [nums[i+1], nums[i]] 。这些相邻元素对可以 按任意顺序 出现。 
# 
#  返回 原始数组 nums 。如果存在多种解答，返回 其中任意一个 即可。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：adjacentPairs = [[2,1],[3,4],[3,2]]
# 输出：[1,2,3,4]
# 解释：数组的所有相邻元素对都在 adjacentPairs 中。
# 特别要注意的是，adjacentPairs[i] 只表示两个元素相邻，并不保证其 左-右 顺序。
#  
# 
#  示例 2： 
# 
#  
# 输入：adjacentPairs = [[4,-2],[1,4],[-3,1]]
# 输出：[-2,4,1,-3]
# 解释：数组中可能存在负数。
# 另一种解答是 [-3,1,4,-2] ，也会被视作正确答案。
#  
# 
#  示例 3： 
# 
#  
# 输入：adjacentPairs = [[100000,-100000]]
# 输出：[100000,-100000]
#  
# 
#  
# 
#  提示： 
# 
#  
#  nums.length == n 
#  adjacentPairs.length == n - 1 
#  adjacentPairs[i].length == 2 
#  2 <= n <= 105 
#  -105 <= nums[i], ui, vi <= 105 
#  题目数据保证存在一些以 adjacentPairs 作为元素对的数组 nums 
#  
#  Related Topics 数组 哈希表 
#  👍 87 👎 0

from typing import List
from collections import defaultdict
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        memo = set()
        for u, v in adjacentPairs:
            if u in memo: memo.remove(u)
            else: memo.add(u)
            if v in memo: memo.remove(v)
            else: memo.add(v)
        ans = [memo.pop()]
        memo = defaultdict(int)
        for i, (u, v) in enumerate(adjacentPairs):
            memo[u] += i
            memo[v] += i
        prev = 0
        i = 0
        while i < len(adjacentPairs):
            idx = memo[ans[-1]] - prev
            nxt = sum(adjacentPairs[idx]) - ans[-1]
            ans.append(nxt)
            i += 1
            prev = idx
        return ans
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        for u, v in adjacentPairs:
            mp[u].append(v)
            mp[v].append(u)
        n = len(adjacentPairs) + 1
        ans = [0] * n
        for e, adj in mp.items():
            if len(adj) == 1:
                ans[0] = e
                break
        ans[1] = mp[ans[0]][0]
        for i in range(2, n):
            adj = mp[ans[i - 1]]
            ans[i] = adj[0] if ans[i - 2] != adj[0] else adj[1]
        return ans
# leetcode submit region end(Prohibit modification and deletion)
