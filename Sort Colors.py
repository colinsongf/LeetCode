class Solution(object):
	def sortColors(self, array):
		hashmap={}.fromkeys(range(3),0)
		for num in array:
			hashmap[num]+=1
		sp = 0
		while hashmap[0]:
			array[sp]=0
			sp+=1
			hashmap[0]-=1
		while hashmap[1]:
			array[sp]=1
			sp+=1
			hashmap[1]-=1
		while hashmap[2]:
			array[sp]=2
			sp+=1
			hashmap[2]-=1