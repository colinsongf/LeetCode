class Solution:
    def calculateMinimumHP(self, dungeon):
        row,col=len(dungeon),len(dungeon[0])
        m=[[0 for y in range(col)] for x in range(row)]
        
        for i in range(1,row):
