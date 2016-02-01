class Item {
public:
    Item(string _vertex): vertex(_vertex), status(0) {}
    bool finished() {
        return status == 2;
    }
    string &getVertex() {
        return vertex;
    }
    void addStatus() {
        ++status;
    }
private:
    string vertex;
    int status;
};

void stringSplit(string input, char split, vector<Item*>& afterSplit) {
    int start = 0, end = 0;
    for (int i = 0;i < input.size(); ++i) {
        if (input[i] == split) {
            end = i;
            string substring = input.substr(start, end - start);
            Item *item = new Item(substring);
            afterSplit.push_back(item);
            start = i + 1;
        }
    }
    if (start < input.size()) {
        string substring = input.substr(start, input.size() - start);
        Item *item = new Item(substring);
        afterSplit.push_back(item);
    }
}

class Solution {
public:
    bool isValidSerialization(string preorder) {
        vector<Item*> input;
        stringSplit(preorder, ',', input);
        if (input.size() == 0) {
            return false;
        }
        if (input.size() == 1 && input[0]->getVertex() == "#") {
            return true;
        }
        stack<Item*> istack;
        vector<Item*>::iterator it = input.begin();
        istack.push(*it);
        ++it;
        for (;it != input.end(); ++it) {
            if (istack.empty()) {
                return false;
            }
            Item* top = istack.top();
            top->addStatus();
            if (top->finished()) {
                istack.pop();
                delete top;
            }
            if ((*it)->getVertex() != "#") {
                istack.push(*it);
            }
        }
        return istack.empty();
    }
};