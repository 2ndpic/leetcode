# 二进制手表顶部有 4 个 LED 代表 小时（0-11），底部的 6 个 LED 代表 分钟（0-59）。每个 LED 代表一个 0 或 1，最低位在右侧。
#  
# 
#  
#  例如，下面的二进制手表读取 "3:25" 。 
#  
# 
#  
# 
#  （图源：WikiMedia - Binary clock samui moon.jpg ，许可协议：Attribution-ShareAlike 3.0 
# Unported (CC BY-SA 3.0) ） 
# 
#  给你一个整数 turnedOn ，表示当前亮着的 LED 的数量，返回二进制手表可以表示的所有可能时间。你可以 按任意顺序 返回答案。 
# 
#  小时不会以零开头： 
# 
#  
#  例如，"01:00" 是无效的时间，正确的写法应该是 "1:00" 。 
#  
# 
#  分钟必须由两位数组成，可能会以零开头： 
# 
#  
#  例如，"10:2" 是无效的时间，正确的写法应该是 "10:02" 。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：turnedOn = 1
# 输出：["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
#  
# 
#  示例 2： 
# 
#  
# 输入：turnedOn = 9
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= turnedOn <= 10 
#  
#  Related Topics 位运算 回溯算法 
#  👍 276 👎 0

import collections
from typing import List
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        def helper(hstart, mstart, l1, l2):
            if len(l1)+len(l2) == num:
                hour = sum(l1)
                minute = sum(l2)
                res.add('%d:%02d' % (hour, minute))
                return

            for i in range(hstart, 4):
                '''搜索时针'''
                if sum(l1) + nums[i] > 11:
                    break
                l1.append(nums[i])
                helper(i+1, mstart, l1, l2)
                l1.pop()

            for i in range(mstart, 6):
                '''搜索分针'''
                if sum(l2) + nums[i] > 59:
                    break
                l2.append(nums[i])
                helper(hstart, i+1,  l1, l2)
                l2.pop()

        nums = [1, 2, 4, 8, 16, 32]
        res = set()
        helper(0, 0, [], [])
        return list(res)

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        memo = collections.defaultdict(list)
        for i in range(12):
            for j in range(60):
                lights = bin(i).count("1") + bin(j).count("1")
                memo[lights].append("{}:{:0>2d}".format(i, j))
        print(memo[turnedOn])

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        """
        用2^10表示所有亮灯的组合，其中高四位表示小时，低六位表示分钟
        """
        ans = []
        for i in range(1024):
            h, m = i >> 6, i & 63
            if h < 12 and m < 60 and bin(i).count("1") == turnedOn:
                ans.append(f"{h}:{m:02d}")
        return ans
# leetcode submit region end(Prohibit modification and deletion)
