# 你有一套活字字模 tiles，其中每个字模上都刻有一个字母 tiles[i]。返回你可以印出的非空字母序列的数目。 
# 
#  注意：本题中，每个活字字模只能使用一次。 
# 
#  
# 
#  示例 1： 
# 
#  输入："AAB"
# 输出：8
# 解释：可能的序列为 "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"。
#  
# 
#  示例 2： 
# 
#  输入："AAABBC"
# 输出：188
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= tiles.length <= 7 
#  tiles 由大写英文字母组成 
#  
#  Related Topics 回溯算法 
#  👍 108 👎 0
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtracking():
            ans = 0
            for i in range(26):
                if tiles_map[i] > 0:
                    tiles_map[i] -= 1
                    ans += 1
                    ans += backtracking()
                    tiles_map[i] += 1
            return ans
        tiles_map = [0] * 26
        for i in tiles:
            tiles_map[ord(i) - ord('A')] += 1
        return backtracking()

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtracking():
            ans[0] += 1
            for i in range(26):
                if tiles_map[i] > 0:
                    tiles_map[i] -= 1
                    backtracking()
                    tiles_map[i] += 1
        tiles_map = [0] * 26
        for i in tiles:
            tiles_map[ord(i) - ord('A')] += 1
        ans = [-1]
        backtracking()
        return ans[0]

# leetcode submit region end(Prohibit modification and deletion)
tiles = "AAB"
print(Solution().numTilePossibilities(tiles))