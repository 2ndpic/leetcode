# 累加数是一个字符串，组成它的数字可以形成累加序列。 
# 
#  一个有效的累加序列必须至少包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。 
# 
#  给定一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是累加数。 
# 
#  说明: 累加序列里的数不会以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。 
# 
#  示例 1: 
# 
#  输入: "112358"
# 输出: true 
# 解释: 累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
#  
# 
#  示例 2: 
# 
#  输入: "199100199"
# 输出: true 
# 解释: 累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199 
# 
#  进阶: 
# 你如何处理一个溢出的过大的整数输入? 
#  Related Topics 回溯算法 
#  👍 153 👎 0
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def backtracking(start, a1, a2, a3):
            if a1 > -1 and a2 > -1 and a3 > -1 and a3 != a1 + a2:
                return
            if start == len(num):
                if a1 > -1 and a2 > -1 and a3 > -1:
                    ans[0] += 1
                return
            for i in range(start, len(num)):
                cur = int(num[start: i + 1])
                if a1 == -1:
                    backtracking(i + 1, cur, a2, a3)
                elif a2 == - 1:
                    backtracking(i + 1, a1, cur, a3)
                elif a3 == -1:
                    backtracking(i + 1, a1, a2, cur)
                else:
                    if cur > a2 + a3:
                        break
                    backtracking(i + 1, a2, a3, cur)
                if cur == 0:
                    break

        ans = [0]
        backtracking(0, -1, -1, -1)
        return ans[0] > 0

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        # 每次递归都会确定一个数字，这个数字有多种可能，具体几种取决于里面的 for 循环。
        def dfs(start, a, b, picked_cnt):
            if start == len(num) and picked_cnt > 2: return True # 找到了
            # 确定一个数字的过程，即上面例子中的 1xxxxx，11xxxx，112xxx，1123xx
            for i in range(start, len(num)):
                if num[start] == '0' and i != start: return False # 不能以 0 开头，除非是 0 本身
                if picked_cnt < 2 and dfs(i + 1, b, int(num[start:i+1] or '0'), picked_cnt + 1): return True
                if int(num[start:i+1] or '0') == a + b and dfs(i + 1, b, int(num[start:i+1] or '0'), picked_cnt + 1): return True
            return False
        if len(num) < 3: return False
        return dfs(0, 0, 0, 0)

# leetcode submit region end(Prohibit modification and deletion)
# num = "112358"
# num = "199100199"
# num = "113"
# num = "101"
num = "0"
# num = "1023"
# num = "199111992"
print(Solution().isAdditiveNumber(num))