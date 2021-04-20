# 实现 strStr() 函数。 
# 
#  给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如
# 果不存在，则返回 -1 。 
# 
#  
# 
#  说明： 
# 
#  当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。 
# 
#  对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：haystack = "hello", needle = "ll"
# 输出：2
#  
# 
#  示例 2： 
# 
#  
# 输入：haystack = "aaaaa", needle = "bba"
# 输出：-1
#  
# 
#  示例 3： 
# 
#  
# 输入：haystack = "", needle = ""
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= haystack.length, needle.length <= 5 * 104 
#  haystack 和 needle 仅由小写英文字符组成 
#  
#  Related Topics 双指针 字符串 
#  👍 819 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        KMP算法
        next_arr[i]保存needle[0,..,i-1]范围内的最长前缀后缀匹配长度
        '''
        def get_index_of(s, m, arr):
            i, j = 0, 0
            while i < len(s) and j < len(m):
                if j == -1 or s[i] == m[j]:
                    i += 1
                    j += 1
                else:
                    j = arr[j]
            return i - j if j == len(m) else -1
        def get_next_arr(m):
            next_arr = [-1] * (len(m) + 1)
            pos = 0
            cn = -1
            while pos < len(m):
                #cn当前保存的是最长前缀后缀匹配长度
                if cn == -1 or m[pos] == m[cn]:
                    cn += 1
                    pos += 1
                    next_arr[pos] = cn
                else:
                    cn = next_arr[cn]
            return next_arr

        next_arr = get_next_arr(needle)
        return get_index_of(haystack, needle, next_arr)
# leetcode submit region end(Prohibit modification and deletion)
haystack = "hello"
needle = "ll"
print(Solution().strStr(haystack, needle))