class Solution:
    # @param s, a string
    # @return an integer
	def numDecodings(self, string):
		if not string:
			return 0
		size=len(string)
		m=[0 for x in range(size+1)]
		m[0]=1
		m[1]=1 if string[0]!='0' else 0
		#print m
		for i in range(2,size+1):
			ch,prev=string[i-1],string[i-2]
			m[i]=0
			if ch!='0':
				m[i]+=m[i-1]
			if prev!='0' and int(prev)*10+int(ch)<=26:
				m[i]+=m[i-2]
		#print m
		return m[size]