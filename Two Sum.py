class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, array, target):
        size=len(array)
        bitmap={}.fromkeys(array,0)
        posmap={}.fromkeys(range(size),-1)
        reversearray=array[::-1]
        for num in array:
            bitmap[num]+=1
        before = 0
        for key in sorted(bitmap.keys()):
            bitmap[key]+=before
            before = bitmap[key]
        for i,num in enumerate(reversearray):
            origin_pos = size-1-i
            new_pos = bitmap[num]-1
            bitmap[num]-=1
            array[new_pos]=num
            posmap[new_pos]=origin_pos
        i,j=0,size-1
        while i<j and i<size and j>=0:
            if array[i]+array[j]>target:
                j-=1
            elif array[i]+array[j]<target:
                i+=1
            else:
                reti,retj=posmap[i]+1,posmap[j]+1
                return (reti,retj) if reti < retj else (retj,reti)