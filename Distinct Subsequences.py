class Solution:
    def numDistinct(self,S,T):
        size1,size2=len(S),len(T)
        if not size1 or not size2:
            return 0
        m=[[0 for y in range(size2)] for x in range(size1)]
        #init
        m[0][0]=1 if S[0]==T[0] else 0
        #for j in range(1,size2):
        #    m[0][j]=0
        for i in range(1,size1):
            m[i][0]=m[i-1][0]+1 if S[i]==T[0] else m[i-1][0]
        for i in range(1,size1):
            for j in range(1,size2):
                m[i][j]=m[i-1][j-1]+m[i-1][j] if S[i]==T[j] else m[i-1][j]
        return m[size1-1][size2-1]
