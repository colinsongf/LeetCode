/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        TreeNode *parent = NULL;
        TreeNode *target = root;
        while (target && target->val != key)
        {
            parent = target;
            if (target->val >= key)
            {
                target = target->left;
            }
            else
            {
                target = target->right;
            }
        }
        if (!target)
        {
            return NULL;
        }
        TreeNode *right_left_most = target->right;
        if (!right_left_most)//no right subtree
        {
            if (!parent)
            {
                root = target->left;
            }
            else if (parent->val >= key)
            {
                parent->left = target->left;
            }
            else
            {
                parent->right = target->left;
            }
        }
        else//has right subtree
        {
            while (right_left_most->left)
            {
                right_left_most = right_left_most->left;
            }
            right_left_most->left = target->left;
            if (!parent)
            {
                root = target->right;
            }
            else if (parent->val >= key)
            {
                parent->left = target->right;
            }
            else
            {
                parent->right = target->right;
            }
        }
        delete target;
        return root;
    }
};
