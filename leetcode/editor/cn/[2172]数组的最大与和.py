# 给你一个长度为 n 的整数数组 nums 和一个整数 numSlots ，满足2 * numSlots >= n 。总共有 numSlots 个篮子，编号为
#  1 到 numSlots 。 
# 
#  你需要把所有 n 个整数分到这些篮子中，且每个篮子 至多 有 2 个整数。一种分配方案的 与和 定义为每个数与它所在篮子编号的 按位与运算 结果之和。 
# 
#  
#  比方说，将数字 [1, 3] 放入篮子 1 中，[4, 6] 放入篮子 2 中，这个方案的与和为 (1 AND 1) + (3 AND 1) + (4 
# AND 2) + (6 AND 2) = 1 + 1 + 0 + 2 = 4 。 
#  
# 
#  请你返回将 nums 中所有数放入 numSlots 个篮子中的最大与和。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [1,2,3,4,5,6], numSlots = 3
# 输出：9
# 解释：一个可行的方案是 [1, 4] 放入篮子 1 中，[2, 6] 放入篮子 2 中，[3, 5] 放入篮子 3 中。
# 最大与和为 (1 AND 1) + (4 AND 1) + (2 AND 2) + (6 AND 2) + (3 AND 3) + (5 AND 3) = 
# 1 + 0 + 2 + 2 + 3 + 1 = 9 。
#  
# 
#  示例 2： 
# 
#  输入：nums = [1,3,10,4,7,1], numSlots = 9
# 输出：24
# 解释：一个可行的方案是 [1, 1] 放入篮子 1 中，[3] 放入篮子 3 中，[4] 放入篮子 4 中，[7] 放入篮子 7 中，[10] 放入篮子 9
#  中。
# 最大与和为 (1 AND 1) + (1 AND 1) + (3 AND 3) + (4 AND 4) + (7 AND 7) + (10 AND 9) =
#  1 + 1 + 3 + 4 + 7 + 8 = 24 。
# 注意，篮子 2 ，5 ，6 和 8 是空的，这是允许的。
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == nums.length 
#  1 <= numSlots <= 9 
#  1 <= n <= 2 * numSlots 
#  1 <= nums[i] <= 15 
#  
#  👍 20 👎 0
from typing import List
from functools import lru_cache
class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        """
        f[i][mask]表示考虑nums[0,...,i]整数，且篮子的可用状态为mask时的数组的最大与和。
        考虑将nums[i]放到第k个篮子，那么mask的三进制k-1数位必须大于0
        f[i][mask] = max(f[i - 1][mask - (3 ** j)] + ((j + 1) & nums[i])) 数位j大于0
        """
        @lru_cache(None)
        def f(i, mask):
            if i < 0: return 0
            ans, t, w = 0, mask, 1
            for j in range(1, numSlots + 1):
                if t % 3:
                    ans = max(ans, f(i - 1, mask - w) + (nums[i] & j))
                t, w = t // 3, w * 3
            return ans

        return f(len(nums) - 1, 3 ** numSlots - 1)

class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        """
        注意到实际上i可以由mask推出来，设mask中所表示的状态中共放入了cnt个数，那么i = n - 1 - cnt
        """
        @lru_cache(None)
        def f(mask):
            t, cnt = mask, 0
            for _ in range(numSlots):
                cnt += 2 - (t % 3)
                t //= 3
            if (i := len(nums) - 1 - cnt) < 0: return 0
            ans, t, w = 0, mask, 1
            for j in range(1, numSlots + 1):
                if t % 3:
                    ans = max(ans, f(mask - w) + (j & nums[i]))
                t, w = t // 3, w * 3
            return ans

        return f(3 ** numSlots - 1)


class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        f = [0] * (3 ** numSlots) # f[i]表示篮子状态为i时候的最大与和
        for i, fi in enumerate(f):
            t, cnt = i, 0
            while t:
                cnt += t % 3
                t //= 3
            if cnt >= len(nums): continue
            t, w = i, 1
            for j in range(1, numSlots + 1):
                if t % 3 < 2:
                    f[i + w] = max(f[i + w], fi + (j & nums[cnt]))
                t, w = t // 3, w * 3
        return max(f)
class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        """
        f[mask]表示当篮子的状态为mask，篮子中数的总个数为cnt，并且我们放入的是数组中最开始的cnt个数的情况下的「最大与和」
        """
        mask_max = 3 ** numSlots
        f = [0] * mask_max
        for mask in range(1, mask_max):
            cnt, dummy = 0, mask
            while dummy:
                cnt += dummy % 3
                dummy //= 3
            if cnt > len(nums): continue
            dummy, w = mask, 1
            for i in range(1, numSlots + 1):
                if dummy % 3 > 0:
                    f[mask] = max(f[mask], f[mask - w] + (nums[cnt - 1] & i))
                dummy, w = dummy // 3, w * 3
        return max(f)

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        """
        看作有2 * numSlots个篮子，标号分别为1, 1, 2, 2, ..., numSlots,numSlots
        f[mask]表示将nums的前c个数字(0...c-1)放到篮子中，且放了数字的篮子集合为i时的最大与和, c = bin(mask).count("1")
        f[0] = 0
        考虑将nums[c]放入空蓝子时的状态转移方程，枚举mask中的0,即空蓝子的位置为j，该空蓝子对应的编号为j//2 + 1
        有f[mask | (1 << j)] = max(f[mask | (1 << j)], f[mask] + (j // 2 + 1) & nums[c])
        设nums长度为n，最后答案为max_{c==n}(f)
        若c >= n， 则f[i]无法转移，需要跳过
        """
        f = [0] * (1 << (2 * numSlots))
        for i, fi in enumerate(f):
            c = bin(i).count("1")
            if c >= len(nums): continue
            for j in range(numSlots * 2):
                if (i & (1 << j)) == 0:
                    s = i | (1 << j)
                    f[s] = max(f[s], fi + ((j // 2 + 1) & nums[c]))
        return max(f)

class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        f = [0] * (1 << (2 * numSlots))
        for mask in range(1, len(f)):
            c = bin(mask).count("1")
            if c > len(nums): continue
            for i in range(numSlots * 2):
                if mask & (1 << i):
                    f[mask] = max(f[mask], f[mask ^ (1 << i)] + (nums[c - 1] & (i // 2 + 1)))
        return max(f)


# leetcode submit region end(Prohibit modification and deletion)
nums = [1,3,10,4,7,1]; numSlots = 9
# nums = [1,2,3,4,5,6]; numSlots = 3
nums = [14,7,9,8,2,4,11,1,9]
numSlots = 8
print(Solution().maximumANDSum(nums, numSlots))
