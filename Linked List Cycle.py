class Solution(object):
	def hasCycle(self, head):
		if not head:
			return False
		ret = False
		firstsp,secondsp=head.next,head
		if not firstsp:
			return ret
		secondsp=secondsp.next
		if not secondsp:
			return ret
		secondsp=secondsp.next
		if not secondsp:
			return ret
		while firstsp and secondsp:
			if firstsp==secondsp:
				ret=True
				break
			firstsp=firstsp.next
			secondsp=secondsp.next
			if not secondsp:
				break
			secondsp=secondsp.next
		return ret