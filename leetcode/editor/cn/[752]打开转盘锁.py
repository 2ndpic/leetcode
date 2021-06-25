# 你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
#  。每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。 
# 
#  锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。 
# 
#  列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。 
# 
#  字符串 target 代表可以解锁的数字，你需要给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 -1 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# 输出：6
# 解释：
# 可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
# 注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
# 因为当拨动到 "0102" 时这个锁就会被锁定。
#  
# 
#  示例 2: 
# 
#  
# 输入: deadends = ["8888"], target = "0009"
# 输出：1
# 解释：
# 把最后一位反向旋转一次即可 "0000" -> "0009"。
#  
# 
#  示例 3: 
# 
#  
# 输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], targ
# et = "8888"
# 输出：-1
# 解释：
# 无法旋转到目标数字且不被锁定。
#  
# 
#  示例 4: 
# 
#  
# 输入: deadends = ["0000"], target = "8888"
# 输出：-1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= deadends.length <= 500 
#  deadends[i].length == 4 
#  target.length == 4 
#  target 不在 deadends 之中 
#  target 和 deadends[i] 仅由若干位数字组成 
#  
#  Related Topics 广度优先搜索 数组 哈希表 字符串 
#  👍 307 👎 0

from typing import List
import collections
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends: return -1
        q = collections.deque(["0000"])
        visited = set(deadends + ["0000"])
        ans = 0
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if cur == target:
                    return ans
                for j in range(len(cur)):
                    new_down = cur[:j] + (chr(ord(cur[j]) - 1) if cur[j] > "0" else "9") + cur[j+1:]
                    new_up = cur[:j] + (chr(ord(cur[j]) + 1) if cur[j] < "9" else "0") + cur[j+1:]
                    if new_down not in visited:
                        q.append(new_down)
                        visited.add(new_down)
                    if new_up not in visited:
                        q.append(new_up)
                        visited.add(new_up)
            ans += 1
        return -1

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def update(q, present, other):
            cur = q.popleft()
            for i in range(4):
                new_down = cur[:i] + (chr(ord(cur[i]) - 1) if cur[i] > "0" else "9") + cur[i+1:]
                new_up = cur[:i] + (chr(ord(cur[i]) + 1) if cur[i] < "9" else "0") + cur[i+1:]
                for ns in (new_up, new_down):
                    if ns in deadends or ns in present: continue
                    if ns in other:
                        return other[ns] + present[cur] + 1
                    else:
                        q.append(ns)
                        present[ns] = present[cur] + 1
            return -1
        def bfs(s, target):
                """
                d1 表示从起点s开始搜索(正向)
                d2 表示从结尾t开始搜索(反向)
                """
                d1, d2 = collections.deque([s]), collections.deque([target])
                m1, m2 = {s:0}, {target:0}
                while d1 and d2:
                    if len(d1) <= len(d2):
                        step = update(d1, m1, m2)
                    else:
                        step = update(d2, m2, m1)
                    if step != -1: return step
                return -1

        s = "0000"
        deadends = set(deadends)
        if s in deadends: return -1
        if s == target: return 0
        ans = bfs(s, target)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
deadends = ["0201","0101","0102","1212","2002"]; target = "0202"
# deadends = ["8888"]; target = "0009"
# deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]; target = "8888"
# deadends = ["0000"]; target = "8888"
print(Solution().openLock(deadends, target))

