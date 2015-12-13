class Solution:
    def wordPattern(self, pattern, str):
        words = str.split(' ')
        mydict1, mydict2 = {}, {}
        if len(words) != len(pattern):
            return False
        for ch, word in zip(pattern, words):
            if ch not in mydict1:
                mydict1[ch] = word
            else:
                if mydict1[ch] != word:
                    return False
            if word not in mydict2:
                mydict2[word] = ch
            else:
                if mydict2[word] != ch:
                    return False
        return True
