from sortedcontainers import SortedList
from collections import defaultdict
from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(SortedList)
        self.freq = {"minute": 60, "hour": 3600, "day": 86400}

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].add(time)


    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        t = self.freq[freq]
        tweets = self.tweets[tweetName]
        ans = []
        for i in range(startTime, endTime + 1, t):
            index1 = tweets.bisect_left(i)
            index2 = tweets.bisect_left(min(i + t, endTime + 1))
            if index2 - index1 > 0:
                ans.append(index2 - index1)
        return ans



# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
# leetcode submit region end(Prohibit modification and deletion)
