# 给定一位研究者论文被引用次数的数组（被引用次数是非负整数）。编写一个方法，计算出研究者的 h 指数。 
# 
#  h 指数的定义：h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）总共有 h 篇论文分别被引
# 用了至少 h 次。且其余的 N - h 篇论文每篇被引用次数 不超过 h 次。 
# 
#  例如：某人的 h 指数是 20，这表示他已发表的论文中，每篇被引用了至少 20 次的论文总共有 20 篇。 
# 
#  
# 
#  示例： 
# 
#  
# 输入：citations = [3,0,6,1,5]
# 输出：3 
# 解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
#      由于研究者有 3 篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3。 
# 
#  
# 
#  提示：如果 h 有多种可能的值，h 指数是其中最大的那个。 
#  Related Topics 排序 哈希表 
#  👍 144 👎 0

from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        讲citations降序排列，找到一个i，能在直方图中画出最大的正方形
        """
        citations.sort(reverse=True)
        ans = 0
        while ans < len(citations) and citations[ans] >= ans + 1:
            ans += 1
        return ans

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def check(h):
            ans = 0
            for i in citations:
                if i >= h:
                    ans += 1
            return ans >= h
        lo, hi = 0, len(citations)
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid): lo = mid + 1
            else: hi = mid
        return lo if check(lo) else lo - 1
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        papers = [0] * (n + 1) # papers[i]表示被引量为i的paper数
        for i in citations:
            papers[min(i, n)] += 1
        # 找出最大的k，约束于 k <= kp, kp为至少有k次引用的论文数量
        print(papers)
        kp = 0
        for k in range(n, -1, -1):
            kp += papers[k]  # 至少有k次引用的paper数
            if kp >= k:
                break
        return k
# leetcode submit region end(Prohibit modification and deletion)
citations = [1, 3, 2, 3, 100]
# citations = [0]
print(Solution().hIndex(citations))