class MinStack:
	# @param x, an integer
	# @return an integer
	def __init__(self):
		self.stack=[]
		self.minvaluestack=[]
	def push(self, x):
		if not self.minvaluestack:
			self.minvaluestack.append(x)
		elif self.minvaluestack[0] >= x:
			self.minvaluestack.append(x)
		self.stack.push(x)
		return x
	# @return nothing
	def pop(self):
		if not self.stack:
			return
		if self.stack.pop() == self.minvaluestack[0]:
			self.minvaluestack.pop()
	# @return an integer
	def top(self):
		return self.stack[-1]
	# @return an integer
	def getMin(self):
		return self.minvaluestack[-1]

ins = MinStack()
print ins.x