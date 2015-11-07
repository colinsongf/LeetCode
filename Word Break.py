class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self,string,dict):
        size=len(string)
        if not size:
            return False
        m=[[False for y in range(size)] for x in range(size)]
        for i in range(size):
            if string[i] in dict:
                m[i][i]=True
        for l in range(2,size+1):
            for i in range(0,size+1-l):
                j=i+l-1
                m[i][j]=False
                for k in range(i,j):
                    if m[i][k] and m[k+1][j]:
                        m[i][j]=True
                        break
                if not m[i][j]:
                    if string[i:j+1] in dict:
                        m[i][j]=True
        return m[0][size-1]