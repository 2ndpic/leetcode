# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        """
        假设现在轮到s[i]参与前向组成子串，由于是连续的，因此s[i]参与组成的子串除了s[i]本身成一个字符子串外
        其余的子串必定是与s[i-1]前向组成的所有子串 + s[i]，研究s[i]与s[i-1]的贡献值是求解本题的关键
        我们可以维护两个索引，分别是是s[i]字母出现的距离当前最近的两个位置a与b
        那么[0,a]段大家贡献一致，即以s[i-1]结尾的所有前向子串中(s[k,...,i-1])
                              和以s[i]结尾的所有前向子串（s[k,...,i]）,
                              对于s[i]字符来说都是重复的，贡献为0
        [a + 1, b]段s[i]前向子串贡献比s[i-1]贡献少，少(b-a)个
        [b + 1,i]段s[i]前向子串贡献比s[i-1]贡献多， 多(i-b)个
        那么设s[i-1]前向子串的贡献值为K，那么s[i]前向子串的贡献为K+(i-b)-(b-a)，其中a，b分别为距离最近i的字母s[i]出现的先后两个位置
        为了适配a与b还不存在的情况，将a与b都初始化为-1，递推式不变方便计算
        """
        curr, ans = 0, 0
        memo = [[-1, -1] for _ in range(26)]
        for i, ch in enumerate(s):
            m = memo[ord(ch) - ord('A')]
            curr += (i - m[1]) - (m[1] - m[0])
            m[0], m[1] = m[1], i
            ans += curr
        return ans

# leetcode submit region end(Prohibit modification and deletion)
