#!/usr/bin/python
class Solution:
    def jiecheng(self,n):
        if n<=1:
            return 1
        else:
            return self.jiecheng(n-1)*n

    def trailingZeroes(self, n):
        outcome=self.jiecheng(n)
        ret = 0
        while outcome%10==0:
            ret+=1
        return ret

if __name__ == '__main__':
	ins=Solution()
    print 'hehe'