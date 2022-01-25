# 给定一个 24 小时制（小时:分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：timePoints = ["23:59","00:00"]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：timePoints = ["00:00","23:59","00:00"]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= timePoints <= 2 * 10⁴ 
#  timePoints[i] 格式为 "HH:MM" 
#  
#  Related Topics 数组 数学 字符串 排序 👍 119 👎 0
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 24 * 60: return 0
        arr = [int(t[:2]) * 60 + int(t[3:])for t in timePoints]
        arr.sort()
        ans = arr[0] + 60 * 24 - arr[-1]
        for i in range(1, len(arr)):
            ans = min(ans, arr[i] - arr[i - 1])
        return ans

# leetcode submit region end(Prohibit modification and deletion)
