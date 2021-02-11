# 设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。 
# 
#  请实现 KthLargest 类： 
# 
#  
#  KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。 
#  int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。 
#  
# 
#  
# 
#  示例： 
# 
#  
# 输入：
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# 输出：
# [null, 4, 5, 5, 8, 8]
# 
# 解释：
# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3);   // return 4
# kthLargest.add(5);   // return 5
# kthLargest.add(10);  // return 5
# kthLargest.add(9);   // return 8
# kthLargest.add(4);   // return 8
#  
# 
#  
# 提示：
# 
#  
#  1 <= k <= 104 
#  0 <= nums.length <= 104 
#  -104 <= nums[i] <= 104 
#  -104 <= val <= 104 
#  最多调用 add 方法 104 次 
#  题目数据保证，在查找第 k 大元素时，数组中至少有 k 个元素 
#  
#  Related Topics 堆 设计 
#  👍 223 👎 0

from typing import List
import heapq
# leetcode submit region begin(Prohibit modification and deletion)
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # 第k大元素，就是size=k的数组的最小那个元素，这里使用最小堆
        self.heap = []
        self.k = k
        for i in range(len(nums)):
            if i >= k:
                if nums[i] > self.heap[0]:
                    heapq.heappop(self.heap)
                else:
                    continue
            heapq.heappush(self.heap, nums[i])

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]





# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# leetcode submit region end(Prohibit modification and deletion)
k = 3
nums = [4, 5, 8, 2]
obj = KthLargest(k, nums)
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))