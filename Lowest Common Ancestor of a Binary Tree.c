/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct ListNodeItem {
	struct TreeNode *treenode;
	struct ListNodeItem *next;
};

struct ListNodeItem *createListNodeItem(struct TreeNode *root){
	struct ListNodeItem *list = malloc(sizeof(struct ListNodeItem));
	if (!list)
		exit(1);
	list->treenode = root;
	list->next = NULL;
	return list;
}

struct ListNodeItem *getList(struct TreeNode* root, struct TreeNode* p){
	struct ListNodeItem *leftList,*rightList,*current;
	if (!p || !root)
		return NULL;
	if (root == p)
		return createListNodeItem(p);
	else if(!root->left && !root->right)
		return NULL;
	leftList = getList(root->left,p);
	rightList = getList(root->right,p);
	if (leftList){
		current = createListNodeItem(root);
		current->next = leftList;
		return current;
	}
	else if (rightList){
		current = createListNodeItem(root);
		current->next = rightList;
		return current;
	}
	else
		return NULL;
}

struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
	if (!root || !p || !q)
		return NULL;
	struct TreeNode *lcs = NULL;
	struct ListNodeItem *head1 = getList(root,p);
	struct ListNodeItem *head2 = getList(root,q);
	//disp(head1);
	//disp(head2);
	while (head1 && head2 && head1->treenode == head2->treenode){
		//printf("%d,%d\n",head1->treenode->val,head2->treenode->val );
		lcs = head1->treenode;
		head1 = head1->next;
		head2 = head2->next;
	}
	return lcs;
}