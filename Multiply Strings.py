class ClassName(object):
	"""docstring for ClassName"""
	def mutil(self,num,ch):
		ret = 0
		di = ord(ch)-ord('0')
		for ch0 in num:
			ret*=10
			ret += (ord(ch0)-ord('0'))*di
		return ret
		
	def multiply(self, num1, num2):
		ret=0
		for ch in num2:
			ret*=10
			ret+=self.mutil(num1,ch)
		return ret			

ins = ClassName()

print ins.multiply('123','123')