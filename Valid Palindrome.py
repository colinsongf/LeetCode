class Solution(object):
    def isPalindrome(self, string):
        flag = True
        string=[ch for ch in string if ch in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
        size=len(string)
        hsp,rsp=0,size-1
        while hsp<rsp:
            if string[hsp].upper()!=string[rsp].upper():
                flag = False
                break
            hsp += 1
            rsp -= 1
        return flag  

ins = Solution()
print ord('A')<=ord('`')<=ord('z')# or ord('0')<=ord('`')<=ord('9')
print ord('A')
print ord('`')
print ins.isPalindrome('`l;`` 1o1 ??;l`')