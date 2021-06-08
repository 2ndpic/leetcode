# 有一堆石头，用整数数组 stones 表示。其中 stones[i] 表示第 i 块石头的重量。 
# 
#  每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下： 
# 
#  
#  如果 x == y，那么两块石头都会被完全粉碎； 
#  如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。 
#  
# 
#  最后，最多只会剩下一块 石头。返回此石头 最小的可能重量 。如果没有石头剩下，就返回 0。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：stones = [2,7,4,1,8,1]
# 输出：1
# 解释：
# 组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
# 组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
# 组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
# 组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。
#  
# 
#  示例 2： 
# 
#  
# 输入：stones = [31,26,33,21,40]
# 输出：5
#  
# 
#  示例 3： 
# 
#  
# 输入：stones = [1,2]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= stones.length <= 30 
#  1 <= stones[i] <= 100 
#  
#  Related Topics 动态规划 
#  👍 192 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        石头抽两个出来，较大的为a，较小的为b，则新产生的石头c为a-b
        如果c在下一步的运算中是较大石头，则运行结果还是a - b - d
        如果c在下一步的运算中是较小石头，则运行结果是d - (a - b)
        所以其实在整个【合并】【放回】中，操作的其实就是每个数前面的符号
        那么想要最后结果最小，则就是想要带正号的数绝对值之和与带负号的数的绝对值之和最小
        则问题转化为：希望在stones选择,凑成总和不超过sum/2的最大价值，01背包问题
        f[i][j]为考虑前i个物品，其总和不超过j的最大价值
        f[i][j] = max(f[i-1][j], f[i-1][j-stones[i-1]] + stones[i-1])
        """
        s = sum(stones) // 2
        f = [[0] * (s + 1) for _ in range(2)]
        for i in range(1, len(stones) + 1):
            for j in range(s + 1):
                f[i&1][j] = f[(i-1)&1][j]
                if j >= stones[i - 1]:
                    f[i&1][j] = max(f[i&1][j], f[(i-1)&1][j-stones[i-1]] + stones[i-1])

        return abs(sum(stones) - f[len(stones)&1][s] - f[len(stones)&1][s])


# leetcode submit region end(Prohibit modification and deletion)
stones = [2,7,4,1,8,1]
# stones = [31,26,33,21,40]
# stones = [1,1]
print(Solution().lastStoneWeightII(stones))