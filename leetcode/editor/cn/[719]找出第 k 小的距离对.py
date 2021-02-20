# 给定一个整数数组，返回所有数对之间的第 k 个最小距离。一对 (A, B) 的距离被定义为 A 和 B 之间的绝对差值。 
# 
#  示例 1: 
# 
#  
# 输入：
# nums = [1,3,1]
# k = 1
# 输出：0 
# 解释：
# 所有数对如下：
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# 因此第 1 个最小距离的数对是 (1,1)，它们之间的距离为 0。
#  
# 
#  提示: 
# 
#  
#  2 <= len(nums) <= 10000. 
#  0 <= nums[i] < 1000000. 
#  1 <= k <= len(nums) * (len(nums) - 1) / 2. 
#  
#  Related Topics 堆 数组 二分查找 
#  👍 150 👎 0

from typing import List
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # 超时
        ans = [0] * (10**6) # 下标是距离，值代表此距离存在多少个数对，0代表不存在数对
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                ans[abs(nums[i] - nums[j])] += 1
        for i in range(10**6):
            k -= ans[i]
            if k <= 0:
                return i
# leetcode submit region begin(Prohibit modification and deletion)
def get_dis_pairs(arr, dis):
    l, ans = 0, 0
    for r in range(len(arr)):
        while arr[r] - arr[l] > dis:
            l += 1
        ans += (r - l)
    return ans

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        lo, hi = 0, nums[-1] - nums[0] + 1
        while lo < hi:
            mid = (lo + hi) // 2
            count = get_dis_pairs(nums, mid)
            if count < k: lo = mid + 1
            else: hi = mid
        return lo
# leetcode submit region end(Prohibit modification and deletion)
nums = [2,3,4,5,6,10,20]
k = 1
print(Solution().smallestDistancePair(nums, k))

"""
采用双指针法 总共遍历n+j次
for i in range(1，n) 以每个nums[i]为较大数, 判断可以产生多少个小于等于mid的距离，把它们累加起来即可
具体做法： 如果对于每个i，如果能得到 j为起始坐标，刚好满足nums[i] - nums[j] <=mid, 那么对于nums[i], 有（i - j）个距离对符合要求。（因为是刚好满足，所以对于下标小于j的数字 ，与nums[i]的距离会增大，就大于mid了）

举个例子： 1 2 3 3 5 j i mid = 2 如果j在位置0，i在位置3，那么以nums[i]为较大数可以产生3个（i - j）小于等于mid的距离，[1 3], [2 3], [3 3]
这样当i遍历完所有的数字后，所有小于等于mid的距离的个数就求出来了，即count

这里注意，对于每个nums[i]，j无需从头遍历，因为nums[i]-nums[j]<= mid的首尾下标i,j是刚好满足条件时的值
那么我们得到nums[i]-nums[j-1]肯定不满足条件，即nums[i] - nums[j-1] > mid
那么nums[i+1]-nums[j-1]距离只会更大，所以只需要判断nums[i+1]-nums[j]能否满足条件了
所以找count的时间复杂度为O(len(nums)+max(j))， max(j)为i= nums[n-1]时，刚好满足条件nums[n-1]-nums[j]<=mid时的下标j。 伪代码如下：

"""