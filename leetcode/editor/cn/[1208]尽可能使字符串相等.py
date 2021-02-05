# 给你两个长度相同的字符串，s 和 t。 
# 
#  将 s 中的第 i 个字符变到 t 中的第 i 个字符需要 |s[i] - t[i]| 的开销（开销可能为 0），也就是两个字符的 ASCII 码值的差的
# 绝对值。 
# 
#  用于变更字符串的最大预算是 maxCost。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。 
# 
#  如果你可以将 s 的子字符串转化为它在 t 中对应的子字符串，则返回可以转化的最大长度。 
# 
#  如果 s 中没有子字符串可以转化成 t 中对应的子字符串，则返回 0。
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "abcd", t = "bcdf", cost = 3
# 输出：3
# 解释：s 中的 "abc" 可以变为 "bcd"。开销为 3，所以最大长度为 3。 
# 
#  示例 2： 
# 
#  输入：s = "abcd", t = "cdef", cost = 3
# 输出：1
# 解释：s 中的任一字符要想变成 t 中对应的字符，其开销都是 2。因此，最大长度为 1。
#  
# 
#  示例 3： 
# 
#  输入：s = "abcd", t = "acde", cost = 0
# 输出：1
# 解释：你无法作出任何改动，所以最大长度为 1。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length, t.length <= 10^5 
#  0 <= maxCost <= 10^6 
#  s 和 t 都只含小写英文字母。 
#  
#  Related Topics 数组 Sliding Window 
#  👍 59 👎 0
def s1(s: str, t: str, maxCost: int) -> int:
    """
    转化思路：
    在maxCost为0的情况下，任务就是找到s和t中的共同子串，注意不是子序列，比如"aacddd"和"aabccc"maxCost=0，答案是3
    在maxCost有值的情况下，“共同子串”被定义为s和t的位置对应的两个字串ASCII差的绝对值之和不超过maxCost
    所以可以利用滑动窗口
    """
    l, r, cur_cost, res = 0, 0, 0, -1
    f = lambda x, y: abs(ord(x) - ord(y))
    while r < len(s):
        cur_cost += f(s[r], t[r])
        while cur_cost > maxCost:
            cur_cost -= f(s[l], t[l])
            l += 1
        res = max(res, r - l + 1)
        r += 1
    return res
def s2(s: str, t: str, maxCost: int) -> int:
    l, cur_cost, diff = 0, 0, [abs(ord(x)-ord(y)) for x, y in zip(s, t)]
    for r in range(len(s)):
        cur_cost += diff[r]
        if cur_cost > maxCost:
            cur_cost -= diff[l]
            l += 1
    return r - l + 1
# leetcode submit region begin(Prohibit modification and deletion)
def check(arr, length, cost):
    for i in range(length, len(arr)):
        if arr[i] - arr[i-length] <= cost:
            return True
    return False

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l, cur_cost, pre_sum = 0, 0, [0]
        for i in range(len(s)):
            pre_sum.append(pre_sum[-1] + abs(ord(s[i])-ord(t[i])))
        lo, hi = 0, len(s) # 二分答案,lo,hi代表长度,小于等于答案的长度都合法，大于答案的长度不合法
        while lo < hi:
            mid = (lo + hi) // 2
            if check(pre_sum, mid, maxCost): lo = mid + 1
            else: hi = mid
        return lo if check(pre_sum, lo, maxCost) else lo - 1

# leetcode submit region end(Prohibit modification and deletion)
s = "abcd"
t = "bcdf"
cost = 3
print(Solution().equalSubstring(s, t, cost))
