# 给你一个二进制字符串 s 。你可以按任意顺序执行以下两种操作任意次： 
# 
#  
#  类型 1 ：删除 字符串 s 的第一个字符并将它 添加 到字符串结尾。 
#  类型 2 ：选择 字符串 s 中任意一个字符并将该字符 反转 ，也就是如果值为 '0' ，则反转得到 '1' ，反之亦然。 
#  
# 
#  请你返回使 s 变成 交替 字符串的前提下， 类型 2 的 最少 操作次数 。 
# 
#  我们称一个字符串是 交替 的，需要满足任意相邻字符都不同。 
# 
#  
#  比方说，字符串 "010" 和 "1010" 都是交替的，但是字符串 "0100" 不是。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "111000"
# 输出：2
# 解释：执行第一种操作两次，得到 s = "100011" 。
# 然后对第三个和第六个字符执行第二种操作，得到 s = "101010" 。
#  
# 
#  示例 2： 
# 
#  输入：s = "010"
# 输出：0
# 解释：字符串已经是交替的。
#  
# 
#  示例 3： 
# 
#  输入：s = "1110"
# 输出：1
# 解释：对第二个字符执行第二种操作，得到 s = "1010" 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 105 
#  s[i] 要么是 '0' ，要么是 '1' 。 
#  
#  Related Topics 贪心算法 数组 
#  👍 19 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minFlips(self, s: str) -> int:
        s = s + s
        n = len(s)
        s0 = "".join([str(i % 2) for i in range(n)])
        s1 = "".join([str((i + 1) % 2) for i in range(n)])
        l = 0
        cnt0 = 0
        cnt1 = 0
        ans = n
        for r in range(n):
            cnt0 += (s0[r] != s[r])
            cnt1 += (s1[r] != s[r])
            if r - l + 1 > n // 2:
               cnt0 -= (s0[l] != s[l])
               cnt1 -= (s1[l] != s[l])
               l += 1
            if r - l + 1 == n // 2:
                ans = min(ans, cnt0, cnt1)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
s = "111000"
print(Solution().minFlips(s))