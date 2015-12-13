class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        level1,level2 = version1.split('.'),version2.split('.')
        i = 0
        size1,size2 = len(level1),len(level2)
        if size1 > size2:
            while i < size1-size2:
                i += 1
                level2.append('0')
        else:
            while i < size2-size1:
                i += 1
                level1.append('0')
        status = 0
        for l1,l2 in zip(level1,level2):
            if status:
                break
            if int(l1) < int(l2):
                status = -1
            elif int(l1) > int(l2):
                status = 1
        return status