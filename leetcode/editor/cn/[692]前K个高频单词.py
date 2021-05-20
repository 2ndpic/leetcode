# 给一非空的单词列表，返回前 k 个出现次数最多的单词。 
# 
#  返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。 
# 
#  示例 1： 
# 
#  
# 输入: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# 输出: ["i", "love"]
# 解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
#     注意，按字母顺序 "i" 在 "love" 之前。
#  
# 
#  
# 
#  示例 2： 
# 
#  
# 输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k
#  = 4
# 输出: ["the", "is", "sunny", "day"]
# 解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
#     出现次数依次为 4, 3, 2 和 1 次。
#  
# 
#  
# 
#  注意： 
# 
#  
#  假定 k 总为有效值， 1 ≤ k ≤ 集合元素数。 
#  输入的单词均由小写字母组成。 
#  
# 
#  
# 
#  扩展练习： 
# 
#  
#  尝试以 O(n log k) 时间复杂度和 O(n) 空间复杂度解决。 
#  
#  Related Topics 堆 字典树 哈希表 
#  👍 260 👎 0

from typing import List
import collections
import heapq
class Word:
    def __init__(self, w, f):
        self.w = w
        self.f = f
    def __lt__(self, other):
        if self.f < other.f or (self.f == other.f and self.w > other.w):
            return True
        else:
            return False
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        O(nlogk)
        """
        word_freq = [Word(w, f) for w, f in collections.Counter(words).items()]
        heap = []
        for word in word_freq:
            heapq.heappush(heap, word)
            if len(heap) > k:
                heapq.heappop(heap)
        ans = [""] * k
        for i in range(k - 1, -1, -1):
            ans[i] = heapq.heappop(heap).w
        return ans

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        O(nlogn)
        """
        num_dic = dict(collections.Counter(words))
        h = []
        res = []
        for key, value in num_dic.items():
            heapq.heappush(h, (-value, key))  # 按第一个键值进行排序，堆顶是最小值
        for _ in range(k):
            res.append(heapq.heappop(h)[1])
        return res
# leetcode submit region end(Prohibit modification and deletion)
# words = ["i", "love", "leetcode", "i", "love", "coding"];k = 2
words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]; k = 4
words = ["i", "love", "leetcode", "i", "love", "coding"]; k = 3
words = ["aaa","aa","a"]; k = 2
print(Solution().topKFrequent(words, k))
