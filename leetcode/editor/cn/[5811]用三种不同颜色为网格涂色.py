# 给你两个整数 m 和 n 。构造一个 m x n 的网格，其中每个单元格最开始是白色。请你用 红、绿、蓝 三种颜色为每个单元格涂色。所有单元格都需要被涂色。
#  
# 
#  涂色方案需要满足：不存在相邻两个单元格颜色相同的情况 。返回网格涂色的方法数。因为答案可能非常大， 返回 对 109 + 7 取余 的结果。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：m = 1, n = 1
# 输出：3
# 解释：如上图所示，存在三种可能的涂色方案。
#  
# 
#  示例 2： 
# 
#  
# 输入：m = 1, n = 2
# 输出：6
# 解释：如上图所示，存在六种可能的涂色方案。
#  
# 
#  示例 3： 
# 
#  
# 输入：m = 5, n = 5
# 输出：580986
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= m <= 5 
#  1 <= n <= 1000 
#  
#  👍 7 👎 0

import collections
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        """
        状态压缩动态规划
        将红黄蓝编码为012,那么一行n个格子就是一串三进制字符，将较小长度的数字作为列数，那么转化为10进制取值为[0, 3^m)
        要使得两个相邻格子的颜色均不同，要保证：同一行任意两个相邻格子颜色互不相同，同一列两个格子的颜色互不相同
        那么可以用动态规划：
        - 通过枚举，找出所有对一行进行涂色的方案数
        - 通过动态规划，计算出整个m * n的方格进行涂色的方案数
        用f[i][mask]表示已经对[0,..,i]行进行了涂色，且第i行的涂色方案为mask的总方案数
        那么f[i][mask] = sum(f[i-1][mk]) 其中mk要满足与mask同一数位上的数字均不相同
        先预先处理出同一行任意两个相邻格子颜色互不相同的合法取值
        """
        masks, mod = [], 10 ** 9 + 7
        for num in range(3 ** m):
            n1 = -1
            tmp = num
            for _ in range(m):
                n2 = tmp % 3
                tmp //= 3
                if n1 == n2: break
                n1 = n2
            else:
                masks.append(num)
        f = [[1 if i in masks else 0 for i in range(3 ** m)] for _ in range(2)]
        for i in range(1, n):
            f[i & 1] = [0] * (3 ** m)
            for mask in masks:
                for mk in masks:
                    n1, n2 = mask, mk
                    for _ in range(m):
                        i1, i2 = n1 % 3, n2 % 3
                        n1, n2 = n1 // 3, n2 // 3
                        if i1 == i2: break
                    else:
                        f[i & 1][mask] += f[(i - 1) & 1][mk]
                f[i & 1][mask] %= mod
        return sum(f[(n - 1) & 1])
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        """
        还可以预处理出所有的合法mask对
        """
        masks, mod = [], 10 ** 9 + 7
        for num in range(3 ** m):
            n1 = -1
            tmp = num
            for _ in range(m):
                n2 = tmp % 3
                tmp //= 3
                if n1 == n2: break
                n1 = n2
            else:
                masks.append(num)
        valid = collections.defaultdict(list)
        for i in range(len(masks)):
            for j in range(i + 1, len(masks)):
                n1, n2 = masks[i], masks[j]
                for _ in range(m):
                    i1, i2 = n1 % 3, n2 % 3
                    n1, n2 = n1 // 3, n2 // 3
                    if i1 == i2: break
                else:
                    valid[masks[i]].append(masks[j])
                    valid[masks[j]].append(masks[i])

        f = [[1 if i in masks else 0 for i in range(3 ** m)] for _ in range(2)]
        for i in range(1, n):
            f[i & 1] = [0] * (3 ** m)
            for mask in masks:
                for mk in valid[mask]:
                    f[i & 1][mask] += f[(i - 1) & 1][mk]
                f[i & 1][mask] %= mod
        return sum(f[(n - 1) & 1]) % mod
# leetcode submit region end(Prohibit modification and deletion)
m, n = 5, 5
print(Solution().colorTheGrid(m, n))
