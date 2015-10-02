class Point(object):
	"""docstring for Point"""
	def __init__(self, a=0,b=0):
		self.x=a
		self.y=b

class Solution:
	def maxPoints(self, points):
		hashmap={}
		samemap={}
		size=len(points)
		if not size:
			return 0
		for i in range(size-1):
			for j in range(i+1,size):
				a1,b1=points[i].x,points[i].y
				a2,b2=points[j].x,points[j].y
				if a1==a2 and b1==b2:
					continue
				key=(b2-b1,a1-a2,b2*a1-a2*b1)
				if key not in hashmap:
					hashmap[key]=0
		for point in points:
			if (point.x,point.y) in samemap:
				samemap[(point.x,point.y)]+=1
			else:
				samemap[(point.x,point.y)]=1
			for key in hashmap:
				if point.x*key[0]+point.y*key[1]==key[2]:
					hashmap[key]+=1
		maxsum=0
		for i in hashmap.values()+samemap.values():
			maxsum=max(maxsum,i)
		return maxsum

ins=Solution()
points=[Point(0,0),Point(0,0)]#[Point(84,250),Point(0,0),Point(1,0),Point(0,-70),Point(0,-70),Point(1,-1),Point(21,10),Point(42,90),Point(-42,-230)]
print ins.maxPoints(points)