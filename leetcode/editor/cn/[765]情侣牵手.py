# N 对情侣坐在连续排列的 2N 个座位上，想要牵到对方的手。 计算最少交换座位的次数，以便每对情侣可以并肩坐在一起。 一次交换可选择任意两人，让他们站起来交
# 换座位。 
# 
#  人和座位用 0 到 2N-1 的整数表示，情侣们按顺序编号，第一对是 (0, 1)，第二对是 (2, 3)，以此类推，最后一对是 (2N-2, 2N-1)
# 。 
# 
#  这些情侣的初始座位 row[i] 是由最初始坐在第 i 个座位上的人决定的。 
# 
#  示例 1: 
# 
#  
# 输入: row = [0, 2, 1, 3]
# 输出: 1
# 解释: 我们只需要交换row[1]和row[2]的位置即可。
#  
# 
#  示例 2: 
# 
#  
# 输入: row = [3, 2, 0, 1]
# 输出: 0
# 解释: 无需交换座位，所有的情侣都已经可以手牵手了。
#  
# 
#  说明: 
# 
#  
#  len(row) 是偶数且数值在 [4, 60]范围内。 
#  可以保证row 是序列 0...len(row)-1 的一个全排列。 
#  
#  Related Topics 贪心算法 并查集 图 
#  👍 219 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
def find(u, parents):
    if u != parents[u]:
        parents[u] = find(parents[u], parents)
    return parents[u]

def union(u, v, parents, ranks):
    pu, pv = find(u, parents), find(v, parents)
    if pu == pv:
        return False
    if ranks[pu] > ranks[pv]:
        parents[pv] = pu
    elif ranks[pv] > ranks[pu]:
        parents[pu] = pv
    else:
        parents[pv] = pu
        ranks[pu] += 1
    return True

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row) // 2
        parents = [i for i in range(n)]
        ranks = [0 for _ in range(n)]
        for i in range(0, len(row), 2):
            cp1, cp2 = row[i]//2, row[i + 1]//2
            union(cp1, cp2, parents, ranks)
        # groups = set()
        # for i in range(n):
        #     groups.add(find(i, parents))
        m = 0
        for i in range(n):
            if i == find(i, parents):
                m += 1
        """
        n是总节点个数，若k代表集合中的节点，则一个集合中需要交换的次数为k - 1
        如果一个m个集合，节点数分别为{k1, k2, ..., km}
        则总共需要交换的次数为：k1-1 + k2-1 + k3-1 ... + km - 1 = n - m
        """
        return n - m
        
# leetcode submit region end(Prohibit modification and deletion)
