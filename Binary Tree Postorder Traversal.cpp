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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> answer;
        if (!root)
            return answer;
        stack<TreeNode *> mystack;
        TreeNode* current = root;
        while (current || !mystack.empty()) {
            while (current) {
                mystack.push(current);
                current = current->left;
            }
            current = mystack.top();
            //mystack.pop();
            if (!current) {
                mystack.pop();
                current = mystack.top();
                mystack.pop();
                answer.push_back(current->val);
                current = NULL;
            }
            else if (current->right) {
                mystack.push(NULL);
                current = current->right;  
            }else {
                answer.push_back(current->val);
                mystack.pop();
                current = NULL;
            }
        }
        return answer;
    }
};