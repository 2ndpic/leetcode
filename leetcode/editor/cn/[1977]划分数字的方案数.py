# 你写下了若干 正整数 ，并将它们连接成了一个字符串 num 。但是你忘记给这些数字之间加逗号了。你只记得这一列数字是 非递减 的且 没有 任何数字有前导 0
#  。 
# 
#  请你返回有多少种可能的 正整数数组 可以得到字符串 num 。由于答案可能很大，将结果对 10⁹ + 7 取余 后返回。 
# 
#  
# 
#  示例 1： 
# 
#  输入：num = "327"
# 输出：2
# 解释：以下为可能的方案：
# 3, 27
# 327
#  
# 
#  示例 2： 
# 
#  输入：num = "094"
# 输出：0
# 解释：不能有数字有前导 0 ，且所有数字均为正数。
#  
# 
#  示例 3： 
# 
#  输入：num = "0"
# 输出：0
# 解释：不能有数字有前导 0 ，且所有数字均为正数。
#  
# 
#  示例 4： 
# 
#  输入：num = "9999999999999"
# 输出：101
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= num.length <= 3500 
#  num 只含有数字 '0' 到 '9' 。 
#  
#  Related Topics 字符串 动态规划 后缀数组 👍 15 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfCombinations(self, num: str) -> int:
        """
        f[i][j]表示对字符串num的第i个字符进行划分，并且最后一个数字使用了第j个字符的方案数
        为了叙述方便用num(i,j)表示该数
        有这样一个事实：如果数a的位数严格大于b的位数，那么a一定严格大于b
        f[i][j]中的位数为j-i+1，那么上一个数的位数小于等于j-i即可进行转移。
        上一个数的结尾在位置i-1,设开始下标为x，那么需要(i - 1) - x + 1 <= j - i, x >= 2i-j
        f[i][j]对应的状态即为f[2i-j][i-1], f[2i-j+1][i-1], ..., f[i-1][i-1]
        此外还需要比较数位同为j-i+1的num(2i-j-1, i-1)和num(i,j)的大小关系
        如果前者小于后者，那么f[i][j]还可以从f[2i-j-i][i-1]转移而来。因此状态转移方程为：
        if num(2i-j-1, i-1) > num(i-1):
            f[i][j] = sum(f[k][i-1]) 2i-j <= k <= i - 1
        if num(2i-j-1, i-1) <= num(i-1):
            f[i][j] = sum(f[k][i-1]) 2i-j-1 <= k <= i - 1
        注意：这里k的最小值不能小于0
             num(i,j)不能含有前导0，如果num[i]=0，那么f[i][j]=0,特别地，如果num[0]=0，那么直接返回0作为答案
        动态规划地边界条件为f[0][..]=1，其余地状态的初始值均为0.最终答案为所有的f[..][n-1]的和

        即使不考虑如何快速比较num(2i-j-1, i-1)和num(i, j)的大小关系，上诉动态规划的时间复杂度为O(N^3)
        然而计算f[i][j]的过程是可以用前缀和进行优化。设pre[i][j]=sum(f[k][j]) 0<=k<=i
        那么状态转移方程就可以改写为：
        if num(2i-j-1, i-1) > num(i, j):
            f[i][j] = pre[i-1][i-1] - pre[2i-j-1][i-1]
        if num(2i-j-1, i-1) <= num(i, j):
            f[i][j] = pre[i-1][i-1] - pre[2i-j-2][i-1]

        此外，也无需显示地使用前缀和数组：如果按照先枚举i再枚举j地顺序计算f[i][j]，那么有
        f[i][j] = sum(f[k][i-1]) 2i-j <= k <= i - 1
        这里不考虑num(2i-j-1, i-1)和num(i, j)的大小关系，即使前者小于等于后者，多出地f[2i-j-1][i-1]这一项也可以O(1)的时间累加进f[i][j]
        当j->j+1时候：2i - j - 1 <= k
            f[i][j+1] = sum(f[k][i-1]) 2i-j-1 <= k <= i - 1
        可以发现f[i][j+1]比f[i][j]只多出了f[2i-j-1][i-1]这一项，因此在求得f[i][j]的前提下，不考虑字符串比较，可以在O(1)时间得到f[i][j+1]

        ## 快速比较两个数的大小关系
        此时，只剩下最后一步，就是快速比较num(2i-j-1, i-1)和num(i, j)的大小关系,需要在O(1)的时间完成
        这一步可以使用预处理巧妙地解决
        记lcp[i][j]表示在字符串中，以i开始的后缀与j开始的后缀的最长公共前缀的长度，直观上它表示
        x = k + i - 1
        num(i, lcp(i, j) + i - 1) = num(j, lcp(i, j) + j - 1)
        num[lcp(i, j) + i] != num[lcp(i, j) + j]
        lcp[i][j]可以很方便使用动态规划求出，即：
        if num[i] == num[j]:
            lcp[i][j] = 1 + lcp[i+1][j+1]
        else:
            lcp[i][j] = 0
        求出lcp后，就可以很方便地比较num两个子串地大小关系了。对于num(2i-j-1, i-1)和num(i, j)
        - 如果lcp[2i-j-1][i] >= j - i + 1
            那么num(2i-j-1, i-1)一定等于num(i, j)
        - 如果lcp[2i-j-1][i] < j - i + 1
            那么num(2i-j-1, i-1)和num(i, j)的大小关系等同于比较num[2i-j-1 + lcp[2i-j-1][i]] 与 num[i + lcp[2i-j-1][i]]
        """
        mod = 10 ** 9 + 7
        if num[0] == "0": return 0

        n = len(num)

        # 预处理lcp
        lcp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            lcp[i][n - 1] = int(num[i] == num[n - 1])
            for j in range(i + 1, n - 1):
                lcp[i][j] = (lcp[i + 1][j + 1] + 1) if num[i] == num[j] else 0

        # 动态规划
        f = [[0] * n for _ in range(n)]
        # 边界f[0][..] = 1
        for i in range(n):
            f[0][i] = 1

        for i in range(1, n):
            if num[i] == "0": continue
            # 前缀和
            presum = 0
            for j in range(i, n):
                f[i][j] = presum
                # 使用 lcp 比较 num(2i-j-1,i-1) 与 num(i,j) 的大小关系
                if 2 * i - j - 1 >= 0:
                    if lcp[2 * i - j - 1][i] >= j - i + 1 or \
                       num[2 * i - j - 1 + lcp[2 * i - j - 1][i]] < num[i + lcp[2 * i - j - 1][i]]:
                        f[i][j] = (f[i][j] + f[2 * i - j - 1][i - 1]) % mod
                    # 更新前缀和
                    presum += f[2 * i - j - 1][i - 1]
        ans = sum(f[i][n - 1] for i in range(n)) % mod
        return ans
# leetcode submit region end(Prohibit modification and deletion)
print(Solution().numberOfCombinations("9999999999999"))