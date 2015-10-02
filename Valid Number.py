class Solution:
	def isNumber(self, string):
		string=string.strip()
		if not string:
			return False
		if 'e' in string:
			split=string.index('e')
			prefixstring=string[:split]
			suffixstring=string[split+1:]
			if not prefixstring or not suffixstring:
				return False
			if prefixstring[0]=='-' or prefixstring[0]=='+':
				prefixstring=prefixstring[1:]
			if suffixstring[0]=='-' or suffixstring[0]=='+':
				suffixstring=suffixstring[1:]
			if not prefixstring or not suffixstring or prefixstring=='.':
				return False
			dot=0
			for ch in prefixstring:
				if ch not in '0123456789':
					if ch=='.' and dot==0:
						dot+=1
					else:
						return False
			for ch in suffixstring:
				if ch not in '0123456789':
					return False
			return True
		else:
			if string[0]=='-' or string[0]=='+':
				string=string[1:]
			size=len(string)
			if size==0 or (size==1 and string[0]=='.'):
				return False
			dot=0
			for ch in string:
				if ch not in '0123456789':
					if ch=='.' and dot==0:
						dot+=1
					else:
						return False
			return True

ins=Solution()
print ins.isNumber('4e+')