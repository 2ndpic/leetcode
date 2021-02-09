# 给定一个正整数数组 A，如果 A 的某个子数组中不同整数的个数恰好为 K，则称 A 的这个连续、不一定独立的子数组为好子数组。 
# 
#  （例如，[1,2,3,1,2] 中有 3 个不同的整数：1，2，以及 3。） 
# 
#  返回 A 中好子数组的数目。 
# 
#  
# 
#  示例 1： 
# 
#  输入：A = [1,2,1,2,3], K = 2
# 输出：7
# 解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
#  
# 
#  示例 2： 
# 
#  输入：A = [1,2,1,3,4], K = 3
# 输出：3
# 解释：恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 20000 
#  1 <= A[i] <= A.length 
#  1 <= K <= A.length 
#  
#  Related Topics 哈希表 双指针 Sliding Window 
#  👍 188 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
def f(arr, k):
    res = [0 for _ in range(len(arr))]
    l, pos = 0, 0
    memo = dict()
    for r in range(len(arr)):
        """
        从[0,..,r]找到最小的下标pos
        使得[pos,...,r]这个区间的不同元素为k个
        即[pos-1,...,r]不同元素为target+1个
        若[0,..,r]区间的不同元素没有target个的话，pos=0
        问题转化为: 要在[0,...,r]区间找到以r元素结尾时拥有k个不同元素的最长区间下标pos
        """
        memo[arr[r]] = memo.setdefault(arr[r], 0) + 1
        while len(memo) > k:      # len()操作是O(1)时间复杂度
            memo[arr[l]] -= 1
            if memo[arr[l]] == 0:
                del memo[arr[l]]  # 该元素在区间中统计为0次了，删除后，len(memo)才是[l,...,r]区间不同元素个数
            l += 1
        res[r] = l
    return res

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        l, r, res = 0, 0, 0
        far_k = f(A, K)
        far_k_sub = f(A, K - 1)

        for i in range(len(A)):
            res += far_k_sub[i] - far_k[i]
        return res


# leetcode submit region end(Prohibit modification and deletion)
A = [1,2,1,2,3]
K = 2
#
A = [1,2,1,3,4]
K = 3
print(Solution().subarraysWithKDistinct(A, K))
