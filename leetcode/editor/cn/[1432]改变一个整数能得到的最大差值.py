# 给你一个整数 num 。你可以对它进行如下步骤恰好 两次 ： 
# 
#  
#  选择一个数字 x (0 <= x <= 9). 
#  选择另一个数字 y (0 <= y <= 9) 。数字 y 可以等于 x 。 
#  将 num 中所有出现 x 的数位都用 y 替换。 
#  得到的新的整数 不能 有前导 0 ，得到的新整数也 不能 是 0 。 
#  
# 
#  令两次对 num 的操作得到的结果分别为 a 和 b 。 
# 
#  请你返回 a 和 b 的 最大差值 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：num = 555
# 输出：888
# 解释：第一次选择 x = 5 且 y = 9 ，并把得到的新数字保存在 a 中。
# 第二次选择 x = 5 且 y = 1 ，并把得到的新数字保存在 b 中。
# 现在，我们有 a = 999 和 b = 111 ，最大差值为 888
#  
# 
#  示例 2： 
# 
#  输入：num = 9
# 输出：8
# 解释：第一次选择 x = 9 且 y = 9 ，并把得到的新数字保存在 a 中。
# 第二次选择 x = 9 且 y = 1 ，并把得到的新数字保存在 b 中。
# 现在，我们有 a = 9 和 b = 1 ，最大差值为 8
#  
# 
#  示例 3： 
# 
#  输入：num = 123456
# 输出：820000
#  
# 
#  示例 4： 
# 
#  输入：num = 10000
# 输出：80000
#  
# 
#  示例 5： 
# 
#  输入：num = 9288
# 输出：8700
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= num <= 10^8 
#  
#  Related Topics 贪心 数学 👍 18 👎 0
class Solution:
    def maxDiff(self, num: int) -> int:
        max_num, min_num = num, num
        change = lambda x, y: str(num).replace(str(x), str(y))
        for x in range(10):
            for y in range(10):
                res = change(x, y)
                if res[0] != "0":
                    res_i = int(res)
                    max_num = max(max_num, res_i)
                    min_num = min(min_num, res_i)
        return max_num - min_num

class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)
        max_num, change1 = 0, ""
        min_num, change2, flag = 0, "", 0
        for i, ch in enumerate(num_str):
            if not change1 and ch != "9": change1 = ch
            max_num = max_num * 10 + (9 if change1 == ch else int(ch))
            if i == 0:
                if ch != "1":
                    change2 = ch
                    flag = 1
            elif not change2 and ch not in "01":
                change2 = ch
            min_num = min_num * 10 + (flag if change2 == ch else int(ch))
        return max_num - min_num

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxDiff(self, num: int) -> int:
        min_num, max_num = str(num), str(num)
        for digit in max_num:
            if digit != "9":
                max_num = max_num.replace(digit, "9")
                break

        for i, digit in enumerate(min_num):
            if i == 0:
                if digit != "1":
                    min_num = min_num.replace(digit, "1")
                    break
            else:
                if digit != "0" and digit != min_num[0]:
                    min_num = min_num.replace(digit, "0")
                    break
        return int(max_num) - int(min_num)
# leetcode submit region end(Prohibit modification and deletion)
