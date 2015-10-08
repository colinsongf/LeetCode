class Solution:
    # @return a string
    def locater(self,lineno,nRows):
        while True:
            yield 2*(nRows-lineno-1)
            yield 2*lineno

    def convert(self, string, nRows):
        if nRows==1:
            return string
        zigzag=[]
        size=len(string)
        for i in range(nRows):
            if i==0 or i==nRows-1:
                while i<size:
                    zigzag.append(string[i])
                    i+=2*(nRows-1)
            else:
                jmp=self.locater(i,nRows)
                while i<size:
                    zigzag.append(string[i])
                    i+=jmp.next()
        zigzag=''.join(zigzag)
        return zigzag       