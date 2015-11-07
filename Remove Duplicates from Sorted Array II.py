class Solution:
    def removeDuplicates(self,array):
        if not array:
            return 0
        addPos = 1
        counter = 1
        prev=array[0]
        for num in array[1:]:
            if num==prev:
                counter+=1
                if counter<=2:
                    array[addPos]=num
                    addPos+=1
            else:
                counter=1
                prev=num
                array[addPos]=num
                addPos+=1
        return addPos

ins=Solution()

print ins.removeDuplicates([1,1,1,2,2,3])