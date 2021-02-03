# 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。 
# 
#  例如， 
# 
#  [2,3,4] 的中位数是 3 
# 
#  [2,3] 的中位数是 (2 + 3) / 2 = 2.5 
# 
#  设计一个支持以下两种操作的数据结构： 
# 
#  
#  void addNum(int num) - 从数据流中添加一个整数到数据结构中。 
#  double findMedian() - 返回目前所有元素的中位数。 
#  
# 
#  示例： 
# 
#  addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2 
# 
#  进阶: 
# 
#  
#  如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？ 
#  如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？ 
#  
#  Related Topics 堆 设计 
#  👍 343 👎 0
# class MedianFinder:
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.arr = []
#
#
#     def addNum(self, num: int) -> None:
#         index = self._bisect_left(num)
#         self.arr = self.arr[:index] + [num] + self.arr[index:]
#
#     def findMedian(self) -> float:
#         length = len(self.arr)
#         if length % 2:
#             return self.arr[length//2]
#         return (self.arr[length//2-1] + self.arr[length//2]) / 2
#
#     def _bisect_left(self,x):
#         lo, hi = 0, len(self.arr)
#         while lo < hi:
#             mid = (lo + hi) // 2
#             if self.arr[mid] < x: lo = mid + 1
#             else: hi = mid
#         return lo

# leetcode submit region begin(Prohibit modification and deletion)
import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap = [] # 存前半部分数据的最大堆，总数在奇数情况下，最大堆总是多存一个数据
        self.min_heap = [] # 存后半部分数据的最小堆

    def addNum(self, num: int) -> None:
        """
        不管原先总个数是奇数个还是偶数个，都可以这样操作：
        - 先将元素加入最大堆，最大堆元素多一个
        - 然后将弹出最大堆最大值元素，元素个数与之前一样了
        - 将这个元素加入最小堆(原先总数是奇数个的执行就此结束)
        - 如果原先就是偶数个，那么此时最小堆比最大堆会多一个元素
        - 最小堆弹出最小值元素加入到最大堆中
        """
        heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))
        if len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))


    def findMedian(self) -> float:
        length = len(self.min_heap) + len(self.max_heap)
        return -self.max_heap[0] if length % 2 else (self.min_heap[0] - self.max_heap[0]) / 2




# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# leetcode submit region end(Prohibit modification and deletion)
obj = MedianFinder()
obj.addNum(-1)
obj.addNum(-2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())
a = []
