class Solution(object):
    def maxProduct(self, array):
        size,maxvalue = len(array),-2*32
        dmax,dmin=[[0 for x in range(size)] for y in range(size)],[[0 for x in range(size)] for y in range(size)]
        #init
        for i in range(size):
            dmax[i][i]=dmin[i][i]=array[i]
            if dmax[i][i] > maxvalue:
                maxvalue = dmax[i][i]
        #dynamic
        for l in range(2,size):
            for i in range(size-l+1):
                j = i+ l -1
                dmax[i][j]=max(dmax[i][j-1]*array[j],dmin[i][j-1]*array[j])
                if dmax[i][j] > maxvalue:
                    maxvalue = dmax[i][j]
                dmin[i][j]=min(dmax[i][j-1]*array[j],dmin[i][j-1]*array[j])
        return maxvalue
    def maxProduct_less_memory(self, array):
        size,maxvalue=len(array),-2**32
        for i in range(size):
            imax=imin=array[i]
            if imax > maxvalue:
                maxvalue=imax
            for j in range(i+1,size):
                mymax = max(imax*array[j],imin*array[j])
                mymin = min(imax*array[j],imin*array[j])
                mymax,mymin=imax,imin
                if imax > maxvalue:
                    maxvalue=imax
        return maxvalue
    def maxProduct_less_time(self, array):
        size,maxvalue=len(array),array[0]
        imax = imin = array[0]
        for i in range(1,size):
            mymax = max(imax*array[i],imin*array[i],array[i])
            mymin = min(imax*array[i],imin*array[i],array[i])
            imax,imin = mymax,mymin
            if imax > maxvalue:
                maxvalue=imax
        return maxvalue