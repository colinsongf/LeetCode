class Solution:
    def rob(self, num):
        size=len(num)
        if size==0:
            return 0
        if size==1:
            return num[0]
        if size==2:
            return max(num[0],num[1])
        money=0
        m=[0 for x in range(size)]
        m[0],m[1],m[2]=num[0],num[1],num[0]+num[2]
        for i in range(3,size):
            m[i]=max(m[i-2],m[i-3])+num[i]
        return max(m[size-2],m[size-1])
