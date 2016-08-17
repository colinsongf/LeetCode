class RandomizedSet {
public:
    /** Initialize your data structure here. */
    RandomizedSet() {
        
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        std::multiset<int>::iterator it = mymultiset.find(val);
        if (it == mymultiset.end())
        {
            mymultiset.insert(val);
            return true;
        }
        return false;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        std::multiset<int>::iterator it = mymultiset.find(val);
        if (it != mymultiset.end())
        {
            mymultiset.erase(it);
            return true;
        }
        return false;
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        std::srand(std::time(0));
        int select = std::rand() % mymultiset.size();
        int i = 0;
        int randout;
        std::multiset<int>::iterator it = mymultiset.begin();
        while (i <= select)
        {
            randout = *it;
            ++i;
            ++it;
        }
        return randout;
    }
private:
    std::multiset<int> mymultiset;
};


/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * bool param_1 = obj.insert(val);
 * bool param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
