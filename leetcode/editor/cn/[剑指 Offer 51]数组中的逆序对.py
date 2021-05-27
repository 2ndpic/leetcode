# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [7,5,6,4]
# 输出: 5 
# 
#  
# 
#  限制： 
# 
#  0 <= 数组长度 <= 50000 
#  👍 421 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(arr, l, m, r):
            i, j, k, ans = 0, 0, l, 0
            left, right = arr[l:m], arr[m:r]
            while i < m - l and j < r - m:
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                    ans += (m - l - i)
                k += 1
            arr[k:r] = left[i:] or right[j:]
            return ans
        def mergeSort(arr, l, r):
            if r - l == 1: return 0
            m = (l + r) // 2
            ans = mergeSort(arr, l, m) + mergeSort(arr, m, r)
            ans += merge(arr, l, m, r)
            return ans

        return mergeSort(nums, 0, len(nums)) if nums else 0
# leetcode submit region end(Prohibit modification and deletion)
nums = [7,5,6,4]
# nums = []
print(Solution().reversePairs(nums))