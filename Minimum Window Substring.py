class Solution:
	def condition(self,dict,needdict):
		for key in dict:
			if dict[key]<needdict[key]:
				return False
		return True
	def minWindow(self, string, T):
		record,need={},{}
		for ch in T:
			if ch not in need:
				need[ch],record[ch]=1,0
			else:
				need[ch]+=1
		size=len(string)
		head=rear=0
		minw,minwindow=size+1,''
		while rear<size:
			ch=string[rear]
			if ch in record:
				record[ch]+=1
				if self.condition(record,need):
					while (string[head] not in record) or record[string[head]]-1>=need[string[head]]:
						if string[head] in record:
							record[string[head]]-=1
						head+=1
					if rear-head+1<minw:
						minw=rear-head+1
						minwindow=string[head:rear+1]
			rear+=1
		return minwindow

ins=Solution()
print ins.minWindow("aa","aa")