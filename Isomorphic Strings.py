class Solution:
    def isIsomorphic(self, s, t):
        if len(s)!=len(t):
            return False
        mydict1,mydict2={},{}
        for i,j in zip(s,t):
            if i not in mydict1:
                mydict1[i]=j
            else:
                if mydict1[i]!=j:
                    return False
            if j not in mydict2:
                mydict2[j]=i
            else:
                if mydict2[j]!=i:
                    return False
        return True
