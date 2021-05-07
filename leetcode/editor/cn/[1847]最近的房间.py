# 一个酒店里有 n 个房间，这些房间用二维整数数组 rooms 表示，其中 rooms[i] = [roomIdi, sizei] 表示有一个房间号为 roo
# mIdi 的房间且它的面积为 sizei 。每一个房间号 roomIdi 保证是 独一无二 的。 
# 
#  同时给你 k 个查询，用二维数组 queries 表示，其中 queries[j] = [preferredj, minSizej] 。第 j 个查询的答
# 案是满足如下条件的房间 id ： 
# 
#  
#  房间的面积 至少 为 minSizej ，且 
#  abs(id - preferredj) 的值 最小 ，其中 abs(x) 是 x 的绝对值。 
#  
# 
#  如果差的绝对值有 相等 的，选择 最小 的 id 。如果 没有满足条件的房间 ，答案为 -1 。 
# 
#  请你返回长度为 k 的数组 answer ，其中 answer[j] 为第 j 个查询的结果。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：rooms = [[2,2],[1,2],[3,2]], queries = [[3,1],[3,3],[5,2]]
# 输出：[3,-1,3]
# 解释：查询的答案如下：
# 查询 [3,1] ：房间 3 的面积为 2 ，大于等于 1 ，且号码是最接近 3 的，为 abs(3 - 3) = 0 ，所以答案为 3 。
# 查询 [3,3] ：没有房间的面积至少为 3 ，所以答案为 -1 。
# 查询 [5,2] ：房间 3 的面积为 2 ，大于等于 2 ，且号码是最接近 5 的，为 abs(3 - 5) = 2 ，所以答案为 3 。 
# 
#  示例 2： 
# 
#  
# 输入：rooms = [[1,4],[2,3],[3,5],[4,1],[5,2]], queries = [[2,3],[2,4],[2,5]]
# 输出：[2,1,3]
# 解释：查询的答案如下：
# 查询 [2,3] ：房间 2 的面积为 3 ，大于等于 3 ，且号码是最接近的，为 abs(2 - 2) = 0 ，所以答案为 2 。
# 查询 [2,4] ：房间 1 和 3 的面积都至少为 4 ，答案为 1 因为它房间编号更小。
# 查询 [2,5] ：房间 3 是唯一面积大于等于 5 的，所以答案为 3 。 
# 
#  
# 
#  提示： 
# 
#  
#  n == rooms.length 
#  1 <= n <= 105 
#  k == queries.length 
#  1 <= k <= 104 
#  1 <= roomIdi, preferredj <= 107 
#  1 <= sizei, minSizej <= 107 
#  
#  Related Topics 排序 二分查找 
#  👍 11 👎 0

from typing import List
import bisect
class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        n, m = len(rooms), len(queries)
        rooms.sort(key=lambda x: x[1], reverse=True)
        queries = [[idx, q_id, q_size] for idx, (q_id, q_size) in enumerate(queries)]
        queries.sort(key=lambda x: x[2], reverse=True)
        cur = 0
        memo = [] # 记录符合面积要求的房间id
        ans = [-1] * m
        for idx, q_id, q_size in queries:
            while cur < n and rooms[cur][1] >= q_size:
                bisect.insort_left(memo, rooms[cur][0])
                cur += 1
            if memo:
                t = bisect.bisect_left(memo, q_id)
                ans[idx] = memo[t-1] if t == len(memo) or (t > 0 and abs(memo[t] - q_id) >= abs(memo[t - 1] - q_id)) else memo[t]
        return ans

# leetcode submit region begin(Prohibit modification and deletion)
class Block:
    def __init__(self):
        # block 中最小的房间 size
        self.min_size = float("inf")
        # block 中的房间 id
        self.ids = list()
        # 原始数据
        self.origin = list()

    # 加入一个房间
    def insert(self, idx: int, size: int):
        self.origin.append((idx, size))
        self.ids.append(idx)
        self.min_size = min(self.min_size, size)

    # 添加完所有房间后，将房间 id 排序，便于后续二分
    def sort(self):
        self.ids.sort()

    # 封装一下二分函数，找最小的大于等于它的
    def geq(self, preferred: int) -> int:
        _ids = self.ids

        it = bisect.bisect_left(_ids, preferred)
        return -1 if it == len(_ids) else _ids[it]

    # 封装一下二分函数，找最大的严格小于它的
    def lt(self, preferred: int) -> int:
        _ids = self.ids

        it = bisect.bisect_right(_ids, preferred)
        return -1 if it == 0 else _ids[it - 1]


class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        BLOCK_SIZE = 300 # 每个BLOCK放300个房间

        # 按照 size 升序排序
        rooms.sort(key=lambda room: room[1])

        # 每 BLOCK_SIZE 个房间放进一个 block
        blocks = list() # 存放BLOCK
        for i, (roomid, size) in enumerate(rooms):
            if i % BLOCK_SIZE == 0:
                blocks.append(Block())
            blocks[-1].insert(roomid, size)

        for block in blocks:
            block.sort()

        ans = [-1] * len(queries)
        for i, (preferred, minsize) in enumerate(queries):
            mindiff = float("inf")

            # 越往后的block存放的房间面积越大
            for block in blocks[::-1]:
                rooms = block.origin
                # block 中最小 size 的房间大于等于 minsize，整个 block 都可以选择
                if rooms[0][1] >= minsize:
                    c1 = block.geq(preferred)
                    if c1 != -1 and c1 - preferred < mindiff:
                        mindiff = c1 - preferred
                        ans[i] = c1

                    c2 = block.lt(preferred)
                    if c2 != -1 and preferred - c2 <= mindiff:
                        mindiff = preferred - c2
                        ans[i] = c2
                else:
                    # 只有部分都可以选择，遍历一下所有的房间
                    for room in rooms[::-1]:
                        if room[1] >= minsize:
                            diff = abs(room[0] - preferred)
                            if diff < mindiff or (diff == mindiff and room[0] < ans[i]):
                                mindiff = diff
                                ans[i] = room[0]
                        else:
                            break
                    # 再之前的 block 一定都严格小于 minsize，可以直接退出
                    break

        return ans

# leetcode submit region end(Prohibit modification and deletion)
rooms = [[2,2],[1,2],[3,2]];queries = [[3,1],[3,3],[5,2]]
rooms = [[1,4],[2,3],[3,5],[4,1],[5,2]];queries = [[2,3],[2,4],[2,5]]
rooms = [[23,22],[6,20],[15,6],[22,19],[2,10],[21,4],[10,18],[16,1],[12,7],[5,22]];queries=[[12,5],[15,15],[21,6],[15,1],[23,4],[15,11],[1,24],[3,19],[25,8],[18,6]]
print(Solution().closestRoom(rooms, queries))
