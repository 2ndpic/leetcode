from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
#         get_vetor = lambda a, b: (a[0] - b[0], a[1] - b[1])
#         vetors = [get_vetor(p2, p1), get_vetor(p3, p1), get_vetor(p4, p1)]
#         for i, v in enumerate(vetors):
#             if vetors[i - 1][0] * vetors[i - 2][0] + vetors[i - 1][1] * vetors[i - 2][1] == 0 and \
#                 vetors[i - 1][0] ** 2 + vetors[i - 1][1] ** 2 > 0 and \
#                     vetors[i - 1][0] ** 2 + vetors[i - 1][1] ** 2 == vetors[i - 2][0] ** 2 + vetors[i - 2][1] ** 2 and \
#                         (vetors[i - 1][0] + vetors[i - 2][0], vetors[i - 1][1] + vetors[i - 2][1]) == v:
#                 return True
#         return False

def checkMidPoint(p1, p2, p3, p4):
    return p1[0] + p2[0] == p3[0] + p4[0] and p1[1] + p2[1] == p3[1] + p4[1]

def checkLength(v1, v2):
    return v1[0] ** 2 + v1[1] ** 2 == v2[0] ** 2 + v2[1] ** 2

def calCos(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]

def help(p1, p2, p3, p4):
    v1 = (p1[0] - p2[0], p1[1] - p2[1])
    v2 = (p3[0] - p4[0], p3[1] - p4[1])
    return checkMidPoint(p1, p2, p3, p4) and checkLength(v1, v2) and calCos(v1, v2) == 0

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1 == p2:
            return False
        if help(p1, p2, p3, p4):
            return True
        if p1 == p3:
            return False
        if help(p1, p3, p2, p4):
            return True
        if p1 == p4:
            return False
        if help(p1, p4, p2, p3):
            return True
        return False
# leetcode submit region end(Prohibit modification and deletion)
p1 = [0,0]
p2 = [1,1]
p3 = [1,0]
p4 = [0,1]
print(Solution().validSquare(p1, p2, p3, p4))