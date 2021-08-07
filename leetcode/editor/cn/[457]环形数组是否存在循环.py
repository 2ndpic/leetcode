# 存在一个不含 0 的 环形 数组 nums ，每个 nums[i] 都表示位于下标 i 的角色应该向前或向后移动的下标个数： 
# 
#  
#  如果 nums[i] 是正数，向前 移动 nums[i] 步 
#  如果 nums[i] 是负数，向后 移动 nums[i] 步 
#  
# 
#  因为数组是 环形 的，所以可以假设从最后一个元素向前移动一步会到达第一个元素，而第一个元素向后移动一步会到达最后一个元素。 
# 
#  数组中的 循环 由长度为 k 的下标序列 seq ： 
# 
#  
#  遵循上述移动规则将导致重复下标序列 seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ... 
#  所有 nums[seq[j]] 应当不是 全正 就是 全负 
#  k > 1 
#  
# 
#  如果 nums 中存在循环，返回 true ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,-1,1,2,2]
# 输出：true
# 解释：存在循环，按下标 0 -> 2 -> 3 -> 0 。循环长度为 3 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [-1,2]
# 输出：false
# 解释：按下标 1 -> 1 -> 1 ... 的运动无法构成循环，因为循环的长度为 1 。根据定义，循环的长度必须大于 1 。
#  
# 
#  示例 3: 
# 
#  
# 输入：nums = [-2,1,-1,-2,-2]
# 输出：false
# 解释：按下标 1 -> 2 -> 1 -> ... 的运动无法构成循环，因为 nums[1] 是正数，而 nums[2] 是负数。
# 所有 nums[seq[j]] 应当不是全正就是全负。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 5000 
#  -1000 <= nums[i] <= 1000 
#  nums[i] != 0 
#  
# 
#  
# 
#  进阶：你能设计一个时间复杂度为 O(n) 且额外空间复杂度为 O(1) 的算法吗？ 
#  Related Topics 数组 哈希表 双指针 
#  👍 131 👎 0
from typing import List
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            if nums[i] % n == 0: continue
            cnt = 0
            nxt = i
            while nums[nxt] * nums[i] > 0 and cnt < n:
                if nums[nxt] > 0: nxt = (nxt + nums[nxt]) % n
                else: nxt = (nxt - abs(nums[nxt]) % n + n) % n
                if nxt == i: return True
                cnt += 1
        return False
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        vis = [-1] * n  # 使用vis对每个小标进行标记，若i位置在idx轮被标记，vis[i]=idx
        for i in range(n):
            if vis[i] != -1: continue
            cur = i
            while True:
                nxt = ((cur + nums[cur]) % n + n) % n
                if nxt == cur: break
                if vis[nxt] != -1:
                    # nxt已被标记且非本轮标记，那么往后的通路必然都被标记且无环，跳出
                    if vis[nxt] != i: break
                    # 如果nxt点已被标记，并且是本轮被标记，说明找到了环
                    else: return True
                if nums[i] * nums[nxt] < 0: break
                vis[nxt] = i
                cur = nxt
        return False

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        vis = [-1] * n  # 使用vis对每个小标进行标记，若i位置在idx轮被标记，vis[i]=idx
        for i in range(n):
            if vis[i] != -1: continue
            cur = i
            while True:
                nxt = ((cur + nums[cur]) % n + n) % n
                if nxt == cur: break
                if vis[nxt] != -1:
                    # nxt已被标记且非本轮标记，那么往后的通路必然都被标记且无环，跳出
                    if vis[nxt] != i: break
                    # 如果nxt点已被标记，并且是本轮被标记，说明找到了环
                    else: return True
                if nums[i] * nums[nxt] < 0: break
                vis[nxt] = i
                cur = nxt
        return False
# leetcode submit region end(Prohibit modification and deletion)
# nums = [-2,1,-1,-2,-2]
# nums = [-1,2]
# nums = [2,-1,1,2,2]
nums = [-1,2,1,2]
print(Solution().circularArrayLoop(nums))