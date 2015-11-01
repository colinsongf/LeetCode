class Solution:
    def deleteOne(self, counter, key):
        if counter[key] == 1:
            del counter[key]
        else:
            counter[key] -= 1
    def getHint(self, secret, guess):
        counter = {}
        corret, wrong = 0, 0
        for ch_s, ch_g in zip(secret, guess):
            if ch_s != ch_g:
                counter[ch_s] = counter.get(ch_s, 0) + 1
        for ch_s, ch_g in zip(secret, guess):
            if ch_s == ch_g:
                corret += 1
            elif ch_g in counter:
                wrong += 1
                self.deleteOne(counter, ch_g)
        return '%dA%dB' % (corret, wrong)