# 给你三个整数 n、m 和 k 。下图描述的算法用于找出正整数数组中最大的元素。 
# 
#  
# 
#  请你生成一个具有下述属性的数组 arr ： 
# 
#  
#  arr 中有 n 个整数。 
#  1 <= arr[i] <= m 其中 (0 <= i < n) 。 
#  将上面提到的算法应用于 arr ，search_cost 的值等于 k 。 
#  
# 
#  返回上述条件下生成数组 arr 的 方法数 ，由于答案可能会很大，所以 必须 对 10^9 + 7 取余。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 2, m = 3, k = 1
# 输出：6
# 解释：可能的数组分别为 [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]
#  
# 
#  示例 2： 
# 
#  输入：n = 5, m = 2, k = 3
# 输出：0
# 解释：没有数组可以满足上述条件
#  
# 
#  示例 3： 
# 
#  输入：n = 9, m = 1, k = 1
# 输出：1
# 解释：可能的数组只有 [1, 1, 1, 1, 1, 1, 1, 1, 1]
#  
# 
#  示例 4： 
# 
#  输入：n = 50, m = 100, k = 25
# 输出：34549172
# 解释：不要忘了对 1000000007 取余
#  
# 
#  示例 5： 
# 
#  输入：n = 37, m = 17, k = 7
# 输出：418930126
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 50 
#  1 <= m <= 100 
#  0 <= k <= n 
#  
#  Related Topics 动态规划 👍 69 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        """
        f[i][s][j]表示有i个整数，代价为s，最大值为j的数组的数量。考虑枚举数组中最后一个数，也就是说f[i]会从f[i-1]转移而来
        如果第i个数不改变搜索代价，那么说明他不严格大于数组前的i-1个数，前i-1个数最大值已经为j了
            f[i][s][j] = f[i-1][s][j] * j
        如果第i个数改变了搜索代价，那么只能为j，且前面的数都必须小于j
            f[i][s][j] = f[i-1][s-1][j']  1<=j'<=j-1
        所以f[i][s][j]就是上面两种情况相加
        最终答案就是f[n][k][1...m]
        """
        if k == 0: return 0
        mod = 10 ** 9 + 7
        f = [[[0] * (m + 1) for _ in range(k + 1)] for _ in range(n + 1)]

        # 边界条件，所有长度为1的数组的搜索代价都为1
        for j in range(1, m + 1):
            f[1][1][j] = 1

        for i in range(2, n + 1):
            # 搜索长度不会超过数组长度
            for s in range(1, min(i, k) + 1):
                for j in range(1, m + 1):
                    f[i][s][j] = (f[i - 1][s][j] * j) % mod
                    for j0 in range(1, j):
                        f[i][s][j] = (f[i][s][j] + f[i - 1][s - 1][j0]) % mod
        return sum(f[n][k][j] for j in range(1, m + 1)) % mod
# leetcode submit region end(Prohibit modification and deletion)
