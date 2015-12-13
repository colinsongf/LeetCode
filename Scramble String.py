class Solution:
    def hashEqual(self,hash1,hash2):
        key1,key2=set(hash1.keys()),set(hash2.keys())
        if key1-key2 or key2-key1:
            return False
        for key in hash1:
            if hash1[key]!=hash2[key]:
                return False
        return True
    def isScramble(self,s1,s2):
        if len(s1)!=len(s2):
            return False
        return self.isScramble_real(s1,s2)
    def createHash(self, string):
        yourhash={}.fromkeys(string,0)
        for ch in string:
            yourhash[ch]+=1
        return yourhash
    def isScramble_real(self,str1,str2):
        size1,size2 = len(str1),len(str2)
        hash1,hash2=self.createHash(str1),self.createHash(str2)
        if not self.hashEqual(hash1,hash2):
            return False
        if size1<=2:
            return True
        for i in range(1,size1):
            if self.isScramble_real(str1[:i],str2[:i]) and self.isScramble_real(str1[i:],str2[i:]):
                return True
            if self.isScramble_real(str1[:i],str2[-i:]) and self.isScramble_real(str1[i:],str2[:-i]):
                return True
        return False