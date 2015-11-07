class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        outcome = ''
        size1,size2=len(a),len(b)
        i,size=0,0
        if size1>size2:
            size=size1
            while i<size1-size2:
                b='0'+b
                i+=1
        else:
            size=size2
            while i<size2-size1:
                a='0'+a
                i+=1
        ret=0
        for i in range(size-1,-1,-1):
            ch1,ch2=a[i],b[i]
            sub=int(ch1)+int(ch2)+ret
            outcome=str(sub%2)+outcome
            ret=sub/2
        if ret:
            outcome='1'+outcome
        return outcome
        