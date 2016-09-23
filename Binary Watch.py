class Solution(object):
    def bitCount(self, number):
        counter = 0
        while number:
            number &= (number - 1)
            counter += 1
        return counter
    def __init__(self):
        self.hash = {}
        for number in range(60):
            bitcount = self.bitCount(number)
            if bitcount not in self.hash:
                self.hash[bitcount] = []
            self.hash[bitcount].append(number)

    def readBinaryWatch(self, num):
        final = []
        for hour in range(num + 1):
            minu = num - hour
            if hour not in self.hash or minu not in self.hash:
                continue
            hourSelect = [h for h in self.hash[hour] if h < 12]
            minSelect = self.hash[minu]
            answer = [(h, m) for h in hourSelect for m in minSelect]

            for t in answer:
                hs = str(t[0]) + ':'
                ms = str(t[1]) if t[1] > 9 else ('0' + str(t[1]))
                final.append(hs + ms)
        return final
