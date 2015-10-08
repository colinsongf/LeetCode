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
    vector<vector<int> > levelOrder(TreeNode* root) {
        vector<vector<int> > answer;
        if (!root)
            return answer;
        vector<int> subanswer0;
        subanswer0.push_back(root->val);
        answer.push_back(subanswer0);
        queue<struct TreeNode *> q1,q2;
        struct TreeNode *current;
        q1.push(root);
        while (!q1.empty())
        {
            current = q1.front();
            q1.pop();
            if (current->left)
                q2.push(current->left);
            if (current->right)
                q2.push(current->right);
            if (q1.empty())
            {
                vector<int> subanswer;
                while (!q2.empty())
                {
                    current = q2.front();
                    q2.pop();
                    subanswer.push_back(current->val);
                    q1.push(current);
                }
                if (!subanswer.empty())
                    answer.push_back(subanswer);
            }
        }
        return answer;
    }
};