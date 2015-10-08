class Solution:
	def anagrams(self, strs):
		hashmap={}
		for string in strs:
			key=''.join(sorted(string))
			if key not in hashmap:
				hashmap[key]=[string]
			else:
				hashmap[key].append(string)
		anagram = []
		for key in hashmap:
			if len(hashmap[key])>1:
				anagram.extend(hashmap[key])
		return anagram