struct ListNode *mergeKLists(struct ListNode **lists,int listsSize){
	struct ListNode *current = NULL,*prev = NULL,*list = NULL;
	int i,select;
	if (!listsSize)
		return list;
	if (listsSize == 1)
		return lists[0];
	struct ListNode *leftList = mergeKLists(lists, listsSize/2);
	struct ListNode *rightList = mergeKLists(lists + listsSize/2,listsSize - listsSize/2);
	while (leftList && rightList) {
		current = leftList->val <= rightList->val ? leftList : rightList;
		if (!list) 
			list = current;
		else
			prev->next = current;
		if (leftList->val <= rightList->val)
			leftList = leftList->next;
		else
			rightList = rightList->next;
		prev = current;
	}
	if (leftList) {
		if (!list)
			list = leftList;
		else
			prev->next = leftList;	
	}
	if (rightList) {
		if (!list)
			list = rightList;
		else
			prev->next = rightList;	
	}
	return list;
}