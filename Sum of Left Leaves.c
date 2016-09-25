int sumOfLeftLeaves0(struct TreeNode* root, bool isLeftChild) {
    if (!root)
    {
        return 0;
    }
    if (!root->left && !root->right)
    {
        if (isLeftChild)
        {
            return root->val;
        }
        else
        {
            return 0;
        }
    }
    return sumOfLeftLeaves0(root->left, true) + sumOfLeftLeaves0(root->right, false);
}

int sumOfLeftLeaves(struct TreeNode* root) {
    return sumOfLeftLeaves0(root, false);
}
