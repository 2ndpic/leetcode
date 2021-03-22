# 给你一个 严格升序排列 的正整数数组 arr 和一个整数 k 。 
# 
#  请你找到这个数组里第 k 个缺失的正整数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [2,3,4,7,11], k = 5
# 输出：9
# 解释：缺失的正整数包括 [1,5,6,8,9,10,12,13,...] 。第 5 个缺失的正整数为 9 。
#  
# 
#  示例 2： 
# 
#  输入：arr = [1,2,3,4], k = 2
# 输出：6
# 解释：缺失的正整数包括 [5,6,7,...] 。第 2 个缺失的正整数为 6 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 1000 
#  1 <= arr[i] <= 1000 
#  1 <= k <= 1000 
#  对于所有 1 <= i < j <= arr.length 的 i 和 j 满足 arr[i] < arr[j] 
#  
#  Related Topics 数组 哈希表 
#  👍 39 👎 0

from typing import List
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
        不缺少数据的数组，下标和值满足 i + 1 == arr[i] (数组递增从1开始的)
        若缺少数据，下标和值满足 i + 1 < arr[i] 即 arr[i] - i - 1 > 0
        若遍历到缺少一个，arr[i] - i - 1 == 1
        若遍历到缺少两个，arr[i] - i - 1 == 2
        """
        for i in range(len(arr)):
            if arr[i] - i - 1 >= k:
                return k + i
        return k + len(arr)
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
        在上面的基础上二分
        """
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] - mid - 1 < k: lo = mid + 1
            else: hi = mid
        return lo + k
# leetcode submit region end(Prohibit modification and deletion)
arr = [2,3,4,7,11]
k = 5
# arr = [1,2,3,4]
# k = 2
print(Solution().findKthPositive(arr, k))