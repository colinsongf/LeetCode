class Solution:
    def minDistance(self , word1, word2):
        if word1==word2:
            return 0
        size1,size2=len(word1),len(word2)
        if not size1:
            return size2
        elif not size2:
            return size1
        m=[[0 for y in range(size2)] for x in range(size1)]
        m[0][0]=0 if word1[0]==word2[0] else 1
        #init m[i][0]
        for i in range(1,size1):
            m[i][0]=i if word1[i]==word2[0] else m[i-1][0]+1
        #init m[0][j]
        for j in range(1,size2):
            m[0][j]=j if word1[0]==word2[j] else m[0][j-1]+1
        #dyanmic
        for i in range(1,size1):
            for j in range(1,size2):
                if word1[i]==word2[j]:
                    m[i][j]=m[i-1][j-1]
                else:
                    m[i][j]=min(m[i-1][j-1],m[i][j-1],m[i-1][j])+1
        return m[size1-1][size2-1]
