class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for row in range(9):
            hashmap={}
            for i in board[row]:
                if i=='.':continue
                if i in hashmap:
                    return False
                hashmap[i]=0
        for col in range(9):
            hashmap={}
            array=[board[x][col] for x in range(9)]
            for i in array:
                if i=='.':continue
                if i in hashmap:
                    return False
                hashmap[i]=0
        for row in range(0,9,3):
            for col in range(0,9,3):
                hashmap={}
                array=board[row][col:col+3]
                array+=(board[row+1][col:col+3])
                array+=(board[row+2][col:col+3])
                for i in array:
                    if i=='.':continue
                    if i in hashmap:
                        return False
                    hashmap[i]=0
        return True