class Solution:
    def isInterleave(self, s1,s2,string):
        size1,size2,size=len(s1),len(s2),len(string)
        if size1+size2!=size:
            return False
        if not size1 and not size2 and not size:
            return True
        elif not size1:
            return s2==string
        elif not size2:
            return s1==string
        m=[[False for y in range(size2+1)] for x in range(size1+1)]
        #init
        m[1][0]=True if s1[0]==string[0] else False
        for i in range(2,size1+1):
            if s1[i-1]==string[i-1]:
                m[i][0]=m[i-1][0]
        m[0][1]=True if s2[0]==string[0] else False
        for j in range(2,size2+1):
            if s2[j-1]==string[j-1]:
                m[0][j]=m[0][j-1]
        #dynamic
        for i in range(1,size1+1):
            for j in range(1,size2+1):
                k=i+j-1
                if s1[i-1]==string[k]:
                    m[i][j]=m[i-1][j]
                if s2[j-1]==string[k]:
                    m[i][j]=m[i][j] or m[i][j-1]
        return m[size1][size2]
