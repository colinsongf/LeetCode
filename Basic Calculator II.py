def getToken(string):
	token=[]
	currentnumber=''
	for ch in string:
		if ch in '+-*/()':
			if currentnumber:
				token.append(currentnumber)
			currentnumber=''
			token.append(ch)
		elif ch == ' ':
			if currentnumber:
				token.append(currentnumber)
			currentnumber=''
			continue
		else:
			currentnumber+=ch
	if currentnumber:
		token.append(currentnumber)
	return token

class Solution:
	def calc(self ,n1,n2,op):
		if op == '+':
			return n1 + n2
		elif op == '-':
			return n1 - n2
		elif op == '*':
			return n1 * n2
		else:
			return n1 / n2
	def calculate(self ,string):
		express = getToken(string)
		op_stack=[]
		number_stack=[]
		for ch in express:
			if ch in '+-':
				while op_stack:
					op = op_stack.pop()
					number2 = number_stack.pop()
					number1 = number_stack.pop()
					number = self.calc(number1,number2,op)
					number_stack.append(number)
				op_stack.append(ch)
			elif ch in '*/':
				while op_stack and op_stack[-1] not in '+-':
					op = op_stack.pop()
					number2 = number_stack.pop()
					number1 = number_stack.pop()
					number = self.calc(number1,number2,op)
					number_stack.append(number)
				op_stack.append(ch)
			else:#number
				number_stack.append(int(ch))
		while op_stack:
			op = op_stack.pop()
			number2 = number_stack.pop()
			number1 = number_stack.pop()
			number = self.calc(number1,number2,op)
			number_stack.append(number)
		return number_stack[0]