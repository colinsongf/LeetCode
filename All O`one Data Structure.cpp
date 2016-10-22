struct TwoWayListNode {
    TwoWayListNode(int _count): prev(NULL), next(NULL), count(_count)
    {
    }

    void addMember(const string& member)
    {
        members.insert(member);
    }

    void rmMember(const string& member)
    {
        set<string>::iterator it = members.find(member);
        if (it != members.end())
        {
            members.erase(it);
        }
    }

    bool hasMember() const
    {
        return members.empty() == false;
    }

    string getOneMember() const
    {
        set<string>::iterator it = members.begin();
        return *it;
    }

    const int count;
    set<string> members;
    TwoWayListNode* prev;
    TwoWayListNode* next;
};

struct TwoWayList {
    TwoWayList(): head(NULL), tail(NULL)
    {
    }

    void addNodeInHead(TwoWayListNode* twln)
    {
        if (head)
        {
            head->prev = twln;
        }
        twln->next = head;
        head = twln;
        if (!tail)
        {
            tail = twln;
        }
    }

    void addNodeInMiddle(TwoWayListNode* twln)
    {

    }

    void addNodeBeforeYou(TwoWayListNode* target, TwoWayListNode* oldnode)
    {
        TwoWayListNode* prev = oldnode->prev;
        //prev => target => oldnode
        target->prev = prev;
        target->next = oldnode;
        oldnode->prev = target;
        if (prev)
        {
            prev->next = target;
        }
        else
        {
            head = target;
        }
    }

    void addNodeAfterYou(TwoWayListNode* target, TwoWayListNode* oldnode)
    {
        TwoWayListNode* next = oldnode->next;
        //oldnode => target => next
        target->prev = oldnode;
        target->next = next;
        oldnode->next = target;
        if (next)
        {
            next->prev = target;
        }
        else
        {
            tail = target;
        }
    }

    void deleteNode(TwoWayListNode* target)
    {
        TwoWayListNode* prev = target->prev;
        TwoWayListNode* next = target->next;
        if (prev)
        {
            prev->next = next;
        }
        else
        {
            head = next;
        }
        if (next)
        {
            next->prev = prev;
        }
        else
        {
            tail = prev;
        }
    }

    void incKey(const string& key, int oldvalue)
    {
        if (indexmap.find(oldvalue + 1) == indexmap.end())
        {
            indexmap[oldvalue + 1] = new TwoWayListNode(oldvalue + 1);
            TwoWayListNode* newnode = indexmap[oldvalue + 1];
            newnode->addMember(key);
            if (oldvalue)
            {
                TwoWayListNode* oldnode = indexmap[oldvalue];
                addNodeAfterYou(newnode, oldnode);
            }
            else
            {
                addNodeInHead(newnode);
            }
        }
        else
        {
            TwoWayListNode* newnode = indexmap[oldvalue + 1];
            newnode->addMember(key);
        }

        if (oldvalue)
        {
            TwoWayListNode* oldnode = indexmap[oldvalue];
            oldnode->rmMember(key);
            if (!oldnode->hasMember())
            {
                deleteNode(oldnode);
                indexmap.erase(oldvalue);
            }
        }
    }

    void decKey(const string& key, int oldvalue)
    {
        TwoWayListNode* oldnode = indexmap[oldvalue];
        oldnode->rmMember(key);

        if (oldvalue > 1)
        {
            if (indexmap.find(oldvalue - 1) == indexmap.end())
            {
                indexmap[oldvalue - 1] = new TwoWayListNode(oldvalue - 1);
                TwoWayListNode* newnode = indexmap[oldvalue - 1];
                newnode->addMember(key);
    
                addNodeBeforeYou(newnode, oldnode);
            }
            else
            {
                TwoWayListNode* newnode = indexmap[oldvalue - 1];
                newnode->addMember(key);
            }
        }

        if (!oldnode->hasMember())
        {
            deleteNode(oldnode);
            indexmap.erase(oldvalue);
        }

    }

    string getOneHeadStr() const
    {
        if (!head)
        {
            return "";
        }
        return head->getOneMember();
    }

    string getOneTailStr() const
    {
        if (!tail)
        {
            return "";
        }
        return tail->getOneMember();
    }

    TwoWayListNode* head;
    TwoWayListNode* tail;
    map<int, TwoWayListNode*> indexmap;
};

class AllOne {
public:
    /** Initialize your data structure here. */
    AllOne() {
    }
    
    /** Inserts a new key <Key> with value 1. Or increments an existing key by 1. */
    void inc(string key) {
        map<string, int>::iterator it = countmap.find(key);
        if (it == countmap.end())
        {
            //insert a new key
            countmap[key] = 1;
            dlist.incKey(key, 0);
        }
        else
        {
            //inc a old key
            int oldvalue = countmap[key];
            int newvalue = oldvalue + 1;
            countmap[key] = newvalue;
            dlist.incKey(key, oldvalue);
        }
    }
    
    /** Decrements an existing key by 1. If Key's value is 1, remove it from the data structure. */
    void dec(string key) {
        map<string, int>::iterator it = countmap.find(key);
        if (it != countmap.end())
        {
            int oldvalue = countmap[key];
            int newvalue = oldvalue - 1;
            countmap[key] = newvalue;
            if (!newvalue)
            {
                //need delete node
                countmap.erase(it);
            }
            dlist.decKey(key, oldvalue);
        }
    }
    
    /** Returns one of the keys with maximal value. */
    string getMaxKey() {
        return dlist.getOneTailStr();
    }
    
    /** Returns one of the keys with Minimal value. */
    string getMinKey() {
        return dlist.getOneHeadStr();
    }

private:
    map<string, int> countmap;
    TwoWayList dlist;
};
//因为每个key值变化不是+1就是-1，故每次值变化就进行类似插入排序的操作就很适合，时间基本上是O(1)
