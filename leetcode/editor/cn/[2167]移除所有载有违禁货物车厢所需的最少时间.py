# 给你一个下标从 0 开始的二进制字符串 s ，表示一个列车车厢序列。s[i] = '0' 表示第 i 节车厢 不 含违禁货物，而 s[i] = '1' 表示
# 第 i 节车厢含违禁货物。 
# 
#  作为列车长，你需要清理掉所有载有违禁货物的车厢。你可以不限次数执行下述三种操作中的任意一个： 
# 
#  
#  从列车 左 端移除一节车厢（即移除 s[0]），用去 1 单位时间。 
#  从列车 右 端移除一节车厢（即移除 s[s.length - 1]），用去 1 单位时间。 
#  从列车车厢序列的 任意位置 移除一节车厢，用去 2 单位时间。 
#  
# 
#  返回移除所有载有违禁货物车厢所需要的 最少 单位时间数。 
# 
#  注意，空的列车车厢序列视为没有车厢含违禁货物。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "1100101"
# 输出：5
# 解释：
# 一种从序列中移除所有载有违禁货物的车厢的方法是：
# - 从左端移除一节车厢 2 次。所用时间是 2 * 1 = 2 。
# - 从右端移除一节车厢 1 次。所用时间是 1 。
# - 移除序列中间位置载有违禁货物的车厢。所用时间是 2 。
# 总时间是 2 + 1 + 2 = 5 。
# 
# 一种替代方法是：
# - 从左端移除一节车厢 2 次。所用时间是 2 * 1 = 2 。
# - 从右端移除一节车厢 3 次。所用时间是 3 * 1 = 3 。
# 总时间也是 2 + 3 = 5 。
# 
# 5 是移除所有载有违禁货物的车厢所需要的最少单位时间数。
# 没有其他方法能够用更少的时间移除这些车厢。 
# 
#  示例 2： 
# 
#  
# 输入：s = "0010"
# 输出：2
# 解释：
# 一种从序列中移除所有载有违禁货物的车厢的方法是：
# - 从左端移除一节车厢 3 次。所用时间是 3 * 1 = 3 。
# 总时间是 3.
# 
# 另一种从序列中移除所有载有违禁货物的车厢的方法是：
# - 移除序列中间位置载有违禁货物的车厢。所用时间是 2 。
# 总时间是 2.
# 
# 另一种从序列中移除所有载有违禁货物的车厢的方法是：
# - 从右端移除一节车厢 2 次。所用时间是 2 * 1 = 2 。
# 总时间是 2.
# 
# 2 是移除所有载有违禁货物的车厢所需要的最少单位时间数。
# 没有其他方法能够用更少的时间移除这些车厢。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 2 * 10⁵ 
#  s[i] 为 '0' 或 '1' 
#  
#  Related Topics 字符串 动态规划 👍 26 👎 0
class Solution:
    def minimumTime(self, s: str) -> int:
        n = len(s)
        withoutFirst = [0] * (n + 1) # withoutFirst[i]表示s[i:]不用方法一删除的最少时间
        withoutSecond = [0] * (n + 1) # withoutSecond[i]表示s[0,..,i)不用方法二最少时间
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                withoutFirst[i] = withoutFirst[i + 1]
            else:
                withoutFirst[i] = min(withoutFirst[i + 1] + 2, n - i)
        for i in range(1, n + 1):
            if s[i - 1] == "0":
                withoutSecond[i] = withoutSecond[i - 1]
            else:
                withoutSecond[i] = min(withoutSecond[i - 1] + 2, i)
        ans = n
        for i in range(n + 1):
            ans = min(ans, withoutFirst[i] + withoutSecond[i])
        return ans

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumTime(self, s: str) -> int:
        """
        最终的移除方法为以下两种情况
        1.全部移除
        2.[0,i)全部移除，(j,n)全部移除，[i,j]区间内的1被移除,其中i <= j
        情况2花费时间：i + (n - j - 1) + 2 * Count(i, j)
        利用前缀和可以计算出[i, j]区间内的1: i + (n - j - 1) + 2 * (pre[j] - pre[i - 1])
        把式子拆分合并成三部分：与i有关的项，与j有关的项，以及常数项
        (i - 2 * pre[i - 1]) + (2 * pre[j] - j) + (n - 1)
        在O(n)条件下求上式子最小值
        - 从小到达枚举j，使用变量prebest记录(i - 2 * pre[i - 1])的最小值
        - 对于当前j，先用s[j]更新presum,再用prebest+(2 * pre[j] - j)更新答案
        - 遍历完成后，将答案加上n-1
        """
        n, ans = len(s), float('inf')
        prebest, presum = 0, 0
        for j, ch in enumerate(s):
            prebest = min(prebest, j - 2 * presum)
            presum += int(ch)
            ans = min(ans, prebest + 2 * presum - j)
        return min(ans + n - 1, n)
# leetcode submit region end(Prohibit modification and deletion)
