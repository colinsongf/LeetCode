class Solution(object):
    def frequencySort(self, s):
        dic = {}
        for ch in s:
            if ch not in dic:
                dic[ch] = 1
            else:
                dic[ch] += 1
        keys = sorted(dic.keys(), key = lambda x: dic[x], reverse = True)
        string = ''
        for key in keys:
            counter = dic[key]
            string += key * counter
        return string
