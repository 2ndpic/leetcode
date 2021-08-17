# 给你一个字符串 s 表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字符： 
# 
#  
#  'A'：Absent，缺勤 
#  'L'：Late，迟到 
#  'P'：Present，到场 
#  
# 
#  如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励： 
# 
#  
#  按 总出勤 计，学生缺勤（'A'）严格 少于两天。 
#  学生 不会 存在 连续 3 天或 3 天以上的迟到（'L'）记录。 
#  
# 
#  如果学生可以获得出勤奖励，返回 true ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "PPALLP"
# 输出：true
# 解释：学生缺勤次数少于 2 次，且不存在 3 天或以上的连续迟到记录。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "PPALLL"
# 输出：false
# 解释：学生最后三天连续迟到，所以不满足出勤奖励的条件。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s[i] 为 'A'、'L' 或 'P' 
#  
#  Related Topics 字符串 
#  👍 95 👎 0
class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count("A") > 1: return False
        pre = -1
        for i in range(len(s)):
            if s[i] == "L" and pre == -1:
                pre = i
            elif s[i] != "L" and pre != -1:
                if i - pre >= 3: return False
                pre = -1
            elif i == len(s) - 1 and s[i] == "L":
                if i - pre + 1 >= 3: return False
        return True

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkRecord(self, s: str) -> bool:
        absents = lates = 0
        for i, c in enumerate(s):
            if c == "A":
                absents += 1
                if absents > 1: return False
            if c == "L":
                lates += 1
                if lates >= 3: return False
            else:
                lates = 0
        return True
# leetcode submit region end(Prohibit modification and deletion)
