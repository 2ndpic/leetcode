# n 张多米诺骨牌排成一行，将每张多米诺骨牌垂直竖立。在开始时，同时把一些多米诺骨牌向左或向右推。 
# 
#  每过一秒，倒向左边的多米诺骨牌会推动其左侧相邻的多米诺骨牌。同样地，倒向右边的多米诺骨牌也会推动竖立在其右侧的相邻多米诺骨牌。 
# 
#  如果一张垂直竖立的多米诺骨牌的两侧同时有多米诺骨牌倒下时，由于受力平衡， 该骨牌仍然保持不变。 
# 
#  就这个问题而言，我们会认为一张正在倒下的多米诺骨牌不会对其它正在倒下或已经倒下的多米诺骨牌施加额外的力。 
# 
#  给你一个字符串 dominoes 表示这一行多米诺骨牌的初始状态，其中： 
# 
#  
#  dominoes[i] = 'L'，表示第 i 张多米诺骨牌被推向左侧， 
#  dominoes[i] = 'R'，表示第 i 张多米诺骨牌被推向右侧， 
#  dominoes[i] = '.'，表示没有推动第 i 张多米诺骨牌。 
#  
# 
#  返回表示最终状态的字符串。 
#  
# 
#  示例 1： 
# 
#  
# 输入：dominoes = "RR.L"
# 输出："RR.L"
# 解释：第一张多米诺骨牌没有给第二张施加额外的力。
#  
# 
#  示例 2： 
# 
#  
# 输入：dominoes = ".L.R...LR..L.."
# 输出："LL.RR.LLRRLL.."
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == dominoes.length 
#  1 <= n <= 10⁵ 
#  dominoes[i] 为 'L'、'R' 或 '.' 
#  
#  Related Topics 双指针 字符串 动态规划 👍 237 👎 0
from collections import deque

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        s = list(dominoes)
        n, i, left = len(s), 0, "L"
        while i < n:
            j = i
            while j < n and s[j] == ".":
                j += 1
            right = s[j] if j < n else "R"
            if left == right:
                while i < j:
                    s[i] = right
                    i += 1
            elif left == "R" and right == "L":
                k = j - 1
                while i < k:
                    s[i], s[k] = "R", "L"
                    i += 1
                    k -= 1
            left = right
            i = j + 1
        return "".join(s)


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        q = deque()
        time = [-1] * n
        force = [[] for _ in range(n)]
        for i, f in enumerate(dominoes):
            if f != ".":
                q.append(i)
                time[i] = 0
                force[i].append(f)
        res = ["."] * n
        while q:
            i = q.popleft()
            if len(force[i]) == 1:
                res[i] = f = force[i][0]
                ni = i - 1 if f == "L" else i + 1
                if 0 <= ni < n:
                    if time[ni] == -1:
                        q.append(ni)
                        time[ni] = time[i] + 1
                        force[ni].append(f)
                    elif time[ni] == time[i] + 1:
                        force[ni].append(f)
        return "".join(res)
# leetcode submit region end(Prohibit modification and deletion)
dominoes = ".L.R...LR..L.."
print(Solution().pushDominoes(dominoes))