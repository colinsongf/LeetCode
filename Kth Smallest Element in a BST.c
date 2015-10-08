/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

#define STACKSIZE 10000

struct TreeNode *stack[STACKSIZE];
int sp = -1;

#define PUSH_STACK(x) stack[++sp] = x
#define POP_STACK() sp--
#define TOP_STACK() stack[sp]
#define EMPTY_STACK() (sp == -1)

int kthSmallest(struct TreeNode *root,int k){
	int counter = 0;
	struct TreeNode *current = root;
	while (current || !EMPTY_STACK()){
		while (current) {
			PUSH_STACK(current);
			current = current->left;
		}
		current = TOP_STACK();
		counter++;
		if (counter == k)
			return current->val; 
		POP_STACK();
		current = current->right;
	}
	return -1;
}