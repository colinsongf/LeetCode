LEFT_TO_RIGHT, RIGHT_TO_LEFT = 0, 1

def recursive(n, l_o_r):
    if n == 1:
        return 1
    if l_o_r == LEFT_TO_RIGHT:
        return recursive(n / 2, RIGHT_TO_LEFT) * 2
    else:#RIGHT_TO_LEFT
        if n % 2 == 1:
            return recursive(n / 2, LEFT_TO_RIGHT) * 2
        else:
            return recursive(n / 2, LEFT_TO_RIGHT) * 2 - 1

class Solution(object):
    def lastRemaining(self, n):
        return recursive(n, LEFT_TO_RIGHT)
