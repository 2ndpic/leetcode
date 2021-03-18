# 给你一个由 不同 整数组成的整数数组 arr 和一个整数 k 。 
# 
#  每回合游戏都在数组的前两个元素（即 arr[0] 和 arr[1] ）之间进行。比较 arr[0] 与 arr[1] 的大小，较大的整数将会取得这一回合的
# 胜利并保留在位置 0 ，较小的整数移至数组的末尾。当一个整数赢得 k 个连续回合时，游戏结束，该整数就是比赛的 赢家 。 
# 
#  返回赢得比赛的整数。 
# 
#  题目数据 保证 游戏存在赢家。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [2,1,3,5,4,6,7], k = 2
# 输出：5
# 解释：一起看一下本场游戏每回合的情况：
# 1   2 3 5 4 6 7 1
# 2   3 5 4 6 7 1 2
# 3   5 4 6 7 1 2 3
# 4   5 6 7 1 2 3 4
# 
# 因此将进行 4 回合比赛，其中 5 是赢家，因为它连胜 2 回合。
#  
# 
#  示例 2： 
# 
#  输入：arr = [3,2,1], k = 10
# 输出：3
# 解释：3 将会在前 10 个回合中连续获胜。
#  
# 
#  示例 3： 
# 
#  输入：arr = [1,9,8,2,3,7,6,4,5], k = 7
# 输出：9
#  
# 
#  示例 4： 
# 
#  输入：arr = [1,11,22,33,44,55,66,77,88,99], k = 1000000000
# 输出：99
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= arr.length <= 10^5 
#  1 <= arr[i] <= 10^6 
#  arr 所含的整数 各不相同 。 
#  1 <= k <= 10^9 
#  
#  Related Topics 数组 
#  👍 27 👎 0

from typing import List
class Node:
    def __init__(self, val, nxt):
        self.val = val
        self.next = nxt
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        max_num = max(arr)
        dummy = Node(0, None)
        end = dummy
        for i in arr:
            end.next = Node(i, None)
            end = end.next
        p1, p2 = dummy.next, dummy.next.next
        tmp = k
        while True:
            while p1.val < p2.val and tmp:
                dummy.next = p2
                end.next = p1
                p1.next = None
                end = end.next
                p1 = dummy.next
                p2 = p1.next
                tmp = k - 1
            if p1.val == max_num:
                return p1.val
            while p1.val > p2.val and tmp:
                p1.next = p2.next
                end.next = p2
                p2.next = None
                end = end.next
                p2 = p1.next
                tmp -= 1
            if tmp == 0:
                return p1.val
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        i, t = 0, 0
        while i < len(arr) - 1 and t < k:
            if arr[i] > arr[i + 1]:
                arr[i + 1] = arr[i]
                t += 1
            else:
                t = 1
            i += 1
        return arr[i]
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        """
        prev 为上一回合游戏中取得胜利的整数，consecutive 表示该整数取得连续胜利的回合数
        进行到第i回合时，一定是在第i-1回合游戏中取得胜利的整数和arr[i]之间进行。i∈[0,1,2,...,len(arr)-1]
        """
        prev = max(arr[0], arr[1])
        if k == 1:
            return prev
        consecutive = 1
        for i in range(2, len(arr)):
            if prev > arr[i]:
                consecutive += 1
                if consecutive == k:
                    return prev
            else:
                prev = arr[i]
                consecutive = 1
        return prev


# leetcode submit region end(Prohibit modification and deletion)
# arr = [1,9,8,2,3,7,6,4,5]
# k = 7
# arr = [3,2,1]
# k = 10
# arr = [2,1,3,5,4,6,7]
# k = 2
# arr = [1,11,22,33,44,55,66,77,88,99]
# k = 1000000000
arr = [1,25,35,42,68,70]
k = 2
print(Solution().getWinner(arr, k))