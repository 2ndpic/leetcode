# 小扣当前位于魔塔游戏第一层，共有 `N` 个房间，编号为 `0 ~ N-1`。每个房间的补血道具/怪物对于血量影响记于数组 `nums`，其中正数表示道具补
# 血数值，即血量增加对应数值；负数表示怪物造成伤害值，即血量减少对应数值；`0` 表示房间对血量无影响。
# 
# **小扣初始血量为 1，且无上限**。假定小扣原计划按房间编号升序访问所有房间补血/打怪，**为保证血量始终为正值**，小扣需对房间访问顺序进行调整，**每
# 次仅能将一个怪物房间（负数的房间）调整至访问顺序末尾**。请返回小扣最少需要调整几次，才能顺利访问所有房间。若调整顺序也无法访问完全部房间，请返回 -1。
# 
# 
# **示例 1：**
# >输入：`nums = [100,100,100,-250,-60,-140,-50,-50,100,150]`
# >
# >输出：`1`
# >
# >解释：初始血量为 1。至少需要将 nums[3] 调整至访问顺序末尾以满足要求。
# 
# **示例 2：**
# >输入：`nums = [-200,-300,400,0]`
# >
# >输出：`-1`
# >
# >解释：调整访问顺序也无法完成全部房间的访问。
# 
# **提示：**
# - `1 <= nums.length <= 10^5`
# - `-10^5 <= nums[i] <= 10^5` 👍 8 👎 0

from typing import List
import heapq
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def magicTower(self, nums: List[int]) -> int:
        if sum(nums) + 1 <= 0:
            return -1
        hp = 1
        ans = 0
        pq = []
        for i in nums:
            if i < 0:
                heapq.heappush(pq, i)
            while hp + i <= 0:
                hp -= heapq.heappop(pq)
                ans += 1
            hp += i
        return ans
# leetcode submit region end(Prohibit modification and deletion)
# nums = [100,100,100,-250,-60,-140,-50,-50,100,150]
# nums = [-200,-300,400,0]
nums = [-9635,71923,-37495,8366,54303,-86422,-48303,-47858,98424]
print(Solution().magicTower(nums))