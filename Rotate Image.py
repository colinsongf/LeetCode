class Solution:
    def rotate(self, matrix):
        size = len(matrix)
        tmp = [[0 for x in range(size)] for x in range(size)]
        for i in range(size):
            for j in range(size):
                tmp[i][j]=matrix[size-1-j][i]
        for i in range(size):
            matrix[i]=tmp[i][:]
        return matrix
