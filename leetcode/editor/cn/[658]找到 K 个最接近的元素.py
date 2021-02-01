# 给定一个排序好的数组 arr ，两个整数 k 和 x ，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。 
# 
#  整数 a 比整数 b 更接近 x 需要满足： 
# 
#  
#  |a - x| < |b - x| 或者 
#  |a - x| == |b - x| 且 a < b 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：arr = [1,2,3,4,5], k = 4, x = 3
# 输出：[1,2,3,4]
#  
# 
#  示例 2： 
# 
#  
# 输入：arr = [1,2,3,4,5], k = 4, x = -1
# 输出：[1,2,3,4]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= arr.length 
#  1 <= arr.length <= 104 
#  数组里的每个元素与 x 的绝对值不超过 104 
#  
#  Related Topics 二分查找 
#  👍 180 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
def bisect_left(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x: lo = mid + 1
        else: hi = mid
    return lo

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lo, hi = 0, len(arr) - 1
        while hi - lo + 1 > k:
            if abs(arr[lo] - x) <= abs(arr[hi] - x):
                hi -= 1
            else:
                lo += 1
        return arr[lo:lo + k]

# leetcode submit region end(Prohibit modification and deletion)
arr = [1,2,3,4,5]
k = 2
x = 3
print(Solution().findClosestElements(arr, k, x))