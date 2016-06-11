struct SegmentTreeNode {
    SegmentTreeNode(Interval _interval): interval(_interval), left(NULL), right(NULL) {}
    SegmentTreeNode *left, *right;
    Interval interval;
};

void updateChild(SegmentTreeNode* root, bool checkLeftChild) {
    if (checkLeftChild) {
        if (root->left) {
            if (root->left->interval.end + 1 == root->interval.start) {
                //merge left to root
                root->interval.start = root->left->interval.start;
                SegmentTreeNode* oldLeft = root->left;
                root->left = root->left->left;
                free(oldLeft);
            }
        }
    } else {
        if (root->right) {
            if (root->right->interval.start == root->interval.end + 1) {
                root->interval.end = root->right->interval.end;
                SegmentTreeNode* oldRight = root->right;
                root->right = root->right->right;
                free(oldRight);
            }
        }
    }
}

struct SegmentTree {
    SegmentTree(): root(NULL) {}
    void insertNode(int val) {
        if (!root) {
            root = new SegmentTreeNode(Interval(val, val));
            return ;
        }
        SegmentTreeNode *current = root, *prev = NULL;
        while (current) {
            prev = current;
            if (current->interval.start <= val && val <= current->interval.end) {
                return ;
            } else if (current->interval.start == val + 1) {
                current->interval.start = val;
                //updated!
                updateChild(current, true);
                return ;
            } else if (current->interval.end == val - 1) {
                current->interval.end = val;
                //updated!
                updateChild(current, false);
                return ;
            } else if (current->interval.start > val + 1) {
                current = current->left;
            } else if (current->interval.end < val - 1) {
                current = current->right;
            }
        }
        if (!current) {
            if (prev->interval.start > val + 1) {
                prev->left = new SegmentTreeNode(Interval(val, val));
            } else {
                prev->right = new SegmentTreeNode(Interval(val, val));
            }
        }
    }

    vector<Interval> getNodes() {
        vector<Interval> answer;
        if (root) {
            SegmentTreeNode* current = root;
            queue<SegmentTreeNode*> myqueue;
            myqueue.push(current);
            while (!myqueue.empty()) {
                current = myqueue.front();
                myqueue.pop();
                answer.push_back(current->interval);
                if (current->left) {
                    myqueue.push(current->left);
                }
                if (current->right) {
                    myqueue.push(current->right);
                }
            }
        }
        return answer;
    }

    SegmentTreeNode *root;
};

class SummaryRanges {
public:
    void addNum(int val) {
        tree.insertNode(val);
    }
    vector<Interval> getIntervals() {
        return tree.getNodes();
    }
private:
    SegmentTree tree;
};
