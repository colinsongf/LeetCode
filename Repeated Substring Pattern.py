def getMayBeSubstring(string):
    if len(string) <= 1:
        return False
    str_start = string[0]
    str_end = string[-1]

    start_choose = []
    end_choose = []

    for i in range(len(string) / 2):
        if string[i] == str_start:
            start_choose.append(i)
        if string[i] == str_end:
            end_choose.append(i)
    for start in start_choose:
        for end in end_choose:
            if start > end:
                continue
            sub_size = end - start + 1
            sub_str = string[start: end + 1]
            counter = len(string) / sub_size
            if sub_str * counter == string:
                return True
    return False

class Solution(object):
    def repeatedSubstringPattern(self, string):
        return getMayBeSubstring(string)
