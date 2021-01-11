# 给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。 
# 
# 
#  你可以 任意多次交换 在 pairs 中任意一对索引处的字符。 
# 
#  返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。 
# 
#  
# 
#  示例 1: 
# 
#  输入：s = "dcab", pairs = [[0,3],[1,2]]
# 输出："bacd"
# 解释： 
# 交换 s[0] 和 s[3], s = "bcad"
# 交换 s[1] 和 s[2], s = "bacd"
#  
# 
#  示例 2： 
# 
#  输入：s = "dcab", pairs = [[0,3],[1,2],[0,2]]
# 输出："abcd"
# 解释：
# 交换 s[0] 和 s[3], s = "bcad"
# 交换 s[0] 和 s[2], s = "acbd"
# 交换 s[1] 和 s[2], s = "abcd" 
# 
#  示例 3： 
# 
#  输入：s = "cba", pairs = [[0,1],[1,2]]
# 输出："abc"
# 解释：
# 交换 s[0] 和 s[1], s = "bca"
# 交换 s[1] 和 s[2], s = "bac"
# 交换 s[0] 和 s[1], s = "abc"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10^5 
#  0 <= pairs.length <= 10^5 
#  0 <= pairs[i][0], pairs[i][1] < s.length 
#  s 中只含有小写英文字母 
#  
#  Related Topics 并查集 数组 
#  👍 100 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)

def find(u, parents):
    if parents[u] == u:
        return u
    parents[u] = find(parents[u], parents)
    return parents[u]
def union(u, v, ranks, parents):
    pu, pv = find(u, parents), find(v, parents)
    if pu == pv:
        return False
    ru, rv = ranks[u], ranks[v]
    if ru > rv:
        parents[pv] = pu
    elif rv > ru:
        parents[pu] = pv
    else:
        parents[pv] = pu
        ranks[pu] += 1
    return True

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parents = [i for i in range(len(s))]
        ranks = [0] * len(s)

        for u, v in pairs:
            union(u, v, ranks, parents)

        groups = {}
        for i in range(len(s)):
            groups.setdefault(find(i, parents), [0]*26)[ord(s[i])-ord('a')] += 1

        res = [None] * len(s)
        for index, boss in enumerate(parents):
            for i in range(26):
                if groups[boss][i] > 0:
                    tmp = chr(i+97)
                    res[index] = tmp
                    groups[boss][i] -= 1
                    break

        return "".join(res)


        
# leetcode submit region end(Prohibit modification and deletion)
s = "dcab"
pairs = [[0,3],[1,2]]
print(Solution().smallestStringWithSwaps(s, pairs))