# 给你一个整数数组 jobs ，其中 jobs[i] 是完成第 i 项工作要花费的时间。 
# 
#  请你将这些工作分配给 k 位工人。所有工作都应该分配给工人，且每项工作只能分配给一位工人。工人的 工作时间 是完成分配给他们的所有工作花费时间的总和。请你
# 设计一套最佳的工作分配方案，使工人的 最大工作时间 得以 最小化 。 
# 
#  返回分配方案中尽可能 最小 的 最大工作时间 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：jobs = [3,2,3], k = 3
# 输出：3
# 解释：给每位工人分配一项工作，最大工作时间是 3 。
#  
# 
#  示例 2： 
# 
#  
# 输入：jobs = [1,2,4,7,8], k = 2
# 输出：11
# 解释：按下述方式分配工作：
# 1 号工人：1、2、8（工作时间 = 1 + 2 + 8 = 11）
# 2 号工人：4、7（工作时间 = 4 + 7 = 11）
# 最大工作时间是 11 。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= jobs.length <= 12 
#  1 <= jobs[i] <= 107 
#  
#  Related Topics 递归 回溯算法 
#  👍 101 👎 0

from typing import List
import functools

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        """
        超时
        """
        def backtracking(start, t, p, cost, cur):
            if cur == total:
                return p >= 1
            if p == 1: return False
            for i in range(start, len(jobs)):
                if not visited[i]:
                    visited[i] = True
                    if jobs[i] + cost > t:
                        tmp = backtracking(0, t, p - 1, jobs[i], cur + jobs[i])
                    else:
                        tmp = backtracking(i + 1, t, p, cost + jobs[i], cur + jobs[i])

                    visited[i]= False
                    if tmp:
                        return True
            return False

        jobs.sort()
        lo, hi, total = max(jobs), sum(jobs), sum(jobs)
        visited = [False] * len(jobs)
        while lo < hi:
            mid = (lo + hi) // 2
            if backtracking(0, mid, k, 0, 0): hi = mid
            else: lo = mid + 1
        return lo

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        def backtracking(job_index, used_worker, worker_time, max_time):
            nonlocal ans
            if max_time >= ans: return
            if job_index == len(jobs):
                ans = max_time
                return
            if used_worker < k:
                worker_time[used_worker] = jobs[job_index]
                backtracking(job_index + 1, used_worker + 1, worker_time, max(max_time, worker_time[used_worker]))
                worker_time[used_worker] = 0
            for i in range(used_worker):
                worker_time[i] += jobs[job_index]
                backtracking(job_index + 1, used_worker, worker_time, max(max_time, worker_time[i]))
                worker_time[i] -= jobs[job_index]

        ans = float('inf')
        backtracking(0, 0, [0] * k, 0)
        return ans

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        def backtracking(limit, groups, path):
            """
            回溯，在此limit限制下是否能完成工作
            """
            if not path: return True
            job = path.pop()
            for i in range(len(groups)):
                if groups[i] + job <= limit:
                    groups[i] += job
                    if backtracking(limit, groups, path): return True
                    groups[i] -= job
                    if groups[i] == 0: break # 这个尚未分配任何工作的工人分配job后DFS失败了，后面同样没有工作的工人就没有必要继续了，因为是同样的结果
            path.append(job)
            return False

        jobs.sort()
        lo, hi = max(jobs), sum(jobs)
        while lo < hi:
            mid = (lo + hi) // 2
            if backtracking(mid, [0] * k, jobs[:]): hi = mid
            else: lo = mid + 1
        return lo

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        """
        思路正确，但是TLE
        """
        def number_of_trailingZeros(i):
            ans = 0
            while i & 1 == 0:
                ans += 1
                i >>= 1
            return ans

        n = len(jobs)
        sum_jobs = [0] * (1 << n)

        for i in range(1, 1 << n):
            x = number_of_trailingZeros(i)
            j = i - (1 << x)
            sum_jobs[i] = sum_jobs[j] + jobs[x]

        """
        f[i][j]表示给[0,..,i]分配工作，工作的分配情况为j时，完成所有工作的最短时间
        f[i][j] = min(max(f[i - 1][Cj'], sum(j')) for j' in j) j'是j的子集，Cj'是j'的补集
        """
        f = [[0] * (1 << n) for _ in range(2)]
        f[0] = sum_jobs[:]

        for i in range(1, k):
            for j in range(1 << n):
                minn = float('inf')
                # 枚举子集
                x = j
                while x:
                    minn = min(minn, max(f[(i - 1) & 1][j - x], sum_jobs[x]))
                    x = (x - 1) & j
                f[i & 1][j] = minn
        return f[(k - 1) & 1][(1 << n) - 1]

# leetcode submit region end(Prohibit modification and deletion)
# jobs = [3,2,3];k = 3
# jobs = [1,3,5,1000];k = 4
jobs = [1,2,4,7,8];k = 2
# jobs = [12,13,14,17,25];k = 3 # 29
# jobs = [2978102,9140986,71464,3828079,8045322,9482671,4668155,5705056,2444210,7052934,1110498];k = 2 # 27276775
# jobs = [5,10,9,15,20,12,18,8,13,15];k = 5
# jobs = [6518448,8819833,7991995,7454298,2087579,380625,4031400,2905811,4901241,8480231,7750692,3544254];k=12

print(Solution().minimumTimeRequired(jobs, k))