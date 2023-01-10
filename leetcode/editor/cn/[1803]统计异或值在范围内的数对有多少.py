from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
"""
# 整体思路
f[x]表示[0, x]的漂亮数对数目，那么答案为f[high] - f[low - 1]
考虑数据范围2 * (10 ** 4)，最多不过 15 位数，可以将每个数换成二进制，存储在字典树中
假设当前遍历到了nums[i]，将nums[0,..,i-1]的信息已经添加到字典树中
针对nums[i]，字典树中有多少nums[j]，使得nums[j] ^ nums[i] <= x，那么总体答案就会增加多少
统计完后再将nums[i]的信息添加到字典树中，这样的遍历查找，漂亮数对就不重不漏
# 核心：如何在字典树中统计出有多少nums[j]，使得nums[j] ^ nums[i] <= x
- 任意nums[j]，nums[j] ^ nums[i] < x 的一个「事实」是：不等式左右两数第14位到第k+1位都相等，第k位则小于
- 所以可以由高位到低位遍历二进制位，按每个二进制位统计符合上诉事实的nums[j]个数
- 假设当前在字典树中走到了第k个二进制位，同时保证了前面经过的路径[第14个二进制位，第k+1个二进制位]与x相等
    - 如果x的第k个二进制位为0，那么不存在使得事实成立的nums[j]。那么就考虑去走到第k-1个二进制位，此时要保证[第14个二进制位，第k个二进制位]与x相等，即保证nums[i] ^ nums[j]第k个二进制位与x的第k个二进制位相等，设nums[i]的第k个二进制位为r，如果r是0，那么就只能往表示0的子节点走；如果r是1，那么就只能往表示1的子节点走；这样才能保证nums[i] ^ nums[j]第k位的值是0，与x相同
    - 如果x的第k位二进制位为1，那么需要统计使 nums[i] ^ nums[j]第k位为0的nums[j]的个数。设nums[i]的第k个二进制位为r，如果r是0，那么统计此路径下第k位为1的个数，下一步就只能往表示1的子节点走；如果r是0，那么统计此路径下第k位为0的个数，下一步只能往表示1的子节点走，这样才能保证nums[i] ^ nums[j]第k位的值是1，与x相同
## 细节
在统计完第k位符合事实的nums[j]后，就可以将nums[i]的信息追加到字典树中了，由于要查询个数，所以字典树要维护数量信息。如果在过程中，出现某个子节点不存在就立刻返回答案。否则在最后，遍历完所有的15个二进制位后，到达的最后一个节点记录的数字是使得nums[i] ^ nums[j] = x条件成立的nums[j]的个数，也将其累加到答案中。
"""
HIGH_BIT = 14
class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.cnt = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, num: int) -> None:
        """
        将num添加到字典树中
        """
        cur = self.root
        for k in range(HIGH_BIT, -1, -1):
            bit = (num >> k) & 1
            if cur.children[bit] is None:
                cur.children[bit] = TrieNode()
            cur = cur.children[bit]
            cur.cnt += 1

    def get(self, num: int, x: int) -> int:
        """
        针对num，统计在字典树中有多少数字a，使得num ^ a <= x
        """
        cur, ans = self.root, 0
        for k in range(HIGH_BIT, -1, -1):
            r = (num >> k) & 1
            if (x >> k) & 1 == 0:
                cur = cur.children[r]
            else:
                if cur.children[r]:
                    ans += cur.children[r].cnt
                cur = cur.children[r ^ 1]
            if cur is None:
                return ans
        ans += cur.cnt
        return ans

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        trie, ans = Trie(), 0
        for i in range(1, len(nums)):
            trie.add(nums[i - 1])
            ans += trie.get(nums[i], high) - trie.get(nums[i], low - 1)
        return ans

# leetcode submit region end(Prohibit modification and deletion)

nums = [9,8,4,2,1]
low = 5
high = 14
print(Solution().countPairs(nums, low, high))