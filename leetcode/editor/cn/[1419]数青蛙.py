# 给你一个字符串 croakOfFrogs，它表示不同青蛙发出的蛙鸣声（字符串 "croak" ）的组合。由于同一时间可以有多只青蛙呱呱作响，所以 croak
# OfFrogs 中会混合多个 “croak” 。请你返回模拟字符串中所有蛙鸣所需不同青蛙的最少数目。 
# 
#  注意：要想发出蛙鸣 "croak"，青蛙必须 依序 输出 ‘c’, ’r’, ’o’, ’a’, ’k’ 这 5 个字母。如果没有输出全部五个字母，那么它
# 就不会发出声音。 
# 
#  如果字符串 croakOfFrogs 不是由若干有效的 "croak" 字符混合而成，请返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：croakOfFrogs = "croakcroak"
# 输出：1 
# 解释：一只青蛙 “呱呱” 两次
#  
# 
#  示例 2： 
# 
#  
# 输入：croakOfFrogs = "crcoakroak"
# 输出：2 
# 解释：最少需要两只青蛙，“呱呱” 声用黑体标注
# 第一只青蛙 "crcoakroak"
# 第二只青蛙 "crcoakroak"
#  
# 
#  示例 3： 
# 
#  
# 输入：croakOfFrogs = "croakcrook"
# 输出：-1
# 解释：给出的字符串不是 "croak" 的有效组合。
#  
# 
#  示例 4： 
# 
#  
# 输入：croakOfFrogs = "croakcroa"
# 输出：-1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= croakOfFrogs.length <= 10^5 
#  字符串中的字符只有 'c', 'r', 'o', 'a' 或者 'k' 
#  
#  Related Topics 字符串 
#  👍 45 👎 0

import heapq
import math
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        d = {v : i + 1 for i, v in enumerate("croak")}
        memo = [0] * 6 # ["", "c", "cr", "cro", "croa", "croak"]
        nums = 0
        for c in croakOfFrogs:
            i = d[c]
            if d[c] == 1:
                memo[i] += 1
            elif not memo[i - 1]:
                return -1
            else:
                memo[i - 1] -= 1
                memo[i] += 1
            nums = max(nums, sum(memo[1:5]))
        return nums if sum(memo[1:5]) == 0 else -1

# leetcode submit region end(Prohibit modification and deletion)
# croakOfFrogs = "croakcroak" # 1
croakOfFrogs = "crcoakroak" # 2
# croakOfFrogs = "croakcrook" # -1
# croakOfFrogs = "croakcroa"  # -1
print(Solution().minNumberOfFrogs(croakOfFrogs))