# 给定两个以 升序排列 的整数数组 nums1 和 nums2 , 以及一个整数 k 。 
# 
#  定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2 。 
# 
#  请找到和最小的 k 个数对 (u1,v1), (u2,v2) ... (uk,vk) 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# 输出: [1,2],[1,4],[1,6]
# 解释: 返回序列中的前 3 对数：
#      [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
#  
# 
#  示例 2: 
# 
#  
# 输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# 输出: [1,1],[1,1]
# 解释: 返回序列中的前 2 对数：
#      [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
#  
# 
#  示例 3: 
# 
#  
# 输入: nums1 = [1,2], nums2 = [3], k = 3 
# 输出: [1,3],[2,3]
# 解释: 也可能序列中所有的数对都被返回:[1,3],[2,3]
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= nums1.length, nums2.length <= 10⁵ 
#  -10⁹ <= nums1[i], nums2[i] <= 10⁹ 
#  nums1 和 nums2 均为升序排列 
#  1 <= k <= 1000 
#  
#  Related Topics 数组 堆（优先队列） 👍 325 👎 0
from typing import List
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        q = [(nums1[i] + nums2[0], i, 0) for i in range(min(m, k))]
        ans = []
        while q and len(ans) < k:
            _, x, y = heapq.heappop(q)
            ans.append([nums1[x], nums2[y]])
            if y + 1 < n: heapq.heappush(q, (nums1[x] + nums2[y + 1], x, y + 1))
        return ans

    # leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n, lo, hi = len(nums1), len(nums2), nums1[0] + nums2[0], nums1[-1] + nums2[-1]
        while lo < hi:
            mid = (lo + hi) // 2
            pos1, pos2, cnt = 0, n - 1, 0
            while pos1 < m and pos2 >= 0:
                if nums1[pos1] + nums2[pos2] > mid:
                    pos2 -= 1
                else:
                    cnt += pos2 + 1
                    pos1 += 1
            if cnt < k: lo = mid + 1
            else: hi = mid
        ans = []
        # 找到数对和小于lo的数对
        i = n - 1
        for num1 in nums1:
            while i >= 0 and num1 + nums2[i] >= lo:
                i -= 1
            for j in range(i + 1):
                ans.append([num1, nums2[j]])
                if len(ans) == k: return ans
        # 找到数对和小于lo的数对
        i = n - 1
        for num1 in nums1:
            while i >= 0 and num1 + nums2[i] > lo:
                i -= 1
            j = i
            while j >= 0 and num1 + nums2[j] == lo:
                ans.append([num1, nums2[j]])
                if len(ans) == k: return ans
                j -= 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
nums1 = [0,0,0,0,0]
nums2 = [-3,22,35,56,76]
k = 22
print(Solution().kSmallestPairs(nums1, nums2, k))