class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def largestRectangleArea(self, height):
        size=len(height)
        if not size:
            return 0
        if size==1:
            return height[0]
        maxarea=0
        stack=[]
        for i,hei in enumerate(height):
            if not stack or hei >= stack[-1][1]:
                stack.append((i,hei))
            else:
                last=-1
                while stack and stack[-1][1]>=hei:
                    maxarea=max(maxarea,(i-stack[-1][0])*stack[-1][1])
                    last=stack[-1][0]
                    stack.pop()
                stack.append((last,hei))
        if stack:
            while stack:
                maxarea=max(maxarea,(size-stack[-1][0])*stack[-1][1])
                stack.pop()
        return maxarea
    def maximalRectangle(self, matrix):
        row=len(matrix)
        if not row:
            return 0
        col=len(matrix[0])
        h=[[int(matrix[y][x]) for x in range(col)] for y in range(row)]
        for i in range(1,row):
            for j in range(col):
                if h[i][j]:
                    h[i][j]+=h[i-1][j]
        maxvalue=self.largestRectangleArea(h[0])
        for i in range(1,row):
            maxvalue=max(maxvalue,self.largestRectangleArea(h[i]))
        return maxvalue
        
        