# 给你一个整数数组 arr 。 
# 
#  现需要从数组中取三个下标 i、j 和 k ，其中 (0 <= i < j <= k < arr.length) 。 
# 
#  a 和 b 定义如下： 
# 
#  
#  a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1] 
#  b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k] 
#  
# 
#  注意：^ 表示 按位异或 操作。 
# 
#  请返回能够令 a == b 成立的三元组 (i, j , k) 的数目。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [2,3,1,6,7]
# 输出：4
# 解释：满足题意的三元组分别是 (0,1,2), (0,2,2), (2,3,4) 以及 (2,4,4)
#  
# 
#  示例 2： 
# 
#  输入：arr = [1,1,1,1,1]
# 输出：10
#  
# 
#  示例 3： 
# 
#  输入：arr = [2,3]
# 输出：0
#  
# 
#  示例 4： 
# 
#  输入：arr = [1,3,5,7,9]
# 输出：3
#  
# 
#  示例 5： 
# 
#  输入：arr = [7,11,12,9,5,2,7,17,22]
# 输出：8
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 300 
#  1 <= arr[i] <= 10^8 
#  
#  Related Topics 位运算 数组 数学 
#  👍 67 👎 0

from typing import List
import collections
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        """
        超时，时间复杂度O(n^3)
        """
        def check(path):
            i, j, k = path
            if (pre_xor[j] ^ pre_xor[i]) == (pre_xor[k + 1] ^ pre_xor[j]):
                return True
            return False
        def backtracking(start, path):
            nonlocal ans
            if len(path) == 3:
                if check(path):
                    ans += 1
                return
            for i in range(start, len(arr)):
                backtracking(i + (len(path) < 1), path + [i])

        ans = 0
        pre_xor = [0]
        for i in arr:
            pre_xor.append(pre_xor[-1] ^ i)
        backtracking(0, [])
        return ans
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        """
        a == b， 即 a ^ b == 0
        时间复杂度O(n^2),利用哈希表可缩小至O(1)
        """
        ans = 0
        pre_xor = [0]
        for i in arr:
            pre_xor.append(pre_xor[-1] ^ i)

        for i in range(1, len(arr)):
            for k in range(i + 1, len(pre_xor)):
                if pre_xor[i - 1] ^ pre_xor[k] == 0:
                    ans += (k - i)

        return ans

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        """
        a == b， 即 a ^ b == 0
        时间复杂度O(n^2),利用哈希表可缩小至O(1)
        cnt用来记录x出现了好多次，total记录x出现的下标之和
        如果k位置的异或值为x，x在k之前出现位置是i1,i2,i3
        ans += (k - i1 - 1) + (k - i2 - 1) + (k - i3 -1 ) = 3 * (k - 1) - (i1 + i2 + i3) = cnt[x] * (k - 1) - total[x]
        """
        ans, pre_xor = 0, 0
        cnt, total = collections.defaultdict(int), collections.defaultdict(int)
        cnt[0], total[0] = 1, -1
        for k in range(len(arr)):
            pre_xor ^= arr[k]
            ans += (k - 1) * cnt[pre_xor] - total[pre_xor]
            cnt[pre_xor] += 1
            total[pre_xor] += k
        return ans

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans, pre_xor = 0, 0
        cnt, total = collections.defaultdict(int), collections.defaultdict(int)
        for k in range(len(arr)):
            x = pre_xor ^ arr[k]
            ans += k * cnt[x] - total[x]
            cnt[pre_xor] += 1
            total[pre_xor] += k # xor [0,..k) = pre_xor
            pre_xor = x
        return ans

# leetcode submit region end(Prohibit modification and deletion)
arr = [2,3,1,6,7]
# arr = [1,1,1,1,1]
# arr = [2,3]
# arr = [1,3,5,7,9]
# arr = [7,11,12,9,5,2,7,17,22]
print(Solution().countTriplets(arr))