# 给你一个 n 行 m 列的矩阵，最开始的时候，每个单元格中的值都是 0。 
# 
#  另有一个索引数组 indices，indices[i] = [ri, ci] 中的 ri 和 ci 分别表示指定的行和列（从 0 开始编号）。 
# 
#  你需要将每对 [ri, ci] 指定的行和列上的所有单元格的值加 1。 
# 
#  请你在执行完所有 indices 指定的增量操作后，返回矩阵中 「奇数值单元格」 的数目。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：n = 2, m = 3, indices = [[0,1],[1,1]]
# 输出：6
# 解释：最开始的矩阵是 [[0,0,0],[0,0,0]]。
# 第一次增量操作后得到 [[1,2,1],[0,1,0]]。
# 最后的矩阵是 [[1,3,1],[1,3,1]]，里面有 6 个奇数。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：n = 2, m = 2, indices = [[1,1],[0,0]]
# 输出：0
# 解释：最后的矩阵是 [[2,2],[2,2]]，里面没有奇数。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 50 
#  1 <= m <= 50 
#  1 <= indices.length <= 100 
#  0 <= indices[i][0] < n 
#  0 <= indices[i][1] < m 
#  
#  Related Topics 数组 
#  👍 41 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        '''
        不考虑列的情况，先把行的数据加完，如果某行出现了偶数次，那么这行的所有数据都是偶数,假如一共有rows行出现奇数次，那么一共m*rows个奇数
        不考虑行的情况，如果有一共有cols列出现奇数次，那么一共有n*cols个奇数

        现在放到两个一起考虑，在Matirx[i][j]加了行数据变成奇数后，又加了个列数据就转换成偶数了，所以在最后统计中要减去这个点
        '''
        times_rows = collections.Counter(i[0] for i in indices)
        times_cols = collections.Counter(i[1] for i in indices)
        ret, odd_rows = 0, 0
        for row, time in times_rows.items():
            if time % 2:
                ret += m
                odd_rows += 1
        for col, time in times_cols.items():
            if time % 2:
                ret += n
                ret -= odd_rows * 2
        return ret


        
# leetcode submit region end(Prohibit modification and deletion)