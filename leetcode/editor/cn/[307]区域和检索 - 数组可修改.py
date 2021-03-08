# 给你一个数组 nums ，请你完成两类查询，其中一类查询要求更新数组下标对应的值，另一类查询要求返回数组中某个范围内元素的总和。 
# 
#  实现 NumArray 类： 
# 
#  
#  
#  
#  NumArray(int[] nums) 用整数数组 nums 初始化对象 
#  void update(int index, int val) 将 nums[index] 的值更新为 val 
#  int sumRange(int left, int right) 返回子数组 nums[left, right] 的总和（即，nums[left] + 
# nums[left + 1], ..., nums[right]） 
#  
# 
#  
# 
#  示例： 
# 
#  
# 输入：
# ["NumArray", "sumRange", "update", "sumRange"]
# [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
# 输出：
# [null, 9, null, 8]
# 
# 解释：
# NumArray numArray = new NumArray([1, 3, 5]);
# numArray.sumRange(0, 2); // 返回 9 ，sum([1,3,5]) = 9
# numArray.update(1, 2);   // nums = [1,2,5]
# numArray.sumRange(0, 2); // 返回 8 ，sum([1,2,5]) = 8
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 3 * 104 
#  -100 <= nums[i] <= 100 
#  0 <= index < nums.length 
#  -100 <= val <= 100 
#  0 <= left <= right < nums.length 
#  最多调用 3 * 104 次 update 和 sumRange 方法 
#  
#  
#  
#  Related Topics 树状数组 线段树 
#  👍 235 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self._bit = [0] * (self.n + 1)
        for i in range(self.n):
            self._update(i, nums[i])

    def update(self, index: int, val: int) -> None:
        delta = val - self.sumRange(index, index)
        self._update(index, delta)


    def sumRange(self, left: int, right: int) -> int:
        return self._query(right) - self._query(left-1)

    def _update(self, index, delta):
        index += 1
        while index <= self.n:
            self._bit[index] += delta
            index += index & (-index)

    def _query(self, index):
        # [0,..,index]的和
        index += 1
        ans = 0
        while index:
            ans += self._bit[index]
            index -= index & (-index)
        return ans




# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# leetcode submit region end(Prohibit modification and deletion)
