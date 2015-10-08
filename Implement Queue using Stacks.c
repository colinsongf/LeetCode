struct StackItem {
	int vertex;
	struct StackItem *next;
};

typedef struct StackItem StackItem;

struct Stack {
	int size;
	struct StackItem *head;
};

typedef struct Stack Stack;

Stack *createStack(void){
	Stack *stack = malloc(sizeof(Stack));
	if (!stack)
		exit(1);
	stack->size = 0;
	stack->head = NULL;
	return stack;
}

void push(Stack *stack ,int vertex){
	StackItem *item = malloc(sizeof(Stack));
	if (!item)
		exit(1);
	item->vertex = vertex;
	item->next = stack->head;
	stack->head = item;
	stack->size++;
}

void pop(Stack *stack){
	if (!stack->head)
		return ;
	StackItem *item = stack->head;
	stack->head = stack->head->next;
	stack->size--;
	free(item);
}

int peek(Stack *stack){
	return stack->head->vertex;
}

typedef struct Queue{
	Stack *stack1;
	Stack *stack2;
} Queue;

/* Create a queue */
void queueCreate(Queue *queue, int maxSize) {
	if (!queue)
		return ;
	queue->stack1 = createStack();
	queue->stack2 = createStack();
}

/* Push element x to the back of queue */
void queuePush(Queue *queue, int element) {
   push(queue->stack1,element);	
}

/* Removes the element from front of queue */
void queuePop(Queue *queue) {
	if (queue->stack2->size == 0)
		while (queue->stack1->size != 0){
			push(queue->stack2,peek(queue->stack1));
			pop(queue->stack1);
		}
	pop(queue->stack2);
}

/* Get the front element */
int queuePeek(Queue *queue) {
	if (queue->stack2->size == 0)
		while (queue->stack1->size != 0){
			push(queue->stack2,peek(queue->stack1));
			pop(queue->stack1);
		}
	return peek(queue->stack2);
}

/* Return whether the queue is empty */
bool queueEmpty(Queue *queue) {
	return (queue->stack1->size == 0) && (queue->stack2->size == 0); 
}

/* Destroy the queue */
void queueDestroy(Queue *queue) {
	while (queue->stack1->size != 0)
		pop(queue->stack1);		
	free(queue->stack1);
	while (queue->stack2->size != 0)
		pop(queue->stack2);
	free(queue->stack2);
}