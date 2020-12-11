# 在代号为 C-137 的地球上，Rick 发现如果他将两个球放在他新发明的篮子里，它们之间会形成特殊形式的磁力。Rick 有 n 个空的篮子，第 i 个篮子
# 的位置在 position[i] ，Morty 想把 m 个球放到这些篮子里，使得任意两球间 最小磁力 最大。 
# 
#  已知两个球如果分别位于 x 和 y ，那么它们之间的磁力为 |x - y| 。 
# 
#  给你一个整数数组 position 和一个整数 m ，请你返回最大化的最小磁力。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：position = [1,2,3,4,7], m = 3
# 输出：3
# 解释：将 3 个球分别放入位于 1，4 和 7 的三个篮子，两球间的磁力分别为 [3, 3, 6]。最小磁力为 3 。我们没办法让最小磁力大于 3 。
#  
# 
#  示例 2： 
# 
#  输入：position = [5,4,3,2,1,1000000000], m = 2
# 输出：999999999
# 解释：我们使用位于 1 和 1000000000 的篮子时最小磁力最大。
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == position.length 
#  2 <= n <= 10^5 
#  1 <= position[i] <= 10^9 
#  所有 position 中的整数 互不相同 。 
#  2 <= m <= position.length 
#  
#  Related Topics 数组 二分查找 
#  👍 35 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def valid(self, interval, position, m):
        i, j, m = 0, 1, m - 1
        while j < len(position):
            if position[j] - position[i] >= interval:
                # 可以放置一个小球
                i = j
                j += 1
                m -= 1
            else:
                j += 1
        return m <= 0

    def maxDistance(self, position: List[int], m: int) -> int:
        '''
        首先对position进行排序
        最小可能取值l，只能出现在排序后的挨着的两两一对里面
        最大可能取值r，想象position是连续的空间而不是离散的了，那么最大的可能取值只能是m个球均匀平分这段空间，即放置后的球两两间隔是一样的

        那么我们要找的最大化最小磁力就是在[l, r]这段区间内。如果能将小球全部放完，那么意味着此时的磁力还可以更大一些，需要将左边界右移，否则左移
        '''
        position.sort()
        l, r= float('inf'), 0
        for i in range(len(position)-1):
            l = min(l, position[i+1] - position[i])
        r = (position[-1] - position[0]) // (m-1)
        while l <= r:
            cur = (l + r) // 2
            if self.valid(cur, position, m):
                l = cur + 1
            else:
                r = cur - 1
        return l - 1



# leetcode submit region end(Prohibit modification and deletion)
print(Solution().maxDistance([1,2,3,4,7], 3))