class Solution:
    def pow(self, x, n):
        #return x**n
        flag = False
        if n < 0:
            flag = True
            n=(-1)*n
        binary = bin(n)[2:]
        ret = 1
        for b in binary:
            ret *= ret
            if b=='1':
                ret *= x
        if flag:
            ret = 1.0/ret
        return ret

ins=Solution()
print ins.pow(34.00515,-3)