# 给你一个下标从 0 开始的字符串数组 words 。每个字符串都只包含 小写英文字母 。words 中任意一个子串中，每个字母都至多只出现一次。 
# 
#  如果通过以下操作之一，我们可以从 s1 的字母集合得到 s2 的字母集合，那么我们称这两个字符串为 关联的 ： 
# 
#  
#  往 s1 的字母集合中添加一个字母。 
#  从 s1 的字母集合中删去一个字母。 
#  将 s1 中的一个字母替换成另外任意一个字母（也可以替换为这个字母本身）。 
#  
# 
#  数组 words 可以分为一个或者多个无交集的 组 。如果一个字符串与另一个字符串关联，那么它们应当属于同一个组。 
# 
#  注意，你需要确保分好组后，一个组内的任一字符串与其他组的字符串都不关联。可以证明在这个条件下，分组方案是唯一的。 
# 
#  请你返回一个长度为 2 的数组 ans ： 
# 
#  
#  ans[0] 是 words 分组后的 总组数 。 
#  ans[1] 是字符串数目最多的组所包含的字符串数目。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：words = ["a","b","ab","cde"]
# 输出：[2,3]
# 解释：
# - words[0] 可以得到 words[1] （将 'a' 替换为 'b'）和 words[2] （添加 'b'）。所以 words[0] 与 
# words[1] 和 words[2] 关联。
# - words[1] 可以得到 words[0] （将 'b' 替换为 'a'）和 words[2] （添加 'a'）。所以 words[1] 与 
# words[0] 和 words[2] 关联。
# - words[2] 可以得到 words[0] （删去 'b'）和 words[1] （删去 'a'）。所以 words[2] 与 words[0] 和 
# words[1] 关联。
# - words[3] 与 words 中其他字符串都不关联。
# 所以，words 可以分成 2 个组 ["a","b","ab"] 和 ["cde"] 。最大的组大小为 3 。
#  
# 
#  示例 2： 
# 
#  
# 输入：words = ["a","ab","abc"]
# 输出：[1,3]
# 解释：
# - words[0] 与 words[1] 关联。
# - words[1] 与 words[0] 和 words[2] 关联。
# - words[2] 与 words[1] 关联。
# 由于所有字符串与其他字符串都关联，所以它们全部在同一个组内。
# 所以最大的组大小为 3 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= words.length <= 2 * 10⁴ 
#  1 <= words[i].length <= 26 
#  words[i] 只包含小写英文字母。 
#  words[i] 中每个字母最多只出现一次。 
#  
#  Related Topics 位运算 并查集 字符串 👍 27 👎 0
from typing import List
from collections import defaultdict
from collections import Counter
class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        """
        简单版本
        """
        def find(u):
            if parents[u] != u:
                parents[u] = find(parents[u])
            return parents[u]

        def union(u, v):
            if v not in parents: return
            pu, pv = find(u), find(v)
            if pu == pv: return
            if rank[pu] > rank[pv]:
                parents[pv] = pu
            elif rank[pv] > rank[pu]:
                parents[pu] = pv
            else:
                parents[pv] = pu
                rank[pu] += 1

        parents, rank, w2m = {}, defaultdict(int), {}
        for word in words:
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))
            w2m[word] = mask
            parents[mask], rank[mask] = mask, 1

        for mask in parents:
            for i in range(26):
                union(mask, mask ^ (1 << i)) # 添加或者删除
                if mask & (1 << i):
                    for j in range(26):
                        if mask & (1 << j) == 0:
                            union(mask, mask ^ (1 << i) | (1 << j))


        groups, maxsize = defaultdict(int), 0
        for word in words:
            mask = find(w2m[word])
            groups[mask] += 1
            maxsize = max(maxsize, groups[mask])
        return [len(groups), maxsize]

class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        """
        优化常数版本
        """
        def find(u):
            if parents[u] != u:
                parents[u] = find(parents[u])
            return parents[u]

        def union(u, v):
            nonlocal groups, maxsize
            if v not in parents: return
            pu, pv = find(u), find(v)
            if pu == pv: return
            if rank[pu] > rank[pv]:
                parents[pv] = pu
                size[pu] += size[pv]
                maxsize = max(maxsize, size[pu])
            elif rank[pv] > rank[pu]:
                parents[pu] = pv
                size[pv] += size[pu]
                maxsize = max(maxsize, size[pv])
            else:
                parents[pv] = pu
                rank[pu] += 1
                size[pu] += size[pv]
                maxsize = max(maxsize, size[pu])
            groups -= 1


        parents, rank, size = {}, {}, defaultdict(int)
        maxsize = 0
        for word in words:
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))
            parents[mask], rank[mask], size[mask] = mask, 1, size[mask] + 1
            maxsize = max(maxsize, size[mask])

        groups = len(parents)

        for mask in parents:
            for i in range(26):
                union(mask, mask ^ (1 << i)) # 添加或者删除
                if mask & (1 << i):
                    for j in range(26):
                        if mask & (1 << j) == 0:
                            union(mask, mask ^ (1 << i) | (1 << j))
        return [groups, maxsize]


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        """
        替换操作优化一个26
        """
        def find(u):
            if parents.setdefault(u, u) != u:
                parents[u] = find(parents[u])
            return parents[u]

        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv: return
            if rank[pu] > rank[pv]:
                parents[pv] = pu
            elif rank[pv] > rank[pu]:
                parents[pu] = pv
            else:
                parents[pv] = pu
                rank[pu] += 1

        parents, rank, w2m = {}, defaultdict(int), {}
        for word in words:
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))
            w2m[word] = mask
            parents[mask], rank[mask] = mask, 1

        for mask in w2m.values():
            for i in range(26):
                if (other := mask ^ (1 << i)) in parents:
                    union(mask, other)  # 添加或者删除
                if mask & (1 << i):
                    union(mask, other | (1 << 27))  # 替换

        d = Counter(find(w2m[word]) for word in words)
        return [len(d), max(d.values())]
# leetcode submit region end(Prohibit modification and deletion)
print(Solution().groupStrings(["j"]))