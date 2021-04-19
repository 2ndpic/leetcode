# 列表的 异或和（XOR sum）指对所有元素进行按位 XOR 运算的结果。如果列表中仅有一个元素，那么其 异或和 就等于该元素。 
# 
#  
#  例如，[1,2,3,4] 的 异或和 等于 1 XOR 2 XOR 3 XOR 4 = 4 ，而 [3] 的 异或和 等于 3 。 
#  
# 
#  给你两个下标 从 0 开始 计数的数组 arr1 和 arr2 ，两数组均由非负整数组成。 
# 
#  根据每个 (i, j) 数对，构造一个由 arr1[i] AND arr2[j]（按位 AND 运算）结果组成的列表。其中 0 <= i < arr1.l
# ength 且 0 <= j < arr2.length 。 
# 
#  返回上述列表的 异或和 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr1 = [1,2,3], arr2 = [6,5]
# 输出：0
# 解释：列表 = [1 AND 6, 1 AND 5, 2 AND 6, 2 AND 5, 3 AND 6, 3 AND 5] = [0,1,2,0,2,1]
#  ，
# 异或和 = 0 XOR 1 XOR 2 XOR 0 XOR 2 XOR 1 = 0 。 
# 
#  示例 2： 
# 
#  输入：arr1 = [12], arr2 = [4]
# 输出：4
# 解释：列表 = [12 AND 4] = [4] ，异或和 = 4 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr1.length, arr2.length <= 105 
#  0 <= arr1[i], arr2[j] <= 109 
#  
#  Related Topics 数学 
#  👍 12 👎 0

from typing import List
class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        if len(arr1) < len(arr2):
            arr1, arr2 = arr2, arr1
        arr2xor = 0
        for i in arr2:
            arr2xor ^= i
        ans = 0
        for i in arr1:
            ans = ans ^ (i & arr2xor)
        return ans
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        """
        a&c ^ b&c = (a^b) & c
        考虑结果的每一位是什么，对第i位：
            1、假设c是0，那么左边 a&c=a&0=0, b&c=b&0=0, a&c ^ b&c=0^0=0；右边(a^b)&c=(a^b)&0=0，左边=右边
            2、假设c是1，那么左边 a&c=a&1=a, b&c=b&1=b, a&c ^ b&c=a^b；右边(a^b)&c=(a^b)&1=a^b，左边=右边，证毕。
        """
        arr1_xor, arr2_xor = 0, 0
        for i in arr1:
            arr1_xor ^= i
        for i in arr2:
            arr2_xor ^= i
        return arr1_xor & arr2_xor
# leetcode submit region end(Prohibit modification and deletion)
arr1 = [1,2,3]
arr2 = [6,5]
# arr1 = [12]
# arr2 = [4]
print(Solution().getXORSum(arr1, arr2))