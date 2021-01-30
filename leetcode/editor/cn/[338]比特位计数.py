# 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。 
# 
#  示例 1: 
# 
#  输入: 2
# 输出: [0,1,1] 
# 
#  示例 2: 
# 
#  输入: 5
# 输出: [0,1,1,2,1,2] 
# 
#  进阶: 
# 
#  
#  给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？ 
#  要求算法的空间复杂度为O(n)。 
#  你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。 
#  
#  Related Topics 位运算 动态规划 
#  👍 431 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        """
        后面的奇数一定比前面的偶数多个1，因为偶数最低位肯定是0
        偶数一定跟比他自己小一倍的偶数的1的个数一样多，因为*2就是二进制右移后面添个0
        """
        
        ret = [0 for _ in range(num+1)]
        for i in range(1, num+1):
            ret[i] = ret[i >> 1] + (i & 1)
        return ret
        
# leetcode submit region end(Prohibit modification and deletion)
