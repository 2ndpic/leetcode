# 对于给定的整数 n, 如果n的k（k>=2）进制数的所有数位全为1，则称 k（k>=2）是 n 的一个好进制。 
# 
#  以字符串的形式给出 n, 以字符串的形式返回 n 的最小好进制。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入："13"
# 输出："3"
# 解释：13 的 3 进制是 111。
#  
# 
#  示例 2： 
# 
#  
# 输入："4681"
# 输出："8"
# 解释：4681 的 8 进制是 11111。
#  
# 
#  示例 3： 
# 
#  
# 输入："1000000000000000000"
# 输出："999999999999999999"
# 解释：1000000000000000000 的 999999999999999999 进制是 11。
#  
# 
#  
# 
#  提示： 
# 
#  
#  n的取值范围是 [3, 10^18]。 
#  输入总是有效且没有前导 0。 
#  
# 
#  
#  Related Topics 数学 二分查找 
#  👍 107 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        """
        设进制数为k，数位为s + 1，那么有s越大，k越小的反比关系
        因为n>=3，所以数位必大于等于2，当数为为2时，k ** 1 + k **0 = n,k=n-1
        因为k<=10 ** 18,数为最多为（k最小为2）log2(10 ** 18)= 59
        假设正整数n在k进制下的所有数位都为1，且位数为s + 1,那么有
        k ** s + k ** (s - 1) + ... + k ** 1 + k ** 0 = n
        必然有 k**s < n
        根据二项式定理
        (k + 1) ** s = k ** s + C(s, 1)k**(s - 1) +...+ C(S, S-1)k + 1 > n
        有 k ** s < n < (k + 1) ** s --> k < n ** (1 / s) < k + 1
        因为 s + 1 == 数位，已知数位的上限是59， 下线是2，所以只用枚举s即可
        数位越大，k越小，所以将数位从大到小枚举
        """
        n = int(n)
        ans = n - 1
        for s in range(59, 1, -1):
            k = int(n ** (1 / s))
            if k > 1:
                tmp, mul = 1, 1
                for _ in range(s):
                    mul *= k
                    tmp += mul
                if tmp == n:
                    ans = k
                    break
        return str(ans)
# leetcode submit region end(Prohibit modification and deletion)
n = "13"
print(Solution().smallestGoodBase(n))