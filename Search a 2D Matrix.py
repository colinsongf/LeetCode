class Solution:
    def searchIt(self,matrix,r_start,r_end,c_start,c_end,target):
        if r_start>=r_end or c_start>=c_end:
            return False
        i,j=(r_start+r_end)/2,(c_start+c_end)/2
        mid = matrix[i][j]
        if mid == target:
            return True
        elif mid < target:
            return (self.searchIt(matrix,r_start,i+1,j+1,c_end,target) or self.searchIt(matrix,i+1,r_end,c_start,c_end,target))
        else:
            return (self.searchIt(matrix,r_start,i,j,c_end,target) or self.searchIt(matrix,r_start,r_end,c_start,j,target))
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        row,col = len(matrix),len(matrix[0])
        return self.searchIt(matrix,0,row,0,col,target)
