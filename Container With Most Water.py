class Solution:
    # @return an integer
    def maxArea(self, height):
        size=len(height)
        hsp,rsp=0,size-1
        v = 0
        while hsp<rsp:
            hi,hj=height[hsp],height[rsp]
            if min(hi,hj)*(rsp-hsp) > v:
                v=min(hi,hj)*(rsp-hsp)
            if hi>hj:
                rsp-=1
            else:
                hsp+=1
        return v