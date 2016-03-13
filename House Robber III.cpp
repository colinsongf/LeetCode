class Solution {
public:
    int getMax(initializer_list<int> nums) {
        auto it = nums.begin();
        int max = *it++;
        for (;it != nums.end(); ++it) {
            if (*it > max) {
                max = *it;
            }
        }
        return max;
    }

    pair<int, int> getTreeMaxPath(TreeNode* root) {
        if (!root) {
            return {0, 0};
        }
        pair<int, int> leftPair = getTreeMaxPath(root->left);
        pair<int, int> rightPair = getTreeMaxPath(root->right);
        int useroot = leftPair.second + rightPair.second + root->val;
        int nouseroot = getMax({leftPair.first + rightPair.first, leftPair.first + rightPair.second, leftPair.second + rightPair.first, leftPair.second + rightPair.second});
        return {useroot, nouseroot};
    }

    int rob(TreeNode* root) {
        if (!root) {
            return 0;
        }
        pair<int, int> answerPair = getTreeMaxPath(root);
        return getMax({answerPair.first, answerPair.second});
    }
};