# 给你一个整数 n，请返回长度为 n 、仅由元音 (a, e, i, o, u) 组成且按 字典序排列 的字符串数量。 
# 
#  字符串 s 按 字典序排列 需要满足：对于所有有效的 i，s[i] 在字母表中的位置总是与 s[i+1] 相同或在 s[i+1] 之前。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 1
# 输出：5
# 解释：仅由元音组成的 5 个字典序字符串为 ["a","e","i","o","u"]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 2
# 输出：15
# 解释：仅由元音组成的 15 个字典序字符串为
# ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"]
# 注意，"ea" 不是符合题意的字符串，因为 'e' 在字母表中的位置比 'a' 靠后
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 33
# 输出：66045
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 50 
#  
#  Related Topics 数学 动态规划 回溯算法 
#  👍 48 👎 0
class Solution:
    def countVowelStrings(self, n: int) -> int:
        def backtracking(start, idx):
            if start == n:
                ans[0] += 1
                return

            for i in range(idx, 5):
                backtracking(start + 1, i)

        ans = [0]
        backtracking(0, 0)
        return ans[0]

class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1] * 5
        # for i in range(2, n + 1):
        #     for j in range(5):
        #         dp[j] = sum(dp[j:])
        for i in range(2, n + 1):
            for j in range(3, -1, -1):
                dp[j] = dp[j] + dp[j + 1]
        return sum(dp)
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countVowelStrings(self, n: int) -> int:
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24
# leetcode submit region end(Prohibit modification and deletion)
print(Solution().countVowelStrings(33))