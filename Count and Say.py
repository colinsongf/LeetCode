class Solution:
	def countAndSay(self,n):
		if n==1:
			return '1'
		string=self.countAndSay(n-1)
		if not string:
			return string
		counter,prev = 1,string[0]
		answer=''
		for ch in string[1:]:
			if ch==prev:
				counter+=1
			else:
				answer+='%d%s' % (counter,prev)
				prev=ch
				counter =1
		answer+='%d%s' % (counter,prev)
		self.lasttime=answer
		return answer