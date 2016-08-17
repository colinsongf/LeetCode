class RandomizedCollection {
public:
    /** Initialize your data structure here. */
    RandomizedCollection() {
        std::srand(std::time(0));
        length = 0;
    }
    
    /** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
    bool insert(int val) {
        multimap<int, unsigned int>::iterator it = posmap.find(val);
        ++length;
        if (it == posmap.end())
        {
            pair<int, unsigned int> item(val, 1);
            posmap.insert(item);
            return true;
        }
        else
        {
            it->second += 1;
        }
        return false;
    }
    
    /** Removes a value from the collection. Returns true if the collection contained the specified element. */
    bool remove(int val) {
        multimap<int, unsigned int>::iterator it = posmap.find(val);
        if (it != posmap.end())
        {
            it->second -= 1;
            if (!it->second)
            {
                posmap.erase(it);
            }
            --length;
            return true;
        }
        return false;
    }
    
    /** Get a random element from the collection. */
    int getRandom() {
        unsigned int i = 0;
        multimap<int, unsigned int>::iterator it = posmap.begin();
        unsigned int select = std::rand() % length;
        while (i < length)
        {
            if (i <= select && select < it->second + i)
            {
                return it->first;
            }
            else
            {
                i += it->second;
                ++it;
            }
        }
        return 0;
    }

private:
    multimap<int, unsigned int> posmap;
    unsigned int length;
};
