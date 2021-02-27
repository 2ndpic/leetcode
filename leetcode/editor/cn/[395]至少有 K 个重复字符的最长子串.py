# 给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串， 要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aaabb", k = 3
# 输出：3
# 解释：最长子串为 "aaa" ，其中 'a' 重复了 3 次。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "ababbc", k = 2
# 输出：5
# 解释：最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 104 
#  s 仅由小写英文字母组成 
#  1 <= k <= 105 
#  
#  Related Topics 递归 分治算法 Sliding Window 
#  👍 313 👎 0
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(i, k) for i in s.split(c))
        return len(s)

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """
        假设字符种类数量为c的最长子串长度为t
            长度大于t的子串字符数量必然大于c
            长度小于等于t的子串字符种类必然小于等于c的
        然后去枚举字符种类数量，从[1, 26]，对每个种类数量c二分计算得到最长子串长度t，如果这个子串恰好满足题目条件的话，就去更新答案

        给定窗口的字符种类，双指针恢复了单调性

        双指针不具备单调性 -> 限定字符种类 -> 双指针恢复单调性
        """
        ans = 0
        for i in range(1, 27):
            cnt = [0] * 26
            l, r, char_types, char_appk = 0, 0, 0, 0
            while r < len(s):
                char_index = ord(s[r]) - ord('a')
                cnt[char_index] += 1
                if cnt[char_index] == 1:
                    char_types += 1
                if cnt[char_index] == k:
                    char_appk += 1

                while char_types > i:
                    char_index = ord(s[l]) - ord('a')
                    cnt[char_index] -= 1
                    if cnt[char_index] == 0:
                        char_types -= 1
                    if cnt[char_index] == k - 1:
                        char_appk -= 1
                    l += 1
                if char_appk == char_types:
                    ans = max(ans, r - l + 1)
                r += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)
s = "bbaaacbd"
k = 3
print(Solution().longestSubstring(s, k))