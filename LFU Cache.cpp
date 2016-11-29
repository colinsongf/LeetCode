struct Item
{
    Item(int _key, int _value): key(_key), value(_value), frequence(1), prev(NULL), next(NULL)
    {
    }
    int key;
    int value;
    int frequence;
    Item *prev;
    Item *next;
};

struct LinkedList
{
    LinkedList(): head(NULL), tail(NULL)
    {
    }

    void add_node(Item *newnode)
    {
        if (!head)
        {
            head = newnode;
            tail = newnode;
        }
        else
        {
            tail->next = newnode;
            newnode->prev = tail;
            tail = newnode;
        }
    }

    void rm_node(Item *targetnode)
    {
        Item *prev = targetnode->prev;
        Item *next = targetnode->next;
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

    int pop_node()
    {
        if (!head)
        {
            return -1;
        }
        Item *answernode = head;
        Item *next = head->next;
        head = next;
        if (next)
        {
            next->prev = NULL;
        }
        else
        {
            tail = next;
        }
        return answernode->key;
    }

    bool empty()
    {
        return head == NULL;
    }

private:
    Item *head;
    Item *tail;
};

class LFUCache {
public:
    LFUCache(int _capacity): capacity(_capacity)
    {
    }
    
    int get(int key)
    {
        map<int, Item*>::iterator it = node_mapper.find(key);
        if (it == node_mapper.end())
        {
            return -1;
        }
        Item *node = it->second;
        int value = node->value;
        int frequence = node->frequence;
        map<int, LinkedList*>::iterator lit = list_mapper.find(frequence);
        LinkedList *list = lit->second;
        list->rm_node(node);
        if (list->empty())
        {
            list_mapper.erase(lit);
            delete list;
        }
        
        lit = list_mapper.find(frequence + 1);
        if (lit == list_mapper.end())
        {
            list_mapper[frequence + 1] = new LinkedList();
        }
        node->prev = node->next = NULL;
        node->frequence += 1;
        list_mapper[frequence + 1]->add_node(node);
        return value;
    }
    
    void set(int key, int value)
    {
        if (!capacity)
        {
            return ;
        }
        map<int, Item*>::iterator it = node_mapper.find(key);
        if (it != node_mapper.end())
        {
            Item *node = it->second;
            node->value = value;

            int frequence = node->frequence;
            map<int, LinkedList*>::iterator lit = list_mapper.find(frequence);
            LinkedList *list = lit->second;
            list->rm_node(node);
            if (list->empty())
            {
                list_mapper.erase(lit);
                delete list;
            }

            lit = list_mapper.find(frequence + 1);
            if (lit == list_mapper.end())
            {
                list_mapper[frequence + 1] = new LinkedList();
            }
            node->prev = node->next = NULL;
            node->frequence += 1;
            list_mapper[frequence + 1]->add_node(node);
        }
        else
        {
            Item *node = new Item(key, value);
            if (node_mapper.size() == capacity)
            {
                map<int, LinkedList*>::iterator lit = list_mapper.begin();
                LinkedList *list = lit->second;
                int rmkey = list->pop_node();
                if (list->empty())
                {
                    list_mapper.erase(lit);
                    delete list;
                }
                it = node_mapper.find(rmkey);
                delete it->second;
                node_mapper.erase(rmkey);
            }
            if (list_mapper.find(1) == list_mapper.end())
            {
                list_mapper[1] = new LinkedList();
            }
            list_mapper[1]->add_node(node);
            node_mapper[key] = node;
        }
    }
private:
    int capacity;
    map<int, Item*> node_mapper;
    map<int, LinkedList*> list_mapper;
};
