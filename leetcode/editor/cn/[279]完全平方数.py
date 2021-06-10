# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。 
# 
#  给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。 
# 
#  完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 12
# 输出：3 
# 解释：12 = 4 + 4 + 4 
# 
#  示例 2： 
# 
#  
# 输入：n = 13
# 输出：2
# 解释：13 = 4 + 9 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 104 
#  
#  Related Topics 广度优先搜索 数学 动态规划 
#  👍 895 👎 0
import collections
class Solution:
    def numSquares(self, n: int) -> int:
        """
        元素最多有1,2,...,100
        转化为完全背包问题，求解目标是背包装满的最少数量
        f[i][j]表示考虑[1,..,i]个元素凑齐j的最少数量
        f[i][j] = min(f[i-1][j], f[i-1][j-i*i] + 1, f[i-1][j-2*i*i] + 2, f[i-1][j-3*i*i] + 3)
        f[i][j - i * i] =    min(f[i-1][j-i*i],     f[i-1][j-2*i*i] + 1, f[i-1][j-3*i*i] + 2)
        所以可以优化为一维,时间复杂度优化为O(n**1.5)
        f[j] = min(f[j], f[j - i * i] + 1)
        """
        f = [0] + [10 ** 4] * n
        for i in range(1, int(n ** 0.5) + 1):
            for j in range(i * i, n + 1):
                f[j] = min(f[j], f[j - i * i] + 1)
        return f[-1]

class Solution:
    def numSquares(self, n: int) -> int:
        """
        贪心 + 递归。
        is_divided_by(num, count),表示n是否可以由一个完全平方数表示
        1. 先准备一个小于等于n的完全平方数列表
        2.将组合大小(count)从1迭代到n，检查n是否可以由count个完全平方数表示，由is_divided_by表示
        3.base case 只需检查num是否本身是一个完全平方数
        """
        def is_divided_by(num, count):
            if count == 1: return num in square_num
            for k in square_num:
                if is_divided_by(num - k, count - 1):
                    return True
            return False

        square_num = set(i * i for i in range(1, int(n ** 0.5) + 1))
        for count in range(1, n + 1):
            if is_divided_by(n, count):
                return count

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSquares(self, n: int) -> int:
        """
        上述递归的思想其实就是n元树，我们可以用队列BFS去处理
        """
        square_num = set(i * i for i in range(1, int(n ** 0.5) + 1))
        q = collections.deque([n])
        ans = 1
        while True:
            for _ in range(len(q)):
                num = q.popleft()
                if num in square_num:
                    return ans
                for k in square_num:
                    if k > num: continue # 因为是无序set所以不能break
                    q.append(num - k)
            ans += 1
# leetcode submit region end(Prohibit modification and deletion)
n = 43
print(Solution().numSquares(n))