# 你被安排了 n 个任务。任务需要花费的时间用长度为 n 的整数数组 tasks 表示，第 i 个任务需要花费 tasks[i] 小时完成。一个 工作时间段 
# 中，你可以 至多 连续工作 sessionTime 个小时，然后休息一会儿。 
# 
#  你需要按照如下条件完成给定任务： 
# 
#  
#  如果你在某一个时间段开始一个任务，你需要在 同一个 时间段完成它。 
#  完成一个任务后，你可以 立马 开始一个新的任务。 
#  你可以按 任意顺序 完成任务。 
#  
# 
#  给你 tasks 和 sessionTime ，请你按照上述要求，返回完成所有任务所需要的 最少 数目的 工作时间段 。 
# 
#  测试数据保证 sessionTime 大于等于 tasks[i] 中的 最大值 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：tasks = [1,2,3], sessionTime = 3
# 输出：2
# 解释：你可以在两个工作时间段内完成所有任务。
# - 第一个工作时间段：完成第一和第二个任务，花费 1 + 2 = 3 小时。
# - 第二个工作时间段：完成第三个任务，花费 3 小时。
#  
# 
#  示例 2： 
# 
#  输入：tasks = [3,1,3,1,1], sessionTime = 8
# 输出：2
# 解释：你可以在两个工作时间段内完成所有任务。
# - 第一个工作时间段：完成除了最后一个任务以外的所有任务，花费 3 + 1 + 3 + 1 = 8 小时。
# - 第二个工作时间段，完成最后一个任务，花费 1 小时。
#  
# 
#  示例 3： 
# 
#  输入：tasks = [1,2,3,4,5], sessionTime = 15
# 输出：1
# 解释：你可以在一个工作时间段以内完成所有任务。
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == tasks.length 
#  1 <= n <= 14 
#  1 <= tasks[i] <= 10 
#  max(tasks[i]) <= sessionTime <= 15 
#  
#  👍 30 👎 0
from typing import List
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        """
        f[mask]表示选取状态为mask时，所用最短时间
        枚举mask中为1的位置i,置0后记为mask\i，f[mask]取枚举过程中的最小值
        如果f[mask\i] % sessionTime + tasks[i] <= sessionTime: 那么就可以合在一个时间段完成
        否则，需要新开时间段，这段剩下的时间记得加上去
        """
        n = len(tasks)
        f = [float('inf')] * (1 << n)
        f[0] = 0
        for mask in range(1, 1 << n):
            for i in range(n):
                if mask & (1 << i):
                    t = f[mask ^ (1 << i)]
                    cur = t % sessionTime
                    if cur + tasks[i] <= sessionTime:
                        f[mask] = min(f[mask], t + tasks[i])
                    else:
                        f[mask] = min(f[mask], t - cur + sessionTime + tasks[i])
        return (f[(1 << n) - 1] + sessionTime - 1) // sessionTime

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        """
        枚举子集 + 动态规划
        记f[mask]表示选择状态为mask时，最少需要的工作时间段
        f[mask] = min(f[mask\subject] + 1)
        subject是mask的子集，当且仅当subject中任意1的位置在mask中对应位置也是1。注意合法的subject需满足任务时间总和不超过sessionTime
        所以可以进行预处理，枚举[1, 2**n)范围每一个mask计算其任务时间总和，如果小于等于sessionTime，就valid[mask]标记True
        初始化f[0]=0,最终答案f[2**n-1]
        """
        n = len(tasks)
        valid = [False] * (1 << n)
        for mask in range(1 << n):
            t = 0
            for i in range(n):
                if mask & (1 << i):
                    t += tasks[i]
            if t <= sessionTime:
                valid[mask] = True
        f = [float('inf')] * (1 << n)
        f[0] = 0
        for mask in range(1, 1 << n):
            subject = mask
            while subject:
                if valid[subject]:
                    f[mask] = min(f[mask], f[mask ^ subject] + 1)
                subject = (subject - 1) & mask
        return f[(1 << n) - 1]

# leetcode submit region end(Prohibit modification and deletion)
