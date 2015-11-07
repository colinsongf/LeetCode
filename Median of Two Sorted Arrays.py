class Solution:
    def findMedianSortedArrays(self, array1,array2):
        size1,size2=len(array1),len(array2)
        even = False if (size1+size2)&0x1 else True
        half=(size1+size2)>>1
        if even:
            half-=1
        counter=0
        while array1 and array2 and counter<half:
            if array1[0] < array2[0]:
                array1.pop(0)
            else:
                array2.pop(0)
            counter+=1
        while array1 and counter<half:
            counter+=1
            array1.pop(0)
        while array2 and counter<half:
            counter+=1
            array2.pop(0)
        #now counter=half
        top=None
        if array1 and array2:
            top=array1.pop(0) if array1[0]<array2[0] else array2.pop(0)
        elif array1:
            top=array1.pop(0)
        elif array2:
            top=array2.pop(0)
        if not even:
            return float(top)
        if array1 and array2:
            top+=array1.pop(0) if array1[0]<array2[0] else array2.pop(0)
        elif array1:
            top+=array1.pop(0)
        elif array2:
            top+=array2.pop(0)
        return float(top)/2

ins=Solution()

print ins.findMedianSortedArrays([1,3,6,9],[2,5,7])