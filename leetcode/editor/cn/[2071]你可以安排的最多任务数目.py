# 给你 n 个任务和 m 个工人。每个任务需要一定的力量值才能完成，需要的力量值保存在下标从 0 开始的整数数组 tasks 中，第 i 个任务需要 
# tasks[i] 的力量才能完成。每个工人的力量值保存在下标从 0 开始的整数数组 workers 中，第 j 个工人的力量值为 workers[j] 。每个工人只能完
# 成 一个 任务，且力量值需要 大于等于 该任务的力量要求值（即 workers[j] >= tasks[i] ）。 
# 
#  除此以外，你还有 pills 个神奇药丸，可以给 一个工人的力量值 增加 strength 。你可以决定给哪些工人使用药丸，但每个工人 最多 只能使用 一
# 片 药丸。 
# 
#  给你下标从 0 开始的整数数组tasks 和 workers 以及两个整数 pills 和 strength ，请你返回 最多 有多少个任务可以被完成。 
# 
# 
#  
# 
#  示例 1： 
# 
#  输入：tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1
# 输出：3
# 解释：
# 我们可以按照如下方案安排药丸：
# - 给 0 号工人药丸。
# - 0 号工人完成任务 2（0 + 1 >= 1）
# - 1 号工人完成任务 1（3 >= 2）
# - 2 号工人完成任务 0（3 >= 3）
#  
# 
#  示例 2： 
# 
#  输入：tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5
# 输出：1
# 解释：
# 我们可以按照如下方案安排药丸：
# - 给 0 号工人药丸。
# - 0 号工人完成任务 0（0 + 5 >= 5）
#  
# 
#  示例 3： 
# 
#  输入：tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10
# 输出：2
# 解释：
# 我们可以按照如下方案安排药丸：
# - 给 0 号和 1 号工人药丸。
# - 0 号工人完成任务 0（0 + 10 >= 10）
# - 1 号工人完成任务 1（10 + 10 >= 15）
#  
# 
#  示例 4： 
# 
#  输入：tasks = [5,9,8,5,9], workers = [1,6,4,2,6], pills = 1, strength = 5
# 输出：3
# 解释：
# 我们可以按照如下方案安排药丸：
# - 给 2 号工人药丸。
# - 1 号工人完成任务 0（6 >= 5）
# - 2 号工人完成任务 2（4 + 5 >= 8）
# - 4 号工人完成任务 3（6 >= 5）
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == tasks.length 
#  m == workers.length 
#  1 <= n, m <= 5 * 10⁴ 
#  0 <= pills <= m 
#  0 <= tasks[i], workers[j], strength <= 10⁹ 
#  
#  Related Topics 贪心 队列 数组 二分查找 排序 单调队列 👍 21 👎 0

from typing import List

from sortedcontainers import SortedList
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        def check(k):
            w = SortedList(workers[-k:])
            cnt = pills
            for i in range(k - 1, -1, -1):
                if w[-1] >= tasks[i]: w.pop()
                elif cnt and (idx := w.bisect_left(tasks[i] - strength)) != len(w):
                    w.pop(idx)
                    cnt -= 1
                else: return False
            return True
        tasks.sort()
        workers.sort()
        n, m = len(tasks), len(workers)
        lo, hi = 0, min(n, m)
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid): lo = mid + 1
            else: hi = mid
        return lo if check(lo) else lo - 1
# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        def check(k):
            cnt = pills
            w = deque()
            j = m - 1
            for i in range(k - 1, -1, -1):
                while j >= m - k and workers[j] + strength >= tasks[i]:
                    w.appendleft(workers[j])
                    j -= 1
                if w and w[-1] >= tasks[i]: w.pop()
                elif cnt and w:
                    w.popleft()
                    cnt -= 1
                else: return False
            return True
        tasks.sort()
        workers.sort()
        n, m = len(tasks), len(workers)
        lo, hi = 0, min(n, m)
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid): lo = mid + 1
            else: hi = mid
        return lo if check(lo) else lo - 1

# leetcode submit region end(Prohibit modification and deletion)
tasks = [5,9,8,5,9]
workers = [1,6,4,2,6]
pills = 1
strength = 5
print("结果", Solution().maxTaskAssign(tasks, workers, pills, strength))