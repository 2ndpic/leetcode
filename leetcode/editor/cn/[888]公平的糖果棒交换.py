# 爱丽丝和鲍勃有不同大小的糖果棒：A[i] 是爱丽丝拥有的第 i 根糖果棒的大小，B[j] 是鲍勃拥有的第 j 根糖果棒的大小。 
# 
#  因为他们是朋友，所以他们想交换一根糖果棒，这样交换后，他们都有相同的糖果总量。（一个人拥有的糖果总量是他们拥有的糖果棒大小的总和。） 
# 
#  返回一个整数数组 ans，其中 ans[0] 是爱丽丝必须交换的糖果棒的大小，ans[1] 是 Bob 必须交换的糖果棒的大小。 
# 
#  如果有多个答案，你可以返回其中任何一个。保证答案存在。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：A = [1,1], B = [2,2]
# 输出：[1,2]
#  
# 
#  示例 2： 
# 
#  
# 输入：A = [1,2], B = [2,3]
# 输出：[1,2]
#  
# 
#  示例 3： 
# 
#  
# 输入：A = [2], B = [1,3]
# 输出：[2,3]
#  
# 
#  示例 4： 
# 
#  
# 输入：A = [1,2,5], B = [2,4]
# 输出：[5,4]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 10000 
#  1 <= B.length <= 10000 
#  1 <= A[i] <= 100000 
#  1 <= B[i] <= 100000 
#  保证爱丽丝与鲍勃的糖果总量不同。 
#  答案肯定存在。 
#  
#  Related Topics 数组 
#  👍 96 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
def s1(A: List[int], B: List[int]) -> List[int]:
    a_sum = sum(A)
    b_sum = sum(B)
    average = (a_sum + b_sum) // 2
    b = set(B)
    for a_i in A:
        b_i = average - (a_sum - a_i)
        if b_i in b:
            return [a_i, b_i]
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        a_sum = sum(A)
        b_sum = sum(B)
        delta = (a_sum - b_sum) // 2
        a = set(A)
        for b_i in B:
            if delta + b_i in a:
                return [delta + b_i, b_i]
        
# leetcode submit region end(Prohibit modification and deletion)
A = [1,2,5]
B = [2,4]
a_1, b_1 = Solution().fairCandySwap(A, B)
print(a_1, b_1)
print(sum(A) - a_1 + b_1, sum(B) - b_1 + a_1, sum(A) - a_1 + b_1 == sum(B) - b_1 + a_1)