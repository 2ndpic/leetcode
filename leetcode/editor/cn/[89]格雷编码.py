# 格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。 
# 
#  给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。即使有多个不同答案，你也只需要返回其中一种。 
# 
#  格雷编码序列必须以 0 开头。 
# 
#  
# 
#  示例 1: 
# 
#  输入: 2
# 输出: [0,1,3,2]
# 解释:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
# 
# 对于给定的 n，其格雷编码序列并不唯一。
# 例如，[0,2,3,1] 也是一个有效的格雷编码序列。
# 
# 00 - 0
# 10 - 2
# 11 - 3
# 01 - 1 
# 
#  示例 2: 
# 
#  输入: 0
# 输出: [0]
# 解释: 我们定义格雷编码序列必须以 0 开头。
#      给定编码总位数为 n 的格雷编码序列，其长度为 2n。当 n = 0 时，长度为 20 = 1。
#      因此，当 n = 0 时，其格雷编码序列为 [0]。
#  
#  Related Topics 回溯算法 
#  👍 282 👎 0

from typing import List
class Solution:
    def grayCode(self, n: int) -> List[int]:
        """
        迭代
        令n阶gray编码序列为G(n)，即该序列的任一两个连续的数值仅有一个位数的差异
        则肯定有n+1阶gray编码序列的所有元素集合是两倍G(n)大小
        一半为G(n)每个二进制值前面添加0记为S(n)，另一半为G(n)每个二进制值前面添加1记为J(n)
        S(n)序列肯定是gray编码，但是如何排列J(n)才能使得也为gray编码，且S(n)和J(n)交界处也只能有一个bit的差异呢
        那就将G(n)倒序前面添加1记为J(n)
        """
        # ans = [0]
        # for i in range(n):
        #     ans = ans + [j | (1 << i) for j in ans[::-1]]
        # return ans
        ans, head = [0], 1
        for i in range(n):
            for j in range(2 ** i - 1, -1, -1):
                ans.append(ans[j] + head)
            head <<= 1
        return ans
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def grayCode(self, n: int) -> List[int]:
        """
        回溯法
        """
        def backtracking(path):
            if len(path) == 2 ** n: return path
            for i in range(n):
                nxt = 1 << i ^ path[-1]
                if nxt in seen: continue
                seen.add(nxt)
                path.append(nxt)
                if backtracking(path): return path
                path.pop()
                seen.remove(nxt)
        seen = set([0])
        return backtracking([0])
# leetcode submit region end(Prohibit modification and deletion)
print(Solution().grayCode(3))
