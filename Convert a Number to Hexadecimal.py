class Solution(object):
    def positiveToHex(self, num):
        string = ''
        if num == 0:
            return '0'
        hexHash = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        while num:
            string = hexHash[num % 16] + string
            num /= 16
        return string
    def toHex(self, num):
        if num < 0:
            num = 2**31 + num
            string = self.positiveToHex(num)
            if len(string) == 8:
                first = string[0]
                string = string[1:]
                head = int(first) + 8
                hexHash = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
                string = hexHash[head] + string
            else:
                while len(string) < 7:
                    string = '0' + string
                string = '8' + string
            return string
        else:
            return self.positiveToHex(num)
