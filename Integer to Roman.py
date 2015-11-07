class Solution:
    def intToRoman(self, num):
        table={
        1:['','I','II','III','IV','V','VI','VII','VIII','IX','IIX'],
        2:['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC','XXC'],
        3:['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM','CCM',],
        4:['','M','MM','MMM']}
        strnum=str(num)[::-1]
        roman=''
        for i,n in enumerate(strnum):
            index=int(n)
            roman=table[i+1][index]+roman
        return roman

ins=Solution()
print ins.intToRoman(93)