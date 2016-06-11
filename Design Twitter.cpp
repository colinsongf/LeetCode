class User {
public:
    void postTweet(int tweetId, int timestamp) {
        tweets.emplace_back(tweetId, timestamp);
    }

    void follow(int userId) {
        followees.insert(userId);
    }
    void unfollow(int userId) {
        followees.erase(userId);
    }

    friend class Twitter;
private:
    unordered_set<int> followees;
    vector<pair<int, unsigned long> > tweets;
};

class Twitter {
public:
    /** Initialize your data structure here. */
    Twitter(): timestamp(0) {
    }
    
    /** Compose a new tweet. */
    void postTweet(int userId, int tweetId) {
        User *user = getUser(userId);
        if (!user) {
            user = new User();
            users[userId] = user;
        }
        user->postTweet(tweetId, timestamp++);
    }
    
    /** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
    vector<int> getNewsFeed(int userId) {
        vector<int> feeds;
        User *user = getUser(userId);
        if (!user) {
            return feeds;
        }
        unordered_map<int, vector<pair<int, unsigned long> >::reverse_iterator> mergeMap;
        for (unordered_set<int>::iterator it = user->followees.begin();it != user->followees.end(); ++it) {
            User *thatuser = getUser(*it);
            if (!thatuser->tweets.empty()) {
                mergeMap[*it] = thatuser->tweets.rbegin();
            }
        }
        if (!user->tweets.empty()) {
            mergeMap[userId] = user->tweets.rbegin();
        }
        //now merge
        int counter = 0;
        while (counter < 10 && !mergeMap.empty()) {
            int who = -1;
            int tweetId = -1;
            unsigned long maxTime = 0;
            unordered_map<int, vector<pair<int, unsigned long> >::reverse_iterator>::iterator it;
            for (it = mergeMap.begin();it != mergeMap.end(); ++it) {
                if (it->second->second >= maxTime) {
                    maxTime = it->second->second;
                    who = it->first;
                    tweetId = it->second->first;
                }
            }    
            feeds.push_back(tweetId);
            mergeMap[who] = mergeMap[who] + 1;
            if (mergeMap[who] == getUser(who)->tweets.rend()) {
                mergeMap.erase(who);
            }
            counter++;
        }
        return feeds;
    }
    
    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */
    void follow(int followerId, int followeeId) {
        User *user = getUser(followerId);
        if (!user) {
            user = new User();
            users[followerId] = user;
        }
        user->follow(followeeId);
    }
    
    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    void unfollow(int followerId, int followeeId) {
        User *user = getUser(followerId);
        if (user) {
            user->unfollow(followeeId);
        }
    }

    User* getUser(int userId) {
        unordered_map<int, User*>::iterator it = users.find(userId);
        return it == users.end()? NULL: it->second;
    }

private:
    unordered_map<int, User*> users;
    unsigned long timestamp;
};
