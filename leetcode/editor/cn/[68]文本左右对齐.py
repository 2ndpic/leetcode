# 给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。 
# 
#  你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。 
# 
#  要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。 
# 
#  文本的最后一行应为左对齐，且单词之间不插入额外的空格。 
# 
#  说明: 
# 
#  
#  单词是指由非空格字符组成的字符序列。 
#  每个单词的长度大于 0，小于等于 maxWidth。 
#  输入单词数组 words 至少包含一个单词。 
#  
# 
#  示例: 
# 
#  输入:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# 输出:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
#  
# 
#  示例 2: 
# 
#  输入:
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# 输出:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# 解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
#      因为最后一行应为左对齐，而不是左右两端对齐。       
#      第二行同样为左对齐，这是因为这行只包含一个单词。
#  
# 
#  示例 3: 
# 
#  输入:
# words = ["Science","is","what","we","understand","well","enough","to",
# "explain",
#          "to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
# 输出:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]
#  
#  Related Topics 字符串 模拟 👍 196 👎 0
from itertools import accumulate
from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def pick(idx):
            # 寻找words[idx,..,end]能在一行的end下标
            lo, hi = idx, n
            while lo < hi:
                mid = (lo + hi) // 2
                if check(idx, mid): lo = mid + 1
                else: hi = mid
            return lo if lo < n and check(idx, lo) else lo - 1

        def print_line(i, j):
            # 将words[i, ...,j]的单词输出为要求格式
            if i == j or j == n - 1: return " ".join(words[i:j+1]).ljust(maxWidth)
            line, space_num = [], (maxWidth - (chars_presum[j + 1] - chars_presum[i])) // (j - i)
            left = maxWidth - space_num * (j - i) - (chars_presum[j + 1] - chars_presum[i])
            space_chars = " " * space_num if j < n - 1 else " "
            for k in range(i, j):
                line.append(words[k])
                line.append(space_chars + (" " if k - i < left else ""))
            return "".join(line + [words[j]]).ljust(maxWidth)

        chars_presum = list(accumulate(words, lambda s, t: s + len(t), initial=0))
        check = lambda idx, mid: chars_presum[mid + 1] - chars_presum[idx] + mid - idx <= maxWidth
        n, cur, ans = len(words), 0, []
        while cur < n:
            end = pick(cur)
            ans.append(print_line(cur, end))
            cur = end + 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
words = ["What","must","be","acknowledgment","shall","be"]
words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
print("\n".join(Solution().fullJustify(words, maxWidth)))