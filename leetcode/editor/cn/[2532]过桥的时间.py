from typing import List
from heapq import *
# leetcode submit region begin(Prohibit modification and deletion)
class Worker:
    def __init__(self, index, *args):
        self.index = index
        self.left_to_right = args[0]
        self.pick_old = args[1]
        self.right_to_left = args[2]
        self.put_new = args[3]

    def __lt__(self, other):
        return (self.left_to_right + self.right_to_left > other.left_to_right + other.right_to_left) or (
                    self.left_to_right + self.right_to_left == other.left_to_right + other.right_to_left and self.index > other.index)

class Bridge:
    def __init__(self):
        self.worker = None
        self.leave_time = -1
        self.flag = -1 # 0表示进入新工厂，1表示从进入旧工厂

    def is_busy(self) -> bool:
        return self.worker is not None

    def add(self, t: int, worker: Worker, flag: int) -> None:
        self.leave_time = t
        self.worker = worker
        self.flag = flag

    def pop(self):
        assert self.worker is not None, "桥上并没有人"
        worker = self.worker
        self.worker = None
        self.flag = -1
        return worker

class Bank:
    def __init__(self):
        self.q = []

    def is_empty(self):
        return len(self.q) == 0

    def add_worker(self, worker: Worker) -> None:
        heappush(self.q, worker)

    def pop(self) -> Worker:
        return heappop(self.q)

class House:
    def __init__(self, num, delta):
        self.q = []
        self.boxes_num = num
        self.delta = delta

    def is_empty(self) -> bool:
        return len(self.q) == 0

    def first_leave_time(self) -> int:
        return self.q[0][0]

    def pop(self) -> Worker:
        return heappop(self.q)[1]

    def add(self, worker: Worker, t: int) -> None:
        self.boxes_num += self.delta
        heappush(self.q, (t, worker))


class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        bridge = Bridge()
        left_bank, right_bank = Bank(), Bank()
        new_house, old_house = House(0, 1), House(n, -1)
        # 对左岸进行初始化
        for i, args in enumerate(time):
            left_bank.add_worker(Worker(i, *args))
        cur_time = 0
        while new_house.boxes_num < n:
            # 如果桥处于忙碌，则跳过这段时间，同时将桥上的工人放入工厂
            if bridge.is_busy():
                # print(f"从 {cur_time} 到 {bridge.leave_time}：工人 {bridge.worker.index} 从{'左' if bridge.flag == 1 else '右'}岸过桥到达{'左' if bridge.flag == 0 else '右'}岸")
                cur_time = bridge.leave_time
                if bridge.flag == 0:
                    worker = bridge.pop()
                    # print(f"从 {cur_time} 到 {cur_time + worker.put_new}： 工人 {worker.index} 将箱子放入新仓库")
                    new_house.add(worker, cur_time + worker.put_new)
                else:
                    worker = bridge.pop()
                    # print(f"从 {cur_time} 到 {cur_time + worker.pick_old}：工人 {worker.index} 从旧仓库搬起一个箱子")
                    old_house.add(worker, cur_time + worker.pick_old)
            elif old_house.boxes_num == 0:
                # 只有right_bank为空 and old_house.box_num == 0才会进入，意味着左边不准进桥了，将时间跳到出旧房子时间
                cur_time = old_house.first_leave_time()


            # 跳过的时间中，可能有挑好box的工人回到右岸，放下box的工人回到左岸
            # 需要维护旧仓库box数量，新仓库box数量，左岸等待工人，右岸等待工人
            while not new_house.is_empty() and cur_time >= new_house.first_leave_time():
                left_bank.add_worker(new_house.pop())
            while not old_house.is_empty() and cur_time >= old_house.first_leave_time():
                right_bank.add_worker(old_house.pop())

            # 此时桥一定处于空闲，但是可能工人都在工厂里面，不在桥边，所以跳过一段时间，令部分工人回到桥边
            # 然后维护在这段时间中左右岸的信息和新旧仓库box的数量
            if left_bank.is_empty() and right_bank.is_empty():
                if new_house.is_empty():
                    cur_time = old_house.first_leave_time()
                elif old_house.is_empty():
                    cur_time = new_house.first_leave_time()
                else:
                    cur_time = min(new_house.first_leave_time(), old_house.first_leave_time())
                while not new_house.is_empty() and cur_time >= new_house.first_leave_time():
                    left_bank.add_worker(new_house.pop())
                while not old_house.is_empty() and cur_time >= old_house.first_leave_time():
                    right_bank.add_worker(old_house.pop())

            # 按照「规则」决定谁上桥，经过上面的处理，左岸或者右岸一定有工人
            if not right_bank.is_empty():
                worker = right_bank.pop()
                bridge.add(cur_time + worker.right_to_left, worker, 0)
            elif old_house.boxes_num > 0:
                worker = left_bank.pop()
                bridge.add(cur_time + worker.left_to_right, worker, 1)
        return bridge.leave_time

# leetcode submit region end(Prohibit modification and deletion)

class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        workL, workR, waitL, waitR, cur = [], [], [], [], 0
        for i, args in enumerate(time):
            heappush(waitL, Worker(i, *args))
        while n:
            while workL and workL[0][0] <= cur:
                heappush(waitL, heappop(workL)[1])
            while workR and workR[0][0] <= cur:
                heappush(waitR, heappop(workR)[1])
            if waitR:
                # 出堆，过桥，放入workL
                worker = heappop(waitR)
                cur += worker.right_to_left
                heappush(workL, (cur + worker.put_new, worker))
            elif waitL:
                # 出堆，过桥，放入workR
                worker = heappop(waitL)
                cur += worker.left_to_right
                heappush(workR, (cur + worker.pick_old, worker))
                n -= 1
            elif len(workL) == 0:
                cur = workR[0][0]
            elif len(workR) == 0:
                cur = workL[0][0]
            else:
                cur = min(workL[0][0], workR[0][0])
        while workR:
            t, worker = heappop(workR)
            cur = max(cur, t) + worker.right_to_left
        return cur


n = 1
k = 3
time = [[1,1,2,1],[1,1,3,1],[1,1,4,1]]


n = 3
k = 2
time = [[1,9,1,8],[10,10,10,10]]

print(Solution().findCrossingTime(n, k, time))