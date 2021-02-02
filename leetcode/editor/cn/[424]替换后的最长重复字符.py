# 给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。
#  
# 
#  注意：字符串长度 和 k 不会超过 104。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "ABAB", k = 2
# 输出：4
# 解释：用两个'A'替换为两个'B',反之亦然。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "AABABBA", k = 1
# 输出：4
# 解释：
# 将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
# 子串 "BBBB" 有最长重复字母, 答案为 4。
#  
#  Related Topics 双指针 Sliding Window 
#  👍 248 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


def s1(s: str, k: int) -> int:
    l, r, res = 0, 0, 0
    d = defaultdict(int)
    while r < len(s):
        d[s[r]] += 1
        while l < r and (r - l + 1 - max(d.values()) > k):
            d[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
        r += 1
    return res
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, res = 0, 0, 0
        d = defaultdict(int)
        max_char_num = 0
        while r < len(s):
            d[s[r]] += 1
            max_char_num = max(max_char_num, d[s[r]])
            while r - l + 1 - max_char_num > k:
                d[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
s = "ABAB"
k = 1
print(Solution().characterReplacement(s, k))

"""
比如说"AAABCDEDFG" k=2，这个case，一开始A出现3次,max_count=3，
但是当指针移到D时发现不行了，要移动left指针了。
此时count['A']-=1，但是不需要把max_count更新为2。为什么呢？ 
因为根据我们的算法，当max_count和k一定时，区间最大长度也就定了。
当我们找到一个max_count之后，我们就能说我们找到了一个长度为d=max_count+k的合法区间，所以最终答案一定不小于d。
所以，当发现继续向右扩展right不合法的时候，我们不需要不断地右移left，只需要保持区间长度为d向右滑动即可。
如果有某个合法区间大于d，一定在某个时刻存在count[t]+1>max_count，这时再去更新max_count即可。
"""