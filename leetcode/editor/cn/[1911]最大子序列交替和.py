# 一个下标从 0 开始的数组的 交替和 定义为 偶数 下标处元素之 和 减去 奇数 下标处元素之 和 。 
# 
#  
#  比方说，数组 [4,2,5,3] 的交替和为 (4 + 5) - (2 + 3) = 4 。 
#  
# 
#  给你一个数组 nums ，请你返回 nums 中任意子序列的 最大交替和 （子序列的下标 重新 从 0 开始编号）。 
# 
#  
#  
# 
#  一个数组的 子序列 是从原数组中删除一些元素后（也可能一个也不删除）剩余元素不改变顺序组成的数组。比方说，[2,7,4] 是 [4,2,3,7,2,1,4
# ] 的一个子序列（加粗元素），但是 [2,4,2] 不是。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [4,2,5,3]
# 输出：7
# 解释：最优子序列为 [4,2,5] ，交替和为 (4 + 5) - 2 = 7 。
#  
# 
#  示例 2： 
# 
#  输入：nums = [5,6,7,8]
# 输出：8
# 解释：最优子序列为 [8] ，交替和为 8 。
#  
# 
#  示例 3： 
# 
#  输入：nums = [6,2,1,2,4,5]
# 输出：10
# 解释：最优子序列为 [6,1,5] ，交替和为 (6 + 5) - 1 = 10 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 105 
#  1 <= nums[i] <= 105 
#  
#  Related Topics 数组 动态规划 
#  👍 15 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        """
        odd[i]表示考虑nums[0,..,i]中选择元素组成子序列，且最后一个选择的元素的下标是奇数时，
              可以得到的最大交替和
        even[i]表示考虑nums[0,..,i]中选择元素组成子序列，且最后一个选择的元素的下标时偶数时，
              可以得到的最大交替和
        在状态转移时，考虑nums[i]是否被选择，对于odd[i]而言:
        - 如果选择nums[i]，那么倒数第二个选择的元素下标在[0,..,i-1]且是一个偶数下标
            odd[i] = even[i-1] - nums[i]
        - 如果不选择nums[i],odd[i] = odd[i-1]
        所以odd[i] = max(odd[i - 1], even[i-1] - nums[i])
        同理可得even的状态转移方程: even[i] = max(even[i - 1], odd[i - 1] + nums[i])
        那么最终答案是max(odd[n - 1], even[n - 1])
        注意到拥有最大交替和的子序列最后一个元素一定不可能位于奇数下标（因为奇数下标对应减）
        因此可以直接返回even[n-1]作为答案
        注意到odd[i]和even[i]都只会从上一状态转移过来，所以可以压缩到一维
        对于只有nums首个元素作为子序列时，有even[0]=nums[0],odd[0]设为0
        """
        even, odd = nums[0], 0
        for i in range(1, len(nums)):
            odd, even = max(odd, even - nums[i]), max(even, odd + nums[i])
        return even
# leetcode submit region end(Prohibit modification and deletion)
