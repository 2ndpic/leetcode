# 给定一位研究者论文被引用次数的数组（被引用次数是非负整数），数组已经按照 升序排列 。编写一个方法，计算出研究者的 h 指数。 
# 
#  h 指数的定义: “h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）总共有 h 篇论文分别
# 被引用了至少 h 次。（其余的 N - h 篇论文每篇被引用次数不多于 h 次。）" 
# 
#  
# 
#  示例: 
# 
#  输入: citations = [0,1,3,5,6]
# 输出: 3 
# 解释: 给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 0, 1, 3, 5, 6 次。
#      由于研究者有 3 篇论文每篇至少被引用了 3 次，其余两篇论文每篇被引用不多于 3 次，所以她的 h 指数是 3。 
# 
#  
# 
#  说明: 
# 
#  如果 h 有多有种可能的值 ，h 指数是其中最大的那个。 
# 
#  
# 
#  进阶： 
# 
#  
#  这是 H 指数 的延伸题目，本题中的 citations 数组是保证有序的。 
#  你可以优化你的算法到对数时间复杂度吗？ 
#  
#  Related Topics 二分查找 
#  👍 107 👎 0

from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        二分O(logn)
        """
        lo, hi = 0, len(citations) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if citations[mid] < len(citations) - mid:
                lo = mid + 1
            else:
                hi = mid
        return len(citations) - lo
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        遍历O(n)
        """
        n = len(citations)
        for i in range(1, n + 1):
            if citations[-i] < i:
                break
        return i - 1 if citations[-i] < i else i
# leetcode submit region end(Prohibit modification and deletion)
citations = [6,6,6,6,6,6]
print(Solution().hIndex(citations))