# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。 
# 
#  换句话说，第一个字符串的排列之一是第二个字符串的子串。 
# 
#  示例1: 
# 
#  
# 输入: s1 = "ab" s2 = "eidbaooo"
# 输出: True
# 解释: s2 包含 s1 的排列之一 ("ba").
#  
# 
#  
# 
#  示例2: 
# 
#  
# 输入: s1= "ab" s2 = "eidboaoo"
# 输出: False
#  
# 
#  
# 
#  注意： 
# 
#  
#  输入的字符串只包含小写字母 
#  两个字符串的长度都在 [1, 10,000] 之间 
#  
#  Related Topics 双指针 Sliding Window 
#  👍 246 👎 0
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l2 < l1:
            return False
        s1_memo = [0 for _ in range(26)]
        s2_memo = [0 for _ in range(26)]
        for i, j in zip(s1, s2):
            s1_memo[ord(i) - ord('a')] += 1
            s2_memo[ord(j) - ord('a')] += 1
        if s1_memo == s2_memo:
            return True

        for i in range(len(s1), len(s2)):
            s2_memo[ord(s2[i - l1]) - ord('a')] -= 1
            s2_memo[ord(s2[i]) - ord('a')] += 1
            if s1_memo == s2_memo:
                return True
        return False
import collections
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = [0] * 26
        for i in s1:
            cnt[ord(i) - ord('a')] += 1
        ws = len(s1)
        cmt = [0] * 26
        for i in range(len(s2)):
            cmt[ord(s2[i]) - ord('a')] += 1
            if i >= ws:
                cmt[ord(s2[i - ws]) - ord('a')] -= 1
            if cmt == cnt: return True
        return False
# leetcode submit region end(Prohibit modification and deletion)
s1 = "aba"
s2 = "eidbaooo"
print(Solution().checkInclusion(s1, s2))