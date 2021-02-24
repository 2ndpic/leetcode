# 给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。 
# 
#  水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。 
# 
#  反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：[[1,1,0],[1,0,1],[0,0,0]]
# 输出：[[1,0,0],[0,1,0],[1,1,1]]
# 解释：首先翻转每一行: [[0,1,1],[1,0,1],[0,0,0]]；
#      然后反转图片: [[1,0,0],[0,1,0],[1,1,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# 输出：[[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# 解释：首先翻转每一行: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]；
#      然后反转图片: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length = A[0].length <= 20 
#  0 <= A[i][j] <= 1 
#  
#  Related Topics 数组 
#  👍 236 👎 0
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        n, m = len(A), len(A[0])
        for i in range(n):
            for j in range((m+1)//2):
                if A[i][j] == A[i][m-1-j]:
                    A[i][j] = A[i][m-1-j] = A[i][j] ^ 1
        return A

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        n, m = len(A), len(A[0])
        for i in range(n):
            l, r = 0, m - 1
            while l <= r:
                if l == r: A[i][l] = 1 - A[i][l]
                else: A[i][l], A[i][r] = (1 - A[i][r]), (1 - A[i][l])
                l += 1
                r -= 1
        return A

        
# leetcode submit region end(Prohibit modification and deletion)
