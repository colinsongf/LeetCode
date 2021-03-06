class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self,A,m,B,n):
        i,j=0,0
        while i<m and j<n:
            if A[i]<=B[j]:
                i+=1
            else:
                A[i:i+1]=[B[j],A[i]]
                i+=1
                j+=1
                m+=1
        while j<n:
            A[i]=B[j]
            i+=1
            j+=1