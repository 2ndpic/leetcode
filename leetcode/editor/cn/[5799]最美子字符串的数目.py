# 如果某个字符串中 至多一个 字母出现 奇数 次，则称其为 最美 字符串。 
# 
#  
#  例如，"ccjjc" 和 "abab" 都是最美字符串，但 "ab" 不是。 
#  
# 
#  给你一个字符串 word ，该字符串由前十个小写英文字母组成（'a' 到 'j'）。请你返回 word 中 最美非空子字符串 的数目。如果同样的子字符串在
#  word 中出现多次，那么应当对 每次出现 分别计数。 
# 
#  子字符串 是字符串中的一个连续字符序列。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：word = "aba"
# 输出：4
# 解释：4 个最美子字符串如下所示：
# - "aba" -> "a"
# - "aba" -> "b"
# - "aba" -> "a"
# - "aba" -> "aba"
#  
# 
#  示例 2： 
# 
#  
# 输入：word = "aabb"
# 输出：9
# 解释：9 个最美子字符串如下所示：
# - "aabb" -> "a"
# - "aabb" -> "aa"
# - "aabb" -> "aab"
# - "aabb" -> "aabb"
# - "aabb" -> "a"
# - "aabb" -> "abb"
# - "aabb" -> "b"
# - "aabb" -> "bb"
# - "aabb" -> "b"
#  
# 
#  示例 3： 
# 
#  
# 输入：word = "he"
# 输出：2
# 解释：2 个最美子字符串如下所示：
# - "he" -> "h"
# - "he" -> "e"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= word.length <= 105 
#  word 由从 'a' 到 'j' 的小写英文字母组成 
#  
#  Related Topics 位运算 字符串 
#  👍 26 👎 0
from collections import Counter
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        """
        由于只关心子字符串每个字母出现次数的奇偶性，所以用一个位数为10的二进制串表示
        二进制串的第i位为0表示第i个小写字母出现了偶数次，为1表示第i个小写字母出现了奇数次
        考虑字母出现次数的前缀和，由于只考虑奇偶性，也可以视为长为10的二进制串。
        此时计算前缀和由加法改为异或运算(1^1=0, 0^1=1,0^0=0)，刚好奇偶性的变化
        若有两个不同下标的前缀和相同，则这两个前缀和的异或结果为0，对应子串的各个字母的个数均为偶数，附和题目要求
        因此可以在求前缀和的同时，用一个长为2^10=1024的cnt数组统计每个前缀和二进制串出现的次数，从而得到相同前缀和，即各个字母的个数均为偶数的子串个数
        还允许有一个字母出现奇数次，这需要我们寻找两个前缀和，其异或结果的二进制数中恰好有个1，对应子串的各个字母个数仅有一个为奇数
            对此我们可以枚举当前前缀和的每个比特，将其反转，然后去cnt中查找该前缀和的出现次数
        时间复杂度：O(10n),n=len(word)
        """
        cnt = [1] + [0] * 1023
        ans, pre = 0, 0
        for ch in word:
            pre ^= (1 << (ord(ch) - ord('a')))
            ans += cnt[pre]          # 子串所有字母均出现偶数次
            for i in range(10):      # 枚举其中一个字母出现奇数次
                ans += cnt[pre ^ (1 << i)]
            cnt[pre] += 1
        return ans

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        freq = Counter([0])
        mask, ans = 0, 0
        for ch in word:
            mask ^= (1 << (ord(ch) - ord('a')))
            ans += freq[mask]
            for i in range(10):
                mask_i = mask ^ (1 << i)
                ans += freq[mask_i]
            freq[mask] += 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
word = "aba"
print(Solution().wonderfulSubstrings(word))