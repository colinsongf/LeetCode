class Solution:
    def sqrt(self, x):
        array=range(x+1)
        i,j=0,x+1
        while i<j:
            mid = (i+j)/2
            pivot=array[mid]
            if pivot**2 == x:
                return pivot
            elif pivot**2 > x:
                j = mid
            else:
                i = mid+1
        return array[i-1]
ins=Solution()
for i in range(10):
    print ins.sqrt(i)