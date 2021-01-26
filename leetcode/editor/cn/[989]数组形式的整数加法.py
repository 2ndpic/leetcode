# 对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。 
# 
#  给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：A = [1,2,0,0], K = 34
# 输出：[1,2,3,4]
# 解释：1200 + 34 = 1234
#  
# 
#  示例 2： 
# 
#  输入：A = [2,7,4], K = 181
# 输出：[4,5,5]
# 解释：274 + 181 = 455
#  
# 
#  示例 3： 
# 
#  输入：A = [2,1,5], K = 806
# 输出：[1,0,2,1]
# 解释：215 + 806 = 1021
#  
# 
#  示例 4： 
# 
#  输入：A = [9,9,9,9,9,9,9,9,9,9], K = 1
# 输出：[1,0,0,0,0,0,0,0,0,0,0]
# 解释：9999999999 + 1 = 10000000000
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 10000 
#  0 <= A[i] <= 9 
#  0 <= K <= 10000 
#  如果 A.length > 1，那么 A[0] != 0 
#  
#  Related Topics 数组 
#  👍 93 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
def s1(A: List[int], K: int) -> List[int]:
    k_list = [] if K else [0]
    while K:
        k_list.append(K % 10)
        K //= 10
    k_list = k_list[::-1]
    m, n = len(A), len(k_list)
    flag = 0
    for i in range(max(m, n)):
        ai, ki = m - 1 - i, n - 1 - i
        if ai >= 0 and ki >= 0:
            tmp = A[ai] + k_list[ki] + flag
        elif ai >= 0:
            tmp = A[ai] + flag
        elif ki >= 0:
            tmp = k_list[ki] + flag
        flag = tmp // 10
        tmp %= 10
        if m >= n:
            A[ai] = tmp
        else:
            k_list[ki] = tmp

    if flag == 1:
        if m >= n:
            A = [1] + A
        else:
            k_list = [1] + k_list
    return A if m >= n else k_list

def s2(A: List[int], K: int) -> List[int]:
    B = [int(i) for i in str(K)]
    an, bn, flag = len(A), len(B), 0
    if an < bn:
        A, B, an, bn = B, A, bn, an
    for i in range(an):
        b = B[bn-1-i] if i < bn else 0
        A[an-1-i] += b + flag
        flag = A[an-1-i] // 10
        A[an-1-i] %= 10
        if flag == 0 and i > bn:
            return A
    return [1]+A if flag else A

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        B = [int(i) for i in list(str(K))]
        if len(A) < len(B):
            A,B = B,A
        K = int("".join(str(i) for i in B))
        A = [0] + A
        n = len(A)-1
        while K:
            A[n] = A[n] + K
            K = A[n] // 10
            A[n] %= 10
            n -= 1
        return A if A[0] > 0 else A[1:]



        
# leetcode submit region end(Prohibit modification and deletion)
A=[99]
K=1
print(Solution().addToArrayForm(A,K))