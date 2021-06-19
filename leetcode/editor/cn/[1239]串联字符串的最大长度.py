# 给定一个字符串数组 arr，字符串 s 是将 arr 某一子序列字符串连接所得的字符串，如果 s 中的每一个字符都只出现过一次，那么它就是一个可行解。 
# 
#  请返回所有可行解 s 中最长长度。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = ["un","iq","ue"]
# 输出：4
# 解释：所有可能的串联组合是 "","un","iq","ue","uniq" 和 "ique"，最大长度为 4。
#  
# 
#  示例 2： 
# 
#  输入：arr = ["cha","r","act","ers"]
# 输出：6
# 解释：可能的解答有 "chaers" 和 "acters"。
#  
# 
#  示例 3： 
# 
#  输入：arr = ["abcdefghijklmnopqrstuvwxyz"]
# 输出：26
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 16 
#  1 <= arr[i].length <= 26 
#  arr[i] 中只含有小写英文字母 
#  
#  Related Topics 位运算 回溯算法 
#  👍 107 👎 0

from typing import List
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def backtrack(pos, mask):
            nonlocal ans
            if pos == len(masks):
                ans = max(ans, bin(mask).count("1"))
                return
            if (mask & masks[pos]) == 0: backtrack(pos + 1, mask | masks[pos])
            backtrack(pos + 1, mask)

        masks = []
        for s in arr:
            mask = 0
            for ch in s:
                idx = ord(ch) - ord('a')
                if (mask >> idx) & 1:
                    mask = 0
                    break
                mask |= 1 << idx
            if mask > 0:
                masks.append(mask)

        ans = 0
        backtrack(0, 0)
        return ans
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks = [0]
        ans = 0
        for s in arr:
            mask = 0
            for ch in s:
                idx = ord(ch) - ord('a')
                if(mask >> idx) & 1:
                    mask = 0
                    break
                mask |= (1 << idx)
            if mask == 0: continue

            for i in range(len(masks)):
                m = masks[i]
                if m & mask == 0:
                    masks.append(m | mask)
                    ans = max(ans, bin(masks[-1]).count("1"))
        return ans
# leetcode submit region end(Prohibit modification and deletion)
arr = ["un","iq","ue"]
arr = ["cha","r","act","ers"]
arr = ["abcdefghijklmnopqrstuvwxyz"]
arr = ["yy","bkhwmpbiisbldzknpm"]
arr = ["jnfbyktlrqumowxd","mvhgcpxnjzrdei"]
print(Solution().maxLength(arr))