import heapq
class Twitter:

    def __init__(self):
        self.follower = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time_stamp = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((-self.time_stamp, tweetId))
        self.time_stamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId in self.tweets:
            merged_tweets = self.tweets[userId].copy()
        else:
            merged_tweets = []
        for user in self.follower[userId]:
            if user not in self.tweets:
                continue
            merged_tweets.extend(self.tweets[user])

        heapq.heapify(merged_tweets)
        tweets_10 = []
        for i in range(min(10, len(merged_tweets))):
            _, tweetId = heapq.heappop(merged_tweets)
            tweets_10.append(tweetId)

        return tweets_10

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower[followerId]:
            self.follower[followerId].remove(followeeId)
