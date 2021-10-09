# 给你一个由非负整数 a1, a2, ..., an 组成的数据流输入，请你将到目前为止看到的数字总结为不相交的区间列表。 
# 
#  实现 SummaryRanges 类： 
# 
#  
#  
#  
#  SummaryRanges() 使用一个空数据流初始化对象。 
#  void addNum(int val) 向数据流中加入整数 val 。 
#  int[][] getIntervals() 以不相交区间 [starti, endi] 的列表形式返回对数据流中整数的总结。 
#  
# 
#  
# 
#  示例： 
# 
#  
# 输入：
# ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", 
# "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
# [[], [1], [], [3], [], [7], [], [2], [], [6], []]
# 输出：
# [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]],
#  null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]
# 
# 解释：
# SummaryRanges summaryRanges = new SummaryRanges();
# summaryRanges.addNum(1);      // arr = [1]
# summaryRanges.getIntervals(); // 返回 [[1, 1]]
# summaryRanges.addNum(3);      // arr = [1, 3]
# summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3]]
# summaryRanges.addNum(7);      // arr = [1, 3, 7]
# summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3], [7, 7]]
# summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
# summaryRanges.getIntervals(); // 返回 [[1, 3], [7, 7]]
# summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
# summaryRanges.getIntervals(); // 返回 [[1, 3], [6, 7]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= val <= 10⁴ 
#  最多调用 addNum 和 getIntervals 方法 3 * 10⁴ 次 
#  
#  
#  
# 
#  
# 
#  进阶：如果存在大量合并，并且与数据流的大小相比，不相交区间的数量很小，该怎么办? 
#  Related Topics 设计 二分查找 有序集合 👍 108 👎 0
from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
from sortedcontainers import SortedDict


class SummaryRanges:

    def __init__(self):
        self.intervals = SortedDict()

    def addNum(self, val: int) -> None:
        intervals_ = self.intervals
        keys_ = self.intervals.keys()
        values_ = self.intervals.values()

        # 找到 l1 最小的且满足 l1 > val 的区间 interval1 = [l1, r1]
        # 如果不存在这样的区间，interval1 为 len(intervals)
        interval1 = intervals_.bisect_right(val)
        # 找到 l0 最大的且满足 l0 <= val 的区间 interval0 = [l0, r0]
        # 在有序集合中，interval0 就是 interval1 的前一个区间
        # 如果不存在这样的区间，interval0 为尾迭代器
        interval0 = (len(intervals_) if interval1 == 0 else interval1 - 1)

        if interval0 != len(intervals_) and keys_[interval0] <= val <= values_[interval0]:
            # 情况一
            return
        else:
            left_aside = (interval0 != len(intervals_) and values_[interval0] + 1 == val)
            right_aside = (interval1 != len(intervals_) and keys_[interval1] - 1 == val)
            if left_aside and right_aside:
                # 情况四
                left, right = keys_[interval0], values_[interval1]
                intervals_.popitem(interval1)
                intervals_.popitem(interval0)
                intervals_[left] = right
            elif left_aside:
                # 情况二
                intervals_[keys_[interval0]] += 1
            elif right_aside:
                # 情况三
                right = values_[interval1]
                intervals_.popitem(interval1)
                intervals_[val] = right
            else:
                # 情况五
                intervals_[val] = val

    def getIntervals(self) -> List[List[int]]:
        # 这里实际上返回的是 List[Tuple[int, int]] 类型
        # 但 Python 的类型提示不是强制的，因此也可以通过
        return list(self.intervals.items())

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
# leetcode submit region end(Prohibit modification and deletion)
