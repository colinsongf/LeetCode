struct TreeNode* invertTree(struct TreeNode* root) {
    if(!root)
        return NULL;
    struct TreeNode *left=root->left;
    root->left=invertTree(root->right);
    root->right=invertTree(left);
    return root;
}