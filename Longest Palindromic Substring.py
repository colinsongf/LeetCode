class Solution:
	def longestPalindrome_low(self, string):
		strArray=[ch for ch in string]
		rstrArray=[ch for ch in reversed(string)]
		diff=[]
		size=len(strArray)
		m=[[0 for y in range(size)] for x in range(size)]
		m[0][0]=1 if strArray[0]==rstrArray[0] else 0
		maxvalue=1 if strArray[0]==rstrArray[0] else 0
		for i in range(1,size):
			for j in range(1,size):
				if strArray[i]==rstrArray[j]:
					m[i][j]=m[i-1][j-1]+1
					if m[i][j] > maxvalue:
						maxvalue = m[i][j]
				else:
					m[i][j]=0
		return maxvalue
	def testPalindrome(self, string, pos1,pos2,size):
		i,j=pos1,pos2
		counter=0
		while i>=0 and j<size and string[i]==string[j]:
			if i==j:
				counter+=1
			else:
				counter+=2
			i-=1
			j+=1
		return counter
	def longestPalindrome(self, string):
		size=len(string)
		maxlength=1
		position=(0,0)
		for i in range(size-1):
			counter=self.testPalindrome(string,i,i,size)
			if counter>maxlength:
				maxlength=counter
				position=(i,i)
			counter=self.testPalindrome(string,i,i+1,size)
			if counter>maxlength:
				maxlength=counter
				position=(i,i+1)
		if position[0]==position[1]:
			return string[position[0]-maxlength/2:position[1]+maxlength/2+1]
		else:
			return string[position[0]-maxlength/2+1:position[0]+1]+string[position[1]:position[1]+maxlength/2]
ins=Solution()
#print ins.longestPalindrome_low('miycvxmqggnmmcwlmizfojwrurwhwygwfykyefxbgveixykdebenzitqnciigfjgrzzbtgeazyrbiirmejhdwcgjzwqolrturjlqpsgunuqerqjevbheblmbvgxyedxshswsokbhzapfuojgyfhctlaifrisgzqlczageirnukgnmnbwogknyyuynwsuwbumdmoqwxprykmazghcpmkdcjduepjmjdxrhvixxbfvhybjdpvwjbarmbqypsylgtzyuiqkexgvirzylydrhrmuwpmfkvqllqvekyojoacvyrzjevaupypfrdguhukzuqojolvycgpjaendfetkgtojepelhcltorueawwjpltehbbjrvznxhahtuaeuairvuklctuhcyzomwrrznrcqmovanxmiyilefybkbveesrxkmqrqkowyrimuejqtikcjfhizsmumajbqglxrvevexnleflocxoqgoyrzgqflwiknntdcykuvdcpzlakljidclhkllftxpinpvbngtexngdtntunzgahuvfnqjedcafzouopiixw')

print ins.longestPalindrome('bb')