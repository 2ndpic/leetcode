# 夏日炎炎，小男孩 Tony 想买一些雪糕消消暑。 
# 
#  商店中新到 n 支雪糕，用长度为 n 的数组 costs 表示雪糕的定价，其中 costs[i] 表示第 i 支雪糕的现金价格。Tony 一共有 coin
# s 现金可以用于消费，他想要买尽可能多的雪糕。 
# 
#  给你价格数组 costs 和现金量 coins ，请你计算并返回 Tony 用 coins 现金能够买到的雪糕的 最大数量 。 
# 
#  注意：Tony 可以按任意顺序购买雪糕。 
# 
#  
# 
#  示例 1： 
# 
#  输入：costs = [1,3,2,4,1], coins = 7
# 输出：4
# 解释：Tony 可以买下标为 0、1、2、4 的雪糕，总价为 1 + 3 + 2 + 1 = 7
#  
# 
#  示例 2： 
# 
#  输入：costs = [10,6,8,7,7,8], coins = 5
# 输出：0
# 解释：Tony 没有足够的钱买任何一支雪糕。
#  
# 
#  示例 3： 
# 
#  输入：costs = [1,6,3,1,2,5], coins = 20
# 输出：6
# 解释：Tony 可以买下所有的雪糕，总价为 1 + 6 + 3 + 1 + 2 + 5 = 18 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  costs.length == n 
#  1 <= n <= 105 
#  1 <= costs[i] <= 105 
#  1 <= coins <= 108 
#  
#  Related Topics 贪心 数组 排序 
#  👍 47 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        """
        01背包问题
        f[i][j]表示考虑前i个最多花费j的最大数量
        f[i][j] = max(f[i-1][j], f[i-1][j-costs[i-1]] + 1)
        虽然可以用一维表示，但是时间复杂度是O(n*coins),超时
        直观的做法是对物品价格从小到大排序，然后贪心从前往后进行决策购买
        证明：
        假定贪心思路取得的序列为[a1, a2, ..,an],真实最优解的序列为[b1,..,bm]
        序列均为单调递增序列。
        其中最优解所对应的具体方案不唯一，只需证明两个序列长度一致即可
        按照贪心的逻辑，最终选择的方案总成本不会超过coins,因此至少是一个合法的选择方案
        天然有 n <= m, 只需证明n >= m，即可得n == m
        通过反证法证明n>=m，假设n>=m不成立，即有n<m
        根据贪心策略，我们的方案在排序好的costs数组里，必然是连续的前缀，并且再选择下一个物品将会超出总费用coins
        而真实最优解的选择方案在排序好的cost数组里分布不定
        这时可以利用【每个物品对答案的贡献为1，将最优解中分布靠后的物品，替换为分布较前的物品，不会使费用增加，同时答案不会减少】
        从而将真实最优解也调整为某段连续的前缀
        这时候根据n<m，会发现存在连续一段长度为m的前缀，费用不超过coins，与我们的贪心决策冲突，
        因此n<m恒不成立，得证n>=m，结合n <= m，可推出n=m
        即贪心解必然能够取得与最优解一样的长度
        """
        costs.sort()
        ans = 0
        for i in costs:
            if coins >= i:
                ans += 1
                coins -= i
            else:
                return ans
        return ans
# leetcode submit region end(Prohibit modification and deletion)
