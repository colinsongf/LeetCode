class Solution:
	def letterCombinations(self,digits):
		hashmap={'0':'','1':'','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
		size=len(digits)
		step=0
		answer=['' for x in range(size)]
		record=[-1 for x in range(size)]
		dicts=[]
		while step>=0:
			dig=digits[step]
			record[step]+=1
			if record[step]>=len(hashmap[dig]):
				step-=1
			elif step==size-1:
				sel=hashmap[dig][record[step]]
				answer[step]=sel
				dicts.append(''.join(answer))
			else:
				sel=hashmap[dig][record[step]]
				answer[step]=sel
				step+=1
				record[step]=-1
		return dicts

ins=Solution()

di=ins.letter('486')

for d in di:
	print d
