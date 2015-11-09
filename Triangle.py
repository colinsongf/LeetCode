class Solution(object):
    def minimumTotal(self, triangle):
        d = []
        size = len(triangle)
        for i in range(size):
            isize=len(triangle[i])
            d.append([0 for x in range(isize)])
        #init
        d[0][0]=triangle[0][0]
        for i in range(1,size):
            d[i][0]=triangle[i][0]+d[i-1][0]
        for i in range(1,size):
            isize =len(triangle[i])
            d[i][isize-1]=triangle[i][isize-1]+d[i-1][isize-2]
        #dynamic
        for i in range(1,size):
            isize=len(triangle[i])
            for j in range(1,isize-1):
                d[i][j]=triangle[i][j]+min(d[i-1][j-1],d[i-1][j])
        return min(d[size-1])
