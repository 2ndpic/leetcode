# 在 "100 game" 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和达到或超过 100 的玩家，即为胜者。 
# 
#  如果我们将游戏规则改为 “玩家不能重复使用整数” 呢？ 
# 
#  例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。 
# 
#  给定一个整数 maxChoosableInteger （整数池中可选择的最大数）和另一个整数 desiredTotal（累计和），判断先出手的玩家是否能稳
# 赢（假设两位玩家游戏时都表现最佳）？ 
# 
#  你可以假设 maxChoosableInteger 不会大于 20， desiredTotal 不会大于 300。 
# 
#  示例： 
# 
#  输入：
# maxChoosableInteger = 10
# desiredTotal = 11
# 
# 输出：
# false
# 
# 解释：
# 无论第一个玩家选择哪个整数，他都会失败。
# 第一个玩家可以选择从 1 到 10 的整数。
# 如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
# 第二个玩家可以通过选择整数 10（那么累积和为 11 >= desiredTotal），从而取得胜利.
# 同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。
#  
#  Related Topics 位运算 记忆化搜索 数学 动态规划 状态压缩 博弈 
#  👍 241 👎 0
import functools

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canIWin(self, n: int, desiredTotal: int) -> bool:
        @functools.lru_cache(None)
        def dfs(mask, cursum):
            for i in range(1, n + 1):
                if mask & (1 << (i - 1)) == 0:
                    if cursum + i >= desiredTotal or (not dfs(mask | (1 << (i - 1)), cursum + i)):
                        return True
            return False

        if n >= desiredTotal: return True
        if (1 + n) * n // 2 < desiredTotal: return False
        dfs.cache_clear()
        return dfs(0, 0)

# leetcode submit region end(Prohibit modification and deletion)
print(Solution().canIWin(10, 11))