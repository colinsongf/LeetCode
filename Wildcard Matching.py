class Solution:
    def isMatch(self , string ,pattern):
        if string==pattern:
            return True
        size1,size2=len(string),len(pattern)
        if not size1:
            for ch in pattern:
                if ch!='*':
                    return False
            return True
        if not size2:
            return False
        m=[[0 for y in range(size2)] for x in range(size1)]
        if string[0]==pattern[0] or pattern[0]=='?' or pattern=='*':
            m[0][0]=1
        
        k_record=[0 for x in range(size2)]

        #init m[i][0]
        for i in range(1,size1):
            if pattern[0]=='*':
                m[i][0]=1
                k_record[0]=1
        #init m[0][j]
        for j in range(1,size2):
            if pattern[j]=='*':
                m[0][j]=m[0][j-1]
                if m[0][j]:
                    k_record[j]=1
        for i in range(1,size1):
            for j in range(1,size2):
                if pattern[j]==string[i] or pattern[j]=='?':
                    m[i][j]=m[i-1][j-1]
                elif pattern[j]=='*':
                    if k_record[j-1]:
                        m[i][j]=1
                    #for k in range(i-1,-1,-1):
                    #    if m[k][j-1]==1:
                    #        m[i][j]=1
                    #        break
                if m[i][j]:
                    k_record[j]=1
        return True if m[size1-1][size2-1] else False