# 今天，书店老板有一家店打算试营业 customers.length 分钟。每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分
# 钟结束后离开。 
# 
#  在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。 当书店老板生气时，那一
# 分钟的顾客就会不满意，不生气则他们是满意的。 
# 
#  书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 X 分钟不生气，但却只能使用一次。 
# 
#  请你返回这一天营业下来，最多有多少客户能够感到满意的数量。 
#  
# 
#  示例： 
# 
#  输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
# 输出：16
# 解释：
# 书店老板在最后 3 分钟保持冷静。
# 感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= X <= customers.length == grumpy.length <= 20000 
#  0 <= customers[i] <= 1000 
#  0 <= grumpy[i] <= 1 
#  
#  Related Topics 数组 Sliding Window 
#  👍 117 👎 0

from typing import List
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        # 两个前缀数组，一个是人数，一个是不使用技能时人数。用来加速运算
        no_skill, people, n = [0], [0], len(customers)
        for i in range(n):
            people.append(people[-1] + customers[i])
            no_skill.append(no_skill[-1] + customers[i] * (1 - grumpy[i]))

        ans = 0
        for i in range(n - X + 1):
            ans = max(ans,
                      people[i + X] - people[i] +
                      no_skill[i] - no_skill[0] +
                      no_skill[-1] - no_skill[i + X]
                      )
        return ans
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        wd, n = 0, len(customers)
        for i in range(n):
            t = 1 if i < X else (1 - grumpy[i])
            wd += customers[i] * t
        ans = wd
        for i in range(n - X):
            wd -= customers[i] * grumpy[i]
            wd += customers[i + X] * grumpy[i + X]
            ans = max(ans, wd)
        return ans
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        """
        1. 我们可以先将原本就满意的客户加入答案，同时将对应的 customers[i] 变为 0。
        2. 问题转化为：在 customers 中找到连续一段长度为 x 的子数组，使得其总和最大。这部分就是我们应用技巧所得到的客户。
        """
        ans = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                ans += customers[i]
                customers[i] = 0
        l, max_sum, cur = 0, 0, 0
        for r in range(len(customers)):
            cur += customers[r]
            if r - l + 1 > X:
                cur -= customers[l]
                l += 1
            max_sum = max(max_sum, cur)
        return ans + max_sum
# leetcode submit region end(Prohibit modification and deletion)
customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
X = 6
print(Solution().maxSatisfied(customers=customers, grumpy=grumpy, X=X))