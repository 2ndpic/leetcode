# Alice 和 Bob 玩一个游戏，两人轮流行动，Alice 先手 。 
# 
#  给你一个 偶数长度 的字符串 num ，每一个字符为数字字符或者 '?' 。每一次操作中，如果 num 中至少有一个 '?' ，那么玩家可以执行以下操作：
#  
# 
#  
#  选择一个下标 i 满足 num[i] == '?' 。 
#  将 num[i] 用 '0' 到 '9' 之间的一个数字字符替代。 
#  
# 
#  当 num 中没有 '?' 时，游戏结束。 
# 
#  Bob 获胜的条件是 num 中前一半数字的和 等于 后一半数字的和。Alice 获胜的条件是前一半的和与后一半的和 不相等 。 
# 
#  
#  比方说，游戏结束时 num = "243801" ，那么 Bob 获胜，因为 2+4+3 = 8+0+1 。如果游戏结束时 num = "243803" 
# ，那么 Alice 获胜，因为 2+4+3 != 8+0+3 。 
#  
# 
#  在 Alice 和 Bob 都采取 最优 策略的前提下，如果 Alice 获胜，请返回 true ，如果 Bob 获胜，请返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：num = "5023"
# 输出：false
# 解释：num 中没有 '?' ，没法进行任何操作。
# 前一半的和等于后一半的和：5 + 0 = 2 + 3 。
#  
# 
#  示例 2： 
# 
#  
# 输入：num = "25??"
# 输出：true
# 解释：Alice 可以将两个 '?' 中的一个替换为 '9' ，Bob 无论如何都无法使前一半的和等于后一半的和。
#  
# 
#  示例 3： 
# 
#  
# 输入：num = "?3295???"
# 输出：false
# 解释：Bob 总是能赢。一种可能的结果是：
# - Alice 将第一个 '?' 用 '9' 替换。num = "93295???" 。
# - Bob 将后面一半中的一个 '?' 替换为 '9' 。num = "932959??" 。
# - Alice 将后面一半中的一个 '?' 替换为 '2' 。num = "9329592?" 。
# - Bob 将后面一半中最后一个 '?' 替换为 '7' 。num = "93295927" 。
# Bob 获胜，因为 9 + 3 + 2 + 9 = 5 + 9 + 2 + 7 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= num.length <= 105 
#  num.length 是 偶数 。 
#  num 只包含数字字符和 '?' 。 
#  
#  Related Topics 贪心 
#  👍 2 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sumGame(self, num: str) -> bool:
        """
        问号个数为奇数，先手的alice必胜。因为最多只有一种变换能使左右两边相等，alice只需不采用即胜利。
        接下来只用讨论问号个数为偶数的情况
        如果问号个数为0那么bob胜利，当前仅当左半数字等于右半数字
        如果问号个数为2且不同侧，那么Bob获胜当且仅当左半数字等于右半数字。因为如果不等，alice只需将大数那边的问号换成9，bob无法平衡
        如果问号个数为2且同侧，Bob获胜当且仅当另一侧数字和 - 此侧数字和 == 9。如果超过9，alice将一个问好换成0，小于9alice换成9
        假设左半数字和为n0，问号个数为q0, 右半数字和为n1,问号个数为q1,且(q1 + q2) % 2 == 0
        那么Bob获胜的关键是: n0 - n1 = 9 * (q1 - q0) / 2,假设q0 < q1
        解释：
        - 对于q0个分别在两侧的问号，alice和bob的最优策略会使得它们的数字和完全相等，那么左侧没有问号了，右侧还有q1 - q0个问号
        - 此时Alice和Bob可操作(q1 - q0)/2对个问号，每对的和为9
        """
        n, n0, n1, q0, q1 = len(num), 0, 0, 0, 0
        for i in range(n // 2):
            if num[i] == "?": q0 += 1
            else: n1 += int(num[i])
            if num[n // 2 + i] == "?": q1 += 1
            else: n1 += int(num[n // 2 + i])
        if (q0 + q1) % 2: return True
        if q0 > q1: n0, q0, n1, q1 = n1, q1, n0, q0
        return n0 - n1 != 9 * (q1 - q0) // 2


# leetcode submit region end(Prohibit modification and deletion)
