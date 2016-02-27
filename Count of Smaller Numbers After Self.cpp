struct _TreeNode {
    _TreeNode(int _val):val(_val) {}
    int val;
    int counter = 1;
    int leftCounter = 0;
    _TreeNode* left = nullptr;
    _TreeNode* right = nullptr;
};

class BinaryTree {
public:
    BinaryTree() = default;

    int insertToTree(int val) {
        int smallthanme = 0;
        if (!root) {
            root = new _TreeNode(val);
            return smallthanme;
        }
        _TreeNode* current = root;
        while (current) {
            if (current->val > val) {
                current->leftCounter++;
                if (current->left) {
                    current = current->left;
                } else {
                    current->left = new _TreeNode(val);
                    break;
                }
            } else if (current->val < val) {
                smallthanme += current->leftCounter + current->counter;
                if (current->right) {
                    current = current->right;
                } else {
                    current->right = new _TreeNode(val);
                    break;
                }
            } else {//equal
                smallthanme += current->leftCounter;
                current->counter++;
                break;
            }
        }
        return smallthanme;
    }

private:
    _TreeNode *root = nullptr;
};

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        vector<int> answer;
        if (!nums.size()) {
            return answer;
        }
        BinaryTree tree;
        for (auto it = nums.rbegin();it != nums.rend(); ++it) {
            int counter = tree.insertToTree(*it);
            answer.push_back(counter);
        }
        reverse(answer.begin(), answer.end());
        return answer;
    }
};