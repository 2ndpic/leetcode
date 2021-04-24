 # 给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。
# 
#  题目数据保证答案符合 32 位整数范围。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3], target = 4
# 输出：7
# 解释：
# 所有可能的组合为：
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# 请注意，顺序不同的序列被视作不同的组合。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [9], target = 3
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 200 
#  1 <= nums[i] <= 1000 
#  nums 中的所有元素 互不相同 
#  1 <= target <= 1000 
#  
# 
#  
# 
#  进阶：如果给定的数组中含有负数会发生什么？问题会产生何种变化？如果允许负数出现，需要向题目中添加哪些限制条件？ 
#  Related Topics 动态规划 
#  👍 399 👎 0

from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
            定义f[x][y]为组合长度为x，凑成总和为y的方案数,f[0][0] = 1，最终答案为sum(f[i][target] for i in range(1, 最长组合数+1))
            对任意的f[x][target]而言，组合中最后一个数字可以选择nums中任意数值,因此
            f[x][target] = f[x - 1][target - nums[0]] +
                        f[x - 1][target - nums[1]] +...
                        f[x - 1][target - nums[j]]       target >= nums[j]

            时间复杂度O(t^2*n), 超时
        """
        x = target
        f = [[0] * (target + 1) for _ in range(target + 1)]
        f[0][0] = 1
        for i in range(1, x + 1):
            for j in range(target + 1):
                for k in range(len(nums)):
                    f[i][j] += f[i - 1][j - nums[k]] if j >= nums[k] else 0
        return sum(f[i][target] for i in range(1, target + 1))
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        定义f[i]为凑成总和为i的方案数是多少，显然f[0] = 1
        由于每个数值都可以被选择无数次，因此在计算任意总和时，保证nums每一个数字都会被考虑到即可
        f[i] = sum(f[i - j] for j in nums if i >= j)
        """

        f = [0] * (target + 1)
        f[0] = 1
        for i in range(1, target + 1):
            for j in nums:
                f[i] += f[i - j] if i >= j else 0
        return f[target]

# leetcode submit region end(Prohibit modification and deletion)

nums = [1,2,3]
target = 0
print(Solution().combinationSum4(nums, target))