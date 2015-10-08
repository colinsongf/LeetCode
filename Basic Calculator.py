def getToken(string):
	token=[]
	currentnumber=''
	for ch in string:
		if ch in '+-()':
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
	def calculate(self ,string):
		express = getToken(string)
		op_stack=[]
		number_stack=[]
		for exp in express:
			if exp == '(':
				op_stack.append(exp)
			elif exp == '+':
				while op_stack and op_stack[-1] == '-':
					op=op_stack.pop()
					num2=number_stack.pop()
					num1=number_stack.pop()
					number_stack.append(num1 - num2)
				op_stack.append(exp)
			elif exp == '-':
				while op_stack and op_stack[-1] == '-':
					op=op_stack.pop()
					num2=number_stack.pop()
					num1=number_stack.pop()
					number_stack.append(num1 - num2)
				op_stack.append(exp)
			elif exp == ')':
				while op_stack[-1] != '(':
					op = op_stack.pop()
					num2=number_stack.pop()
					num1=number_stack.pop()
					if op == '+':
						number_stack.append(num1 + num2)
					else:
						number_stack.append(num1 - num2)
				op_stack.pop()
			else:
				number_stack.append(int(exp))
		while op_stack:
			op = op_stack.pop()
			num2=number_stack.pop()
			num1=number_stack.pop()
			if op == '+':
				number_stack.append(num1 + num2)
			else:
				number_stack.append(num1 - num2)
		return number_stack[0]
