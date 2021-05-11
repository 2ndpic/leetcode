# 给你一个整数数组 perm ，它是前 n 个正整数的排列，且 n 是个 奇数 。 
# 
#  它被加密成另一个长度为 n - 1 的整数数组 encoded ，满足 encoded[i] = perm[i] XOR perm[i + 1] 。比方说
# ，如果 perm = [1,3,2] ，那么 encoded = [2,1] 。 
# 
#  给你 encoded 数组，请你返回原始数组 perm 。题目保证答案存在且唯一。 
# 
#  
# 
#  示例 1： 
# 
#  输入：encoded = [3,1]
# 输出：[1,2,3]
# 解释：如果 perm = [1,2,3] ，那么 encoded = [1 XOR 2,2 XOR 3] = [3,1]
#  
# 
#  示例 2： 
# 
#  输入：encoded = [6,5,4,6]
# 输出：[2,4,1,5,3]
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= n < 105 
#  n 是奇数。 
#  encoded.length == n - 1 
#  
#  Related Topics 位运算 
#  👍 47 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        odd = 0
        for i in encoded[1::2]:
            odd ^= i
        a = 0
        for i in range(len(encoded) + 1):
            a ^= (i + 1)
        ans = [a ^ odd]
        for i in encoded:
            ans.append(ans[-1] ^ i)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
