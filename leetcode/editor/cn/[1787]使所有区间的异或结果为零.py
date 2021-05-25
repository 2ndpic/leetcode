# 给你一个整数数组 nums 和一个整数 k 。区间 [left, right]（left <= right）的 异或结果 是对下标位于 left 和 rig
# ht（包括 left 和 right ）之间所有元素进行 XOR 运算的结果：nums[left] XOR nums[left+1] XOR ... XOR n
# ums[right] 。 
# 
#  返回数组中 要更改的最小元素数 ，以使所有长度为 k 的区间异或结果等于零。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,0,3,0], k = 1
# 输出：3
# 解释：将数组 [1,2,0,3,0] 修改为 [0,0,0,0,0]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,4,5,2,1,7,3,4,7], k = 3
# 输出：3
# 解释：将数组 [3,4,5,2,1,7,3,4,7] 修改为 [3,4,7,3,4,7,3,4,7]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1,2,4,1,2,5,1,2,6], k = 3
# 输出：3
# 解释：将数组[1,2,4,1,2,5,1,2,6] 修改为 [1,2,3,1,2,3,1,2,3] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= nums.length <= 2000 
#  0 <= nums[i] < 210 
#  
#  Related Topics 动态规划 
#  👍 52 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n, max_num = len(nums), 1024
        f = [[3000] * max_num for _ in range(k)] # f[i][xor]为前i列且首行异或值为xor的最小修改次数
        g = [3000] * k # g[i]表示考虑前i列的最小修改次数
        for i in range(k):
            num_map, cnt = {}, 0
            # 统计该列信息
            for j in range(i, n, k):
                num_map[nums[j]] = num_map.get(nums[j], 0) + 1
                cnt += 1
            if i == 0:
                for xor in range(max_num):
                    f[0][xor] = min(f[0][xor], cnt - num_map.get(xor, 0))
                    g[0] = min(g[0], f[0][xor])
            else:
                for xor in range(max_num):
                    f[i][xor] = g[i - 1] + cnt # 整列替换
                    for cur in num_map:
                        f[i][xor] = min(f[i][xor], f[i - 1][xor ^ cur] + cnt - num_map[cur]) # 部分替换
                    g[i] = min(g[i], f[i][xor]) # 维护最小修改次数

        return f[k-1][0]
# leetcode submit region end(Prohibit modification and deletion)
nums = [3,4,5,2,1,7,3,4,7];k = 3
print(Solution().minChanges(nums, k))