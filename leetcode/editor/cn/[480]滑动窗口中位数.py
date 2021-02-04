# 中位数是有序序列最中间的那个数。如果序列的大小是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。 
# 
#  例如： 
# 
#  
#  [2,3,4]，中位数是 3 
#  [2,3]，中位数是 (2 + 3) / 2 = 2.5 
#  
# 
#  给你一个数组 nums，有一个大小为 k 的窗口从最左端滑动到最右端。窗口中有 k 个数，每次窗口向右移动 1 位。你的任务是找出每次窗口移动后得到的新窗
# 口中元素的中位数，并输出由它们组成的数组。 
# 
#  
# 
#  示例： 
# 
#  给出 nums = [1,3,-1,-3,5,3,6,7]，以及 k = 3。 
# 
#  窗口位置                      中位数
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       1
#  1 [3  -1  -3] 5  3  6  7      -1
#  1  3 [-1  -3  5] 3  6  7      -1
#  1  3  -1 [-3  5  3] 6  7       3
#  1  3  -1  -3 [5  3  6] 7       5
#  1  3  -1  -3  5 [3  6  7]      6
#  
# 
#  因此，返回该滑动窗口的中位数数组 [1,-1,-1,3,5,6]。 
# 
#  
# 
#  提示： 
# 
#  
#  你可以假设 k 始终有效，即：k 始终小于输入的非空数组的元素个数。 
#  与真实值误差在 10 ^ -5 以内的答案将被视作正确答案。 
#  
#  Related Topics Sliding Window 
#  👍 163 👎 0

from typing import List
import bisect
import heapq
import collections

def s1(nums: List[int], k: int) -> List[float]:
    get_mid = lambda x: (x[len(x) // 2] + x[(len(x) - 1) // 2]) / 2
    i, j = 0, k
    window = sorted(nums[:k])  # O(klog(k))
    res = [get_mid(window)]
    while j < len(nums):
        window.pop(bisect.bisect_left(window, nums[i]))  # O(k)
        window.insert(bisect.bisect_left(window, nums[j]), nums[j])  # O(k)
        res.append(get_mid(window))
        i += 1
        j += 1
    return res

class DualHeap:
    def __init__(self, k: int):
        # 大根堆，维护较小的一半元素，注意 python 没有大根堆，需要将所有元素取相反数并使用小根堆
        self.small = list()
        # 小根堆，维护较大的一半元素
        self.large = list()
        # 哈希表，记录「延迟删除」的元素，key 为元素，value 为需要删除的次数
        self.delayed = collections.Counter()

        self.k = k
        # small 和 large 当前包含的元素个数，需要扣除被「延迟删除」的元素
        self.smallSize = 0
        self.largeSize = 0

    # 不断地弹出 heap 的堆顶元素，并且更新哈希表
    def prune(self, heap: List[int]):
        while heap:
            num = heap[0]
            if heap is self.small:
                num = -num
            if num in self.delayed:
                self.delayed[num] -= 1
                if self.delayed[num] == 0:
                    self.delayed.pop(num)
                heapq.heappop(heap)
            else:
                break

    # 调整 small 和 large 中的元素个数，使得二者的元素个数满足要求
    def makeBalance(self):
        if self.smallSize > self.largeSize + 1:
            # small 比 large 元素多 2 个
            heapq.heappush(self.large, -self.small[0])
            heapq.heappop(self.small)
            self.smallSize -= 1
            self.largeSize += 1
            # small 堆顶元素被移除，需要进行 prune
            self.prune(self.small)
        elif self.smallSize < self.largeSize:
            # large 比 small 元素多 1 个
            heapq.heappush(self.small, -self.large[0])
            heapq.heappop(self.large)
            self.smallSize += 1
            self.largeSize -= 1
            # large 堆顶元素被移除，需要进行 prune
            self.prune(self.large)

    def insert(self, num: int):
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.smallSize += 1
        else:
            heapq.heappush(self.large, num)
            self.largeSize += 1
        self.makeBalance()

    def erase(self, num: int):
        self.delayed[num] += 1
        if num <= -self.small[0]:
            self.smallSize -= 1
            if num == -self.small[0]:
                self.prune(self.small)
        else:
            self.largeSize -= 1
            if num == self.large[0]:
                self.prune(self.large)
        self.makeBalance()

    def getMedian(self) -> float:
        return float(-self.small[0]) if self.k % 2 == 1 else (-self.small[0] + self.large[0]) / 2


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        dh = DualHeap(k)
        for num in nums[:k]:
            dh.insert(num)

        ans = [dh.getMedian()]
        for i in range(k, len(nums)):
            dh.insert(nums[i])
            dh.erase(nums[i - k])
            ans.append(dh.getMedian())

        return ans
# leetcode submit region begin(Prohibit modification and deletion)
class Heap:
    def __init__(self, name="min"):
        self.arr = []
        self.f = lambda x: x if name=="min" else -x
    def push(self, num):
        heapq.heappush(self.arr, self.f(num))                   # 推入一个
    def pop(self):
        return self.f(heapq.heappop(self.arr))                  # 弹出堆顶
    def top(self):
        return self.f(self.arr[0])
    def empty(self):
        return len(self.arr) == 0

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small = Heap(name="max") # 较小数字部分使用大根堆
        big = Heap(name="min")   # 较大数字部分使用小根堆
        get_mid = lambda x, y: x.top() if k % 2 else (x.top() + y.top()) / 2
        mp = collections.defaultdict(int)
        for i in range(k):
            small.push(nums[i])
        for i in range(k//2):
            big.push(small.pop())
        ans = [get_mid(small, big)]
        for i in range(k, len(nums)):
            balance = 0
            l, r = nums[i-k], nums[i]  # 将被删除的窗口最左元素和将被添加到窗口最右的元素
            mp[l] += 1                 # 左窗口元素记账
            if l <= small.top():
                balance -= 1           # 较小数字堆需删除一个元素
            else:
                balance += 1           # 较大数字堆需删除一个元素
            if r <= small.top():
                balance += 1           # 较小数字堆添加一个元素
                small.push(r)
            else:
                balance -= 1           # 较大数字堆添加一个元素
                big.push(r)
            """
            此时balance取值可能是:
            balance | small | big  | 解释
              0     | -1+1  |      | 较小数字堆删除一个元素添加一个元素，两边还是平衡的
              0     |       | +1-1 | 较大数字堆删除一个元素添加一个元素，两边还是平衡的
             -2     | -1    | -1   | 较小数字堆删除一个元素，较大数字堆添加一个元素，失衡
              2     | +1    | +1   | 较大数字堆删除一个元素，较小数字堆添加一个元素，失衡
            """
            # 较小数字堆挪一个给较大数字堆(3,3)->(4,2)->(3,3)或者(4,3)->(5,2)->(4,3)
            if balance == 2:
                big.push(small.pop())
            # 较大数字堆挪一个给较小数字堆(3,3)->(2,4)->(3,3)或者(4,3)->(3,4)->(4,3)
            elif balance == -2:
                small.push(big.pop())
            # 重新达到平衡了,该看看堆顶是不是待删除元素了
            while not small.empty() and mp[small.top()]:
                mp[small.top()] -= 1
                small.pop()
            while not big.empty() and mp[big.top()]:
                mp[big.top()] -= 1
                big.pop()
            # 为什么删除堆顶元素后不用重新平衡两边堆了呢？
            ans.append(get_mid(small, big))
        return ans

# leetcode submit region end(Prohibit modification and deletion)
nums = [1,2, 3]
k = 3
print(Solution().medianSlidingWindow(nums, k))
