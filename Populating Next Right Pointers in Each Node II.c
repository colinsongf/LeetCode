/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  struct TreeLinkNode *left, *right, *next;
 * };
 *
 */
void connect(struct TreeLinkNode *root) {
    if (!root)
        return ;
    root->next = NULL;
    struct TreeLinkNode *head = root;
    struct TreeLinkNode *current, *newhead, *prev;
	while (head){
		current = head;
		newhead = NULL;
		while (current){
			if (current->left){
				newhead = current->left;
				break;
			}
			else if (current->right){
				newhead = current->right;
				break;
			}
			current = current->next;
		}
		head = prev = newhead;
		while (current){
			if (current->left && current->left != prev){
				prev->next = current->left;
				prev = prev->next;
			}
			if (current->right && current->right != prev){
				prev->next = current->right;
				prev = prev->next;
			}
			current = current->next;
		}
		if (prev)
			prev->next = NULL;
	}
}
