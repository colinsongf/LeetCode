class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations=sorted(citations)
        m=len(citations)
        h=0
        for i in xrange(m):
            if citations[i]<m-1-i:
                h=citations[i]
            elif citations[i]>=m-i:
                h=max(h,m-i)
                break
        return h
