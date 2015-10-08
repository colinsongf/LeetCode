/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int countNodes(struct TreeNode* root) {
    if (!root) return 0;
    return countNodes2(root, 0);
}

int getLeftHeight(struct TreeNode* root) {
    int h = 0;
    while (root) { root = root->left; h++; }
    return h;
}

int getRightHeight(struct TreeNode* root) {
    int h = 0;
    while (root) { root = root->right; h++; }
    return h;
}

int countNodes2(struct TreeNode* root, int curSum) {
    int lh = getLeftHeight(root);
    int rh = getRightHeight(root);

    if (lh == rh)
        return curSum + pow(2, lh) - 1;

    if (getRightHeight(root->left) + 1 == lh)
        return countNodes2(root->right, curSum + pow(2, lh - 1));
    else
        return countNodes2(root->left, curSum + pow(2, rh - 1));
}