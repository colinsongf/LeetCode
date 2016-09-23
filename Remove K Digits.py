class Solution(object):
    def function(self, array, delete):
        current_size = len(array)
        candidate = delete + 1
        min_one = 10
        pos = -1
        for i in range(candidate):
            if array[i] < min_one:
                min_one = array[i]
                pos = i
        if candidate == len(array):
            real_delete = delete
            array = []
        else:
            real_delete = pos
            array = array[pos + 1: ]
        choose = min_one
        return real_delete, choose, array

    def removeKdigits(self, num, k):
        if len(num) <= k:
            return "0"
        array = [int(ch) for ch in num]
        answer = ''
        while k > 0:
            real_delete, choose, array = self.function(array, k)
            k -= real_delete
            answer += str(choose)
        if array:
            answer += (''.join([str(i) for i in array]))
        answer = int(answer)
        return str(answer)
